"""
This file contains various methods for solving the diffusion equation in both
one and two dimensions.

In one dimension:
    - Neural network solver
    - Forward-euler
    - Backward-euler
    - Crank-Nicolson

Solves the problem du/dt = d^2u/dx^2
with chosen boundary conditions.

In two dimensions:
    - Forward-euler

Solves the problem du/dt = d^2u/dx^2 + d^2u/dy^2
with chosen boundary conditions.

"""
import numpy as np
from numba import jit
import time
import pytest
import multiprocessing as mp
import scipy as sc
from scipy.sparse.linalg import spsolve

import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
tf.reset_default_graph()

# import numpy as np
# from matplotlib import cm
# from matplotlib import pyplot as plt
# from mpl_toolkits.mplot3d import axes3d
# import time

def nn_diffusion_solver(num_iter, lr, reg_param, num_hidden_neurons, points, x, t):
    """Function for calculating the MSE of the neural network solution of the diffusion equation.

    Parameters
    ----------
    num_iter: int
        Number of iterations in training the network.
    lr: float
        Learning rate in gradient descent in training the network.
    reg_param: float
        Regularization parameter in the loss function.
    num_hidden_neurons: list
        List of number of neurons in each layer.
    points: numpy 2d array
        Training data.
    x: numpy array
        x-values.
    t: numpy array
        t-values.

    Returns
    -------
    g_dnn: numpy array
        Solution from the neural network
    g_analytic: numpy array
        Analytical solution

    """

    #Sets up the neural network with the wanted structure.
    with tf.variable_scope('dnn'):
        num_hidden_layers = np.size(num_hidden_neurons)

        previous_layer = points

        for l in range(num_hidden_layers):
            current_layer = tf.layers.dense(previous_layer, num_hidden_neurons[l],activation=tf.nn.sigmoid)
            previous_layer = current_layer

        dnn_output = tf.layers.dense(previous_layer, 1)

    #Defines the h_1 function.
    def u(x):
        return tf.sin(np.pi*x)

    regularization_parameter = reg_param

    #Create the zero vector to compare the loss to.
    zeros = tf.reshape(tf.convert_to_tensor(np.zeros(x.shape)),shape=(-1,1))

    #Sets up the loss function of the problem.
    with tf.name_scope('loss'):
        g_trial = (1-t)*u(x) + x*(1-x)*t*dnn_output

        #Differntiates with respect to t and x(twice) using tensorflows autograd.
        g_trial_dt = tf.gradients(g_trial, t)
        g_trial_d2x = tf.gradients(tf.gradients(g_trial,x),x)

        #Extracts the regularization loss.
        reg_losses = tf.get_collection(tf.GraphKeys.REGULARIZATION_LOSSES)

        #Sets up the loss function as described in the report.
        loss = tf.losses.mean_squared_error(zeros, g_trial_dt[0] - g_trial_d2x[0]) + regularization_parameter*sum(reg_losses)

    learning_rate = lr

    #Train the neural network with the given learning rate. Gradient descent is used as standard.
    with tf.name_scope('train'):
        optimizer = tf.train.GradientDescentOptimizer(learning_rate)
        traning_op = optimizer.minimize(loss)


    init = tf.global_variables_initializer()

    #Calculates the analytic solution.
    g_analytic = tf.exp(-np.pi**2*t)*tf.sin(np.pi*x)
    g_dnn = None

    losses = []
    iterations = []

    # Executes the network as described in training.
    time_start = time.time()
    with tf.Session() as sess:
        init.run()
        for i in range(num_iter):
            sess.run(traning_op)

            if i % 1000 == 0:
                l = loss.eval()
                print("Step:", i, "/",num_iter, "loss: ", l)
                losses.append(l)
                iterations.append(i)

        g_analytic = g_analytic.eval()
        g_dnn = g_trial.eval()
    time_end = time.time()
    print("Time = ", time_end - time_start, " seconds")
    return g_analytic, g_dnn, losses, iterations


def forward_euler(x_min, x_max, dx, dt, t, g, a, b):
    """Solves the heat equation using forward euler.

    Function for solving the diffusion equation in one dimension with
    given boundary conditions.

    Parameters
    ----------
    x_min: float
        Lower limit of spacial dimension.
    x_max: float
        Upper limit of spacial dimension.
    dx: float
        Spacing between spacial points.
    dt: float
        Spacing between time steps.
    t: float
        max time step.
    g: function(x)
        Initial condition for u(x,0).
    a: function(t)
        Boundary condition u(0,t)
    b: function(t)
        Boundary condition u(x_max,t)

    Returns
    -------
    solutions: numpy matrix
        Contains the solution for each time step up to t.
        First dimension: Time steps
        Second dimension: Spacial steps.
    """

    num_t_values = int(float(t)/dt + 1)
    num_x_values = int(float(x_max - x_min)/dx + 1)

    #Matrix the will contain the solution for each time-step.
    u = np.zeros((num_t_values, num_x_values))

    #Vectors for x-values and t_values in the grid.
    x_values = np.linspace(x_min, x_max, num_x_values)
    t_values = np.linspace(0, t, num_t_values)

    alpha = dt/(dx**2)

    #Loops over the u-matrix and sets the boundary conditions.
    for t_index in range(0, num_t_values):
        u[t_index, 0] = a(t_values[t_index])
        u[t_index, -1] = b(t_values[t_index])

    #Loops over the u-matrix and sets the initial conditions.
    for x_index in range(1, num_x_values-1):
        u[0, x_index] = g(x_values[x_index])

    start_time = time.time()
    #Calls function for solving for all time values and times it.
    u = update_forward_euler(num_t_values, num_x_values, u, alpha)
    end_time = time.time()

    print("Time used forward Euler: ", end_time - start_time, " seconds")

    return u

@jit(nopython=True)
def update_forward_euler(num_t_values, num_x_values, u, alpha ):
    """Function for finding the u-matrix in forward euler.

    Parameters
    ----------
    num_t_values: int
        Number of t-values in the grid.
    num_x_values: int
        Number of x-values in the grid.
    u: numpy 2d-array
        Empty matrix that will contain the solution for each time-step.
    alpha: float

    Returns
    -------
    u: numpy 2d-array
        Matrix that contains the solution for each time-step.
    """
    for t_index in range(1, num_t_values):
        for x_index in range(1, num_x_values-1):
            #Updating for the next time-step using vectorization of the forward euler step.
            u[t_index, x_index] = alpha*(u[t_index-1, x_index + 1] - 2*u[t_index-1, x_index] + u[t_index-1, x_index - 1]) + u[t_index-1, x_index]

    return u

def backward_euler(x_min, x_max, dx, dt, t, g, a, b):
    """Solves the heat equation using backward euler.

    Parameters
    ----------
    x_min: float
        Lower limit of spacial dimension.
    x_max: float
        Upper limit of spacial dimension.
    dx: float
        Spacing between spacial points.
    dt: float
        Spacing between time steps.
    t: float
        max time step.
    g: function(x)
        Initial condition for u(x,0).
    a: function(t)
        Boundary condition u(0,t)
    b: function(t)
        Boundary condition u(x_max,t)

    Returns
    -------
    solutions: numpy matrix
        Contains the solution for each time step up to t.
        First dimension: Time steps
        Second dimension: Spacial steps.

    """

    num_t_values = int(float(t)/dt + 1)
    num_x_values = int(float(x_max - x_min)/dx + 1)

    #Matrix with solution for each time step.
    u = np.zeros((num_t_values, num_x_values))

    x_values = np.linspace(x_min, x_max, num_x_values)
    t_values = np.linspace(0, t, num_t_values)

    #Initializes matrix with boundary conditions.
    for t_index in range(0, num_t_values):
        u[t_index, 0] = a(t_values[t_index])
        u[t_index, -1] = b(t_values[t_index])

    #Initializes matrix with initial conditions.
    for x_index in range(1, num_x_values-1):
        u[0, x_index] = g(x_values[x_index])

    #Sets up the matrix on the l.h.s.
    A = 2*np.eye(num_x_values) - np.eye(num_x_values, k=1) - np.eye(num_x_values, k=-1)

    A = np.eye(num_x_values) + (dt/(dx**2))*A

    A[0,0] = A[-1,-1] = 1
    A[0,1] = A[-1,-2] = 0

    start_time = time.time()
    #Calculates solution for each time step and times it.
    u = update_backward_euler(num_t_values, num_x_values, u, dt, A)
    end_time = time.time()

    print("Time used backward Euler: ", end_time - start_time, " seconds")

    return u

# @jit(nopython=True)
def update_backward_euler(num_t_values, num_x_values, u, dt, A):
    """Function for finding the u-matrix in backward euler.


    Uses the scipy sparse functionality to solve the tridiagonal system of equations.
    This speeds up the process significantly.

    Parameters
    ----------
    num_t_values: int
        Number of t-values in the grid.
    num_x_values: int
        Number of x-values in the grid.
    u: numpy 2d-array
        Empty matrix that will contain the solution for each time-step.
    dt: float
        Grid space.
    alpha: float

    Returns
    -------
    u: numpy 2d-array
        Matrix that contains the solution for each time-step.

    """
    A = sc.sparse.csc_matrix(A)
    for i in range(1, num_t_values):
        u[i,:] = spsolve(A , u[i-1, :] )
        u[i,-1] = 1
        u[i,0] = 0
    return u

def crank_nicolson(x_min, x_max, dx, dt, t, g, a, b):
    """Solves the heat equation using crank nicolson.

    Parameters
    ----------
    x_min: float
        Lower limit of spacial dimension.
    x_max: float
        Upper limit of spacial dimension.
    dx: float
        Spacing between spacial points.
    dt: float
        Spacing between time steps.
    t: float
        max time step.
    g: function(x)
        Initial condition for u(x,0).
    a: function(t)
        Boundary condition u(0,t)
    b: function(t)
        Boundary condition u(x_max,t)

    Returns
    -------
    solutions: numpy matrix
        Contains the solution for each time step up to t.
        First dimension: Time steps
        Second dimension: Spacial steps.

    """
    num_t_values = int(float(t)/dt + 1)
    num_x_values = int(float(x_max - x_min)/dx + 1)

    #Initializes matrix to contain solution for each time step.
    u = np.zeros((num_t_values, num_x_values))

    x_values = np.linspace(x_min, x_max, num_x_values)
    t_values = np.linspace(0, t, num_t_values)

    #Initializes the boundary conditions.
    for t_index in range(0, num_t_values):
        u[t_index, 0] = a(t_values[t_index])
        u[t_index, -1] = b(t_values[t_index])

    #Initializes the initial value for t = 0.
    for x_index in range(1, num_x_values-1):
        u[0, x_index] = g(x_values[x_index])

    alpha = dt/(dx**2)

    #Sets up the matrix.
    A = 2*np.eye(num_x_values) - np.eye(num_x_values, k=1) - np.eye(num_x_values, k=-1)


    A[0,0] = A[-1,-1] = 1
    A[0,1] = A[-1,-2] = 0

    start_time = time.time()
    #Calculates the solution for each time step.
    u = update_cn(num_t_values, num_x_values, u, alpha, A)
    end_time = time.time()

    print("Time used Crank Nicolson : ", end_time - start_time, " seconds")

    return u

def update_cn(num_t_values, num_x_values, u, alpha, A):
    """Function for finding the u-matrix in Crank-Nicolson.

    Parameters
    ----------
    num_t_values: int
        Number of t-values in the grid.
    num_x_values: int
        Number of x-values in the grid.
    u: numpy 2d-array
        Empty matrix that will contain the solution for each time-step.
    dt: float
        Grid space.
    A: numpy 2d-array
        The difference scheme matrix. Tridiagonal.

    Returns
    -------
    u: numpy 2d-array
        Matrix that contains the solution for each time-step.

    """
    print(A)

    temp1 = (2*np.eye(num_x_values) + alpha*A)
    print(temp1)
    temp1[0,0] = temp1[-1,-1] = 1
    temp1[0,1] = temp1[-1,-2] = 0
    temp1 = sc.sparse.csc_matrix(temp1)

    temp2 = 2*np.eye(num_x_values) - alpha*A
    temp2[0,0] = temp2[-1,-1] = 1
    temp2[0,1] = temp2[-1,-2] = 0

    for i in range(1, num_t_values):
        forward_step = np.dot(temp2,u[i-1,:])
        u[i,:] = spsolve(temp1,forward_step)
        u[i,-1] = 1
        u[i,0] = 0

    return u

def forward_euler_2d(x_min, x_max, y_min, y_max, dx, dy, dt, t, g):
    """Solves the heat equation in 2 dimensions using forward euler.

    Parameters
    ----------
    x_min: float
        Lower limit of x-dimension.
    x_max: float
        Upper limit of x-dimension.
    y_min: float
        Lower limit of y-dimension.
    y_max: float
        Upper limit of y-dimension.
    dx: float
        Spacing between each grid point in x-dimension.
    dy: float
        Spacing between each grid point in y-dimension.
    dt: float
        Spacing between time steps.
    t: float
        max time step.
    g: function(x,y)
        Initial condition at time = 0.

    Returns
    -------
    u: numpy matrix
        Contains the solution for the last time step.
        First dimension: y-coordinates
        Second dimension: x-coordinates.
    x_values: numpy vector
        Vector containing the grid points in x-direction.
    y_values: numpy vector
        Vector containing the grid points in y-direction.
    """

    num_t_values = int(float(t)/dt + 1)
    num_x_values = int(float(x_max - x_min)/dx + 1)
    num_y_values = int(float(y_max - y_min)/dy + 1)

    save_num_between = 10

    #Matrix for previous timestep.
    u_prev = np.zeros((num_y_values, num_x_values))

    x_values = np.linspace(x_min, x_max, num_x_values)
    y_values = np.linspace(y_min, y_max, num_y_values)

    t_values = np.linspace(0, t, num_t_values)

    alpha = dt/(dx**2)

    initialize_matrix(num_x_values, x_values, num_y_values, y_values, u_prev, g)

    start_time = time.time()
    u = iterate(num_t_values, num_x_values, u_prev, dt, dx, dy)
    end_time = time.time()
    print("time: ", end_time - start_time, " seconds")

    return u, x_values, y_values


@jit(nopython=True)
def iterate(num_t_values, num_x_values, u_prev, dt, dx, dy):
    for t_index in range(1, num_t_values):
        u_prev[1:-1, 1:-1] = u_prev[1:-1, 1:-1] + dt*(  (u_prev[0:-2, 1:-1] -2*u_prev[1:-1,1:-1] + u_prev[2:,1:-1])/(dx**2) + \
                                                    (u_prev[1:-1, 0:-2] -2*u_prev[1:-1,1:-1] + u_prev[1:-1,2:])/(dy**2)  )
    return u_prev

def initialize_matrix(num_x_values, x_values, num_y_values, y_values, u_prev, g):
    for x_index in range(1, num_x_values-1):
        for y_index in range(1, num_y_values-1):
            u_prev[y_index, x_index] = g(x_values[x_index],y_values[y_index])

    for y_index in range(0, num_y_values):
        u_prev[y_index, 0] = 0
        u_prev[y_index, -1] = 0

    for x_index in range(0, num_x_values):
        u_prev[0, x_index] = 0
        u_prev[-1, x_index] = 0

def analytic_solution_1D(x_values, t):
    """Analtytic solution to the diffusion equation with u(x,0) = 0, u(0,t) = 0 and u(1,t) = 1.

    Parameters
    ----------
    x_values: numpy vector
        Vector with x-values in the grid.
    t: float
        The time step to calculate the numerical solution.

    Returns
    -------
    Returns the values of the analytical solution at the grid points for the given
    initial conditions and boundary conditions.
    """
    return np.sin(np.pi*x_values)*np.exp((-np.pi**2)*t)

def analytic_solution_2D(x_values, y_values, t):
    """Analytic solution to the diffusion equation in two dimensions.

    Solution for the initial condition u(x,y,0) = sin(pi*x)*sin(pi*y) and the boundary
    conditions equal to zero.

    Parameters
    ----------
    x_values: numpy vector
        Vector with x-values in the grid.
    y_values: numpy vector
        Vector with y-values in the grid.
    t: float
        The time step to calculate the numerical solution.

    Returns
    -------
    Returns the values of the analytical solution at the grid points for the given
    initial conditions and boundary conditions.

    """
    return np.sin(np.pi*x_values)*np.sin(np.pi*y_values)*np.exp(-2*(np.pi**2)*t)


def test_forward_euler_1():
    """Test if the boundary conditions are fulfilled for all steps.
    """
    x_min = 0
    x_max = 1

    dx = 0.01    #Spatial step
    dt = 0.5*(dx**2)#1e-3   #Time-step

    t = 1  #Max time

    num_x_values = (x_max - x_min)/dx
    num_t_values = float(t)/dt

    x_values = np.linspace(x_min, x_max, num_x_values +1)
    t_values = np.linspace(0, t, num_t_values+1)

    #Defining the boundary and intitial conditions for test1.
    g = (lambda x : 0)
    a = (lambda t : 0)
    b = (lambda t : 0)
    u_forward_euler = forward_euler(x_min, x_max, dx, dt, t, g, a, b)

    #checks if the boundary conditions are fulfilled.
    assert(u_forward_euler[0,0] == 0 and u_forward_euler[0,-1] == 0)
    assert(u_forward_euler[-1,0] == 0 and u_forward_euler[-1,-1] == 0)

def test_forward_euler_2():
    """Tests if the BC is fulfilled for all steps.
    """
    x_min = 0
    x_max = 1

    dx = 0.01    #Spatial step
    dt = 0.5*(dx**2)#1e-3   #Time-step

    t = 1  #Max time

    num_x_values = (x_max - x_min)/dx
    num_t_values = float(t)/dt

    x_values = np.linspace(x_min, x_max, num_x_values +1)
    t_values = np.linspace(0, t, num_t_values+1)
    #Defining the boundary conditions and initial conditions for test2.
    g = (lambda x : np.sin(np.pi*x))
    a = (lambda t : 0)
    b = (lambda t : 0)

    u_forward_euler = forward_euler(x_min, x_max, dx, dt, t, g, a, b)

    assert(u_forward_euler[0,0] == 0 and u_forward_euler[0,-1] == 0)
    assert(u_forward_euler[-1,0] == 0 and u_forward_euler[-1,-1] == 0)

def test_forward_euler_3():
    """Tests if the boundary conditons are fulfilled for all steps.
    """
    x_min = 0
    x_max = 1

    dx = 0.01    #Spatial step
    dt = 0.5*(dx**2)#1e-3   #Time-step

    t = 1  #Max time

    num_x_values = (x_max - x_min)/dx
    num_t_values = float(t)/dt

    x_values = np.linspace(x_min, x_max, num_x_values +1)
    t_values = np.linspace(0, t, num_t_values+1)

    g = (lambda x : 0)
    a = (lambda t : 0)
    b = (lambda t : 1)

    u_forward_euler = forward_euler(x_min, x_max, dx, dt, t, g, a, b)

    assert(u_forward_euler[0,0] == 0 and u_forward_euler[0,-1] == 1)
    assert(u_forward_euler[-1,0] == 0 and u_forward_euler[-1,-1] ==1)

def test_forward_euler_4():
    """Tests if it finds the correct solution for a simple case
    where the analytical solution is known. 
    """
    x_min = 0
    x_max = 1

    dx = 0.01    #Spatial step
    dt = 0.5*(dx**2)#1e-3   #Time-step

    t = 1  #Max time

    num_x_values = (x_max - x_min)/dx
    num_t_values = float(t)/dt

    x_values = np.linspace(x_min, x_max, num_x_values +1)
    t_values = np.linspace(0, t, num_t_values+1)

    g = (lambda x : 1-x)
    a = (lambda t : 0)
    b = (lambda t : 1)

    u_forward_euler = forward_euler(x_min, x_max, dx, dt, t, g, a, b)

    assert(u_forward_euler[0,0] == 0 and u_forward_euler[0,-1] == 1)
    assert(u_forward_euler[-1,0] == 0 and u_forward_euler[-1,-1] ==1)
    assert(np.mean(u_forward_euler[-1,:] - g(x_values)) < 0.0001)
