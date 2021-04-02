# Two-body problems, from the Gravitational Force to Two-body Scattering

## Introduction and Definitions

Central forces are forces which are directed towards or away from a
reference point. A familiar force is the gravitional
force  with the motion of our Earth around the Sun as a classic. The Sun, being
approximately sixth order of magnitude heavier than the Earth serves
as our origin. A force like the gravitational force is a function of the
relative distance $\boldsymbol{r}=\boldsymbol{r}_1-\boldsymbol{r}_2$ only, where 
$\boldsymbol{r}_1$ and $\boldsymbol{r}_2$ are the positions relative to a defined
origin for object one and object two, respectively.

These forces depend on the spatial degrees of freedom only (the
positions of the interacting objects/particles). As discussed earlier, from such forces we can infer
that  the total internal energy, the total linear momentum and total angular momentum are so-called constants of the motion, that is they stay constant  over time. We say that energy, linear and anuglar momentum are conserved.

With a scalar potential $V(\boldsymbol{r})$ we define the force as the gradient of the potential

$$
\boldsymbol{F}(\boldsymbol{r})=-\boldsymbol{\nabla}V(\boldsymbol{r}).
$$

In general these potentials depend only on the magnitude of the
relative position and we will write the potential as $V(r)$ where $r$
is defined as,

$$
r = |\boldsymbol{r}_1-\boldsymbol{r}_2|.
$$

In three dimensions our vectors are defined as (for a given object/particle $i$)

$$
\boldsymbol{r}_i = x_i\boldsymbol{e}_1+y_i\boldsymbol{e}_2+z_i\boldsymbol{e}_3,
$$

while in two dimensions we have

$$
\boldsymbol{r}_i = x_i\boldsymbol{e}_1+y_i\boldsymbol{e}_2.
$$

In two dimensions the radius $r$ is defined as

$$
r = |\boldsymbol{r}_1-\boldsymbol{r}_2|=\sqrt{(x_1-x_2)^2+(y_1-y_2)^2}.
$$

If we consider the gravitational potential involving two masses $1$ and $2$, we have

$$
V_{12}(r)=V(r)=-\frac{Gm_1m_2}{|\boldsymbol{r}_1-\boldsymbol{r}_2|}=-\frac{Gm_1m_2}{r}.
$$

Calculating the gradient of this potential we obtain the force

$$
\boldsymbol{F}(\boldsymbol{r})=-\frac{Gm_1m_2}{|\boldsymbol{r}_1-\boldsymbol{r}_1|^2}\hat{\boldsymbol{r}}_{12}=-\frac{Gm_am_b}{r^2}\hat{\boldsymbol{r}},
$$

where we have the unit vector

$$
\hat{\boldsymbol{r}}=\hat{\boldsymbol{r}}_{12}=\frac{\boldsymbol{r}_2-\boldsymbol{r}_1}{|\boldsymbol{r}_1-\boldsymbol{r}_2|}.
$$

Here $G=6.67\times 10^{-11}$ Nm$^2$/kg$^2$, and $\boldsymbol{F}$ is the force
on $2$ due to $1$. By inspection, one can see that the force on $2$
due to $1$ and the force on $1$ due to $2$ are equal and opposite. The
net potential energy for a large number of masses would be

$$
V=\sum_{i<j}V_{ij}=\frac{1}{2}\sum_{i\ne j}V_{ij}.
$$

In general, the central forces that we will study can be written mathematically as

$$
\boldsymbol{F}(\boldsymbol{r})=f(r)\hat{r},
$$

where $f(r)$ is  a scalar function. For the above gravitational force this scalar term is
$-Gm_1m_2/r^2$.
In general we will simply write this scalar function $f(r)=\alpha/r^2$ where $\alpha$ is a constant that can be either negative or positive. We will also see examples of other types of potentials in the examples below.

Besides general expressions for the potentials/forces, we will discuss
in detail different types of motion that arise, from circular to
elliptical or hyperbolic or parabolic. By transforming to either polar
coordinates or spherical coordinates, we will be able to obtain
analytical solutions for the equations of motion and thereby obtain
new insights about the properties of a system. Where possible, we will
compare our analytical equations with numerical studies.

However, before we arrive at these lovely insights, we need to
introduce some mathematical manipulations and definitions. We conclude
this chapter with a discussion of two-body scattering.


## Center of Mass and Relative Coordinates


Thus far, we have considered the trajectory as if the force is
centered around a fixed point. For two bodies interacting only with
one another, both masses circulate around the center of mass. One
might think that solutions would become more complex when both
particles move, but we will see here that the problem can be reduced
to one with a single body moving according to a fixed force by
expressing the trajectories for $\boldsymbol{r}_1$ and $\boldsymbol{r}_2$ into the
center-of-mass coordinate $\boldsymbol{R}$ and the relative
coordinate $\boldsymbol{r}$. We define the center-of-mass (CoM) coordinate as

$$
\boldsymbol{R}\equiv\frac{m_1\boldsymbol{r}_1+m_2\boldsymbol{r}_2}{m_1+m_2},
$$

and the relative coordinate as

$$
\boldsymbol{r}\equiv\boldsymbol{r}_1-\boldsymbol{r_2}.
$$

We can then rewrite $\boldsymbol{r}_1$ and $\boldsymbol{r}_2$ in terms of the relative and CoM coordinates as

$$
\boldsymbol{r}_1=\boldsymbol{R}+\frac{m_2}{M}\boldsymbol{r},
$$

and

$$
\boldsymbol{r}_2=\boldsymbol{R}-\frac{m_1}{M}\boldsymbol{r}.
$$

### Conservation of total  Linear Momentum

In our discussions on conservative forces we defined 
the total linear momentum as

$$
\boldsymbol{P}=\sum_{i=1}^Nm_i\frac{d\boldsymbol{r}_i}{dt},
$$

where $N=2$ in our case. With the above definition of the center of mass position, we see that we can rewrite the total linear momentum as (multiplying the CoM coordinate  with $M$)

$$
\boldsymbol{P}=M\frac{d\boldsymbol{R}}{dt}=M\dot{\boldsymbol{R}}.
$$

The net force acting on the system is given by the time derivative of the linear momentum (assuming mass is time independent)
and we have

$$
\boldsymbol{F}^{\mathrm{net}}=\dot{\boldsymbol{P}}=M\ddot{\boldsymbol{R}}.
$$

The net force acting on the system is given by the sum of the forces acting on the two bodies, that is we have

$$
\boldsymbol{F}^{\mathrm{net}}=\boldsymbol{F}_1+\boldsymbol{F}_2=\dot{\boldsymbol{P}}=M\ddot{\boldsymbol{R}}.
$$

In our case the forces are given by the internal forces only. The force acting on object $1$ is thus $\boldsymbol{F}_{12}$ and the one acting on object $2$ is $\boldsymbol{F}_{12}$. We have also defined that $\boldsymbol{F}_{12}=-\boldsymbol{F}_{21}$. This means thar we have

$$
\boldsymbol{F}_1+\boldsymbol{F}_2=\boldsymbol{F}_{12}+\boldsymbol{F}_{21}=0=\dot{\boldsymbol{P}}=M\ddot{\boldsymbol{R}}.
$$

We could alternatively had write this

$$
\ddot{\boldsymbol{R}}_{\rm cm}=\frac{1}{m_1+m_2}\left\{m_1\ddot{\boldsymbol{r}}_1+m_2\ddot{\boldsymbol{r}}_2\right\}=\frac{1}{m_1+m_2}\left\{\boldsymbol{F}_{12}+\boldsymbol{F}_{21}\right\}=0.
$$

This has the important consequence that the CoM velocity is a constant
of the motion. And since the total linear momentum is given by the
time-derivative of the CoM coordinate times the total mass
$M=m_1+m_2$, it means that linear momentum is also conserved.
Stated differently,  the center-of-mass coordinate
$\boldsymbol{R}$ moves at a fixed velocity.

This has also another important consequence for our forces. If we
assume that our force depends only on the relative coordinate, it
means that the gradient of the potential with respect to the center of
mass position is zero, that is

$$
M\ddot{d\boldsymbol{R}}=-\boldsymbol{\nabla}_{\boldsymbol{R}}V =0!
$$

If we now switch to the equation of motion for the relative coordinate, we have

$$
\ddot{\boldsymbol{r}}=\ddot{\boldsymbol{r}}_1-\ddot{\boldsymbol{r}}_2=\left(\frac{\boldsymbol{F}_{12}}{m_1}-\frac{\boldsymbol{F}_{21}}{m_2}\right)=\left(\frac{1}{m_1}+\frac{1}{m_2}\right)\boldsymbol{F}_{12},
$$

which we can rewrite in terms of the reduced mass

$$
\mu=\frac{m_1m_2}{m_1+m_2},
$$

as

$$
\mu \ddot{\boldsymbol{r}}=\boldsymbol{F}_{12}.
$$

This has a very important consequence for our coming analysis of the equations of motion for the two-body problem.
Since the acceleration for the CoM coordinate is zero, we can now
treat the trajectory as a one-body problem where the mass is given by 
the reduced mass $\mu$ plus a second trivial problem for the center of
mass. The reduced mass is especially convenient when one is
considering forces that depend only on the relative coordinate (like the Gravitational force or the electrostatic force between two charges)  because then for say the gravitational force we have

$$
\mu \ddot{\boldsymbol{r}}=-\frac{Gm_1m_2}{r^2}\hat{\boldsymbol{r}}=-\frac{GM\mu}{r^2}\hat{\boldsymbol{r}},
$$

where we have defined $M= m_1+m_2$.  It means that the acceleration of the relative coordinate is

$$
\ddot{\boldsymbol{r}}=-\frac{GM}{r^2}\hat{\boldsymbol{r}},
$$

and we have that for the gravitational problem, the reduced mass then falls out and the
trajectory depends only on the total mass $M$.

The standard strategy is to transform into the center of mass frame,
then treat the problem as one of a single particle of mass $\mu$
undergoing a force $\boldsymbol{F}_{12}$. Scattering angles, see our discussion of scattering problems below, can also be
expressed in this frame.  Before we proceed to our definition of the CoM frame we need to set up the expression for the energy in terms of the relative and CoM coordinates.


### Kinetic and total Energy

The kinetic energy and momenta also have analogues in center-of-mass
coordinates. 
We have defined the total linear momentum as

$$
\boldsymbol{P}=\sum_{i=1}^Nm_i\frac{d\boldsymbol{r}_i}{dt}=M\dot{\boldsymbol{R}}.
$$

For the relative momentum $\boldsymbol{q}$, we have that the time derivative of $\boldsymbol{r}$ is

$$
\dot{\boldsymbol{r}} =\dot{\boldsymbol{r}}_1-\dot{\boldsymbol{r}}_2,
$$

We know also that the momenta $\boldsymbol{p}_1=m_1\dot{\boldsymbol{r}}_1$ and
$\boldsymbol{p}_2=m_2\dot{\boldsymbol{r}}_2$. Using these expressions we can rewrite

$$
\dot{\boldsymbol{r}} =\frac{\boldsymbol{p}_1}{m_1}-\frac{\boldsymbol{p}_2}{m_2},
$$

which gives

$$
\dot{\boldsymbol{r}} =\frac{m_2\boldsymbol{p}_1-m_1\boldsymbol{p}_2}{m_1m_2},
$$

and dividing both sides with $M$ we have

$$
\frac{m_1m_2}{M}\dot{\boldsymbol{r}} =\frac{m_2\boldsymbol{p}_1-m_1\boldsymbol{p}_2}{M}.
$$

Introducing the reduced mass $\mu=m_1m_2/M$ we have finally

$$
\mu\dot{\boldsymbol{r}} =\frac{m_2\boldsymbol{p}_1-m_1\boldsymbol{p}_2}{M}.
$$

And $\mu\dot{\boldsymbol{r}}$ defines the relative momentum $\boldsymbol{q}=\mu\dot{\boldsymbol{r}}$. 

With these definitions we can then calculate the kinetic energy in terms of the relative and CoM coordinates.

We have that

$$
K=\frac{p_1^2}{2m_1}+\frac{p_2^2}{2m_2},
$$

and with $\boldsymbol{p}_1=m_1\dot{\boldsymbol{r}}_1$ and $\boldsymbol{p}_2=m_2\dot{\boldsymbol{r}}_2$ and using

$$
\dot{\boldsymbol{r}}_1=\dot{\boldsymbol{R}}+\frac{m_2}{M}\dot{\boldsymbol{r}},
$$

and

$$
\dot{\boldsymbol{r}}_2=\dot{\boldsymbol{R}}-\frac{m_1}{M}\dot{\boldsymbol{r}},
$$

we obtain after squaring the expressions for $\dot{\boldsymbol{r}}_1$ and $\dot{\boldsymbol{r}}_2$

$$
K=\frac{(m_1+m_2)\dot{\boldsymbol{R}}^2}{2}+\frac{(m_1+m_2)m_1m_2\dot{\boldsymbol{r}}^2}{2M^2},
$$

which we simplify to

$$
K=\frac{\dot{\boldsymbol{P}}^2}{2M}+\frac{\mu\dot{\boldsymbol{q}}^2}{2}.
$$

Below we will define a reference frame, the so-called CoM-frame, where
$\boldsymbol{R}=0$. This is going to simplify our equations further.


### Conservation of Angular Momentum

The angular momentum (the total one) is the sum of the individual angular momenta. In our case we have two bodies only, meaning that our angular momentum is defined as

$$
\boldsymbol{L} = \boldsymbol{r}_1 \times \boldsymbol{p}_1+\boldsymbol{r}_2 \times \boldsymbol{p}_2,
$$

and using that $m_1\dot{\boldsymbol{r}}_1=\boldsymbol{p}_1$ and $m_2\dot{\boldsymbol{r}}_2=\boldsymbol{p}_2$ we have

$$
\boldsymbol{L} = m_1\boldsymbol{r}_1 \times \dot{\boldsymbol{r}}_1+m_2\boldsymbol{r}_2 \times \dot{\boldsymbol{r}}_2.
$$

We define now the CoM-Frame where we set $\boldsymbol{R}=0$. This means that the equations 
for $\boldsymbol{r}_1$ and $\boldsymbol{r}_2$ in terms of the relative motion simplify and  we have

$$
\boldsymbol{r}_1=\frac{m_2}{M}\boldsymbol{r},
$$

and

$$
\boldsymbol{r}_2=-\frac{m_1}{M}\boldsymbol{r}.
$$

resulting in

$$
\boldsymbol{L} = m_1 \frac{m_2}{M}\boldsymbol{r}\times\frac{m_2}{M}\boldsymbol{r} +m_2 \frac{m_1}{M}\boldsymbol{r} \times \frac{m_1}{M}\dot{\boldsymbol{r}}.
$$

We see that can rewrite this equation as

$$
\boldsymbol{L}=\boldsymbol{r}\times \mu\dot{\boldsymbol{r}}=\mu\boldsymbol{r}\times \dot{\boldsymbol{r}}.
$$

If we now use a central force, we have that

$$
\mu\dot{\boldsymbol{r}}=\boldsymbol{F}(\boldsymbol{r})=f(r)\hat{\boldsymbol{r}},
$$

and inserting this in the equation for the angular momentum we have

$$
\boldsymbol{L}=\boldsymbol{r}\times f(r)\hat{\boldsymbol{r}},
$$

which equals zero since we are taking the cross product of the vector
$\boldsymbol{r}$ with itself.  Angular momentum is thus conserved and in
addition to the total linear momentum being conserved, we know that
energy is also conserved with forces that depend only on position and
the relative coordinate only.

Since angular momentum is conserved, we can idealize
the motion of our two objects as two bodies moving in a plane spanned by the
relative coordinate and the relative momentum. The angular
momentum is perpendicular to the plane spanned by these two vectors.


It means also, since $\boldsymbol{L}$ is conserved, that we can reduce our
problem to a motion in say the $xy$-plane.  What we have done then is to
reduce a two-body problem in three-dimensions with six degrees of
freedom (the six coordinates of the two objects) to a problem defined
entirely by the relative coordinate in two dimensions.  We have thus
moved from a problem with six degrees of freedom to one with two degrees of freedom only.

Since we deal with central forces that depend only on the
relative coordinate, we will show below that transforming to polar
coordinates, we cna find analytical solution to
the equation of motion

$$
\mu\dot{\boldsymbol{r}}=\boldsymbol{F}(\boldsymbol{r})=f(r)\hat{\boldsymbol{r}}.
$$

Note the boldfaced symbols for the relative position $\boldsymbol{r}$. Our vector $\boldsymbol{r}$ is defined as

$$
\boldsymbol{r}=x\boldsymbol{e}_1+y\boldsymbol{e}_2
$$

and introducing polar coordinates $r\in[0,\infty)$ and $\phi\in [0,2\pi]$ and the transformation

$$
r=\sqrt{x^2+y^2},
$$

and $x=r\cos\phi$ and $y=r\sin\phi$, we will rewrite our equation of motion by transforming from Cartesian coordinates to Polar coordinates. By so doing, we end up with two differential equations which can be solved analytically (it depends on the form of the potential).

What follows now is a rewrite of these equations and the introduction of Kepler's laws as well.

## Deriving Elliptical Orbits

Kepler's laws state that a gravitational orbit should be an ellipse
with the source of the gravitational field at one focus. Deriving this
is surprisingly messy. To do this, we first use angular momentum
conservation to transform the equations of motion so that it is in
terms of $r$ and $\phi$ instead of $r$ and $t$. The overall strategy
is to


1. Find equations of motion for $r$ and $t$ with no angle ($\phi$) mentioned, i.e. $d^2r/dt^2=\cdots$. Angular momentum conservation will be used, and the equation will involve the angular momentum $L$.

2. Use angular momentum conservation to find an expression for $\dot{\phi}$ in terms of $r$.

3. Use the chain rule to convert the equations of motions for $r$, an expression involving $r,\dot{r}$ and $\ddot{r}$, to one involving $r,dr/d\phi$ and $d^2r/d\phi^2$. This is quitecomplicated because the expressions will also involve a substitution $u=1/r$ so that one finds an expression in terms of $u$ and $\phi$.

4. Once $u(\phi)$ is found, you need to show that this can be converted to the familiar form for an ellipse.

We will now rewrite the above equation of motion (note the boldfaced vector $\boldsymbol{r}$)

$$
\mu \ddot{\boldsymbol{r}}=\boldsymbol{F}(\boldsymbol{r}),
$$

in polar coordinates.
What follows here is a repeated application of the chain rule for derivatives.
We start with derivative for $r$ as function of time in a cartesian basis

<!-- Equation labels as ordinary links -->
<div id="eq:radialeqofmotion"></div>

$$
\begin{eqnarray}
\label{eq:radialeqofmotion} \tag{1}
\frac{d}{dt}r^2&=&\frac{d}{dt}(x^2+y^2)=2x\dot{x}+2y\dot{y}=2r\dot{r},\\
\nonumber
\dot{r}&=&\frac{x}{r}\dot{x}+\frac{y}{r}\dot{y},\\
\nonumber
\ddot{r}&=&\frac{x}{r}\ddot{x}+\frac{y}{r}\ddot{y}
+\frac{\dot{x}^2+\dot{y}^2}{r}
-\frac{\dot{r}^2}{r}.
\end{eqnarray}
$$

Note that there are no vectors involved here.

Recognizing that the numerator of the third term is the velocity squared, and that it can be written in polar coordinates,

<!-- Equation labels as ordinary links -->
<div id="_auto1"></div>

$$
\begin{equation}
v^2=\dot{x}^2+\dot{y}^2=\dot{r}^2+r^2\dot{\phi}^2,
\label{_auto1} \tag{2}
\end{equation}
$$

one can write $\ddot{r}$ as

<!-- Equation labels as ordinary links -->
<div id="eq:radialeqofmotion2"></div>

$$
\begin{equation}
\label{eq:radialeqofmotion2} \tag{3}
\ddot{r}=\frac{F_x\cos\phi+F_y\sin\phi}{m}+\frac{\dot{r}^2+r^2\dot{\phi}^2}{r}-\frac{\dot{r}^2}{r}
\end{equation}
$$

$$
\nonumber
=\frac{F}{m}+\frac{r^2\dot{\phi}^2}{r}
$$

<!-- Equation labels as ordinary links -->
<div id="_auto2"></div>

$$
\begin{equation} 
\label{_auto2} \tag{4}
\end{equation}
$$

or

$$
m\ddot{r}=F+\frac{L^2}{mr^3}.
$$

This derivation used the fact that the force was radial,
$F=F_r=F_x\cos\phi+F_y\sin\phi$, and that angular momentum is
$L=mrv_{\phi}=mr^2\dot{\phi}$. The term $L^2/mr^3=mv^2/r$ behaves
like an additional force. Sometimes this is referred to as a
centrifugal force, but it is not a force. Instead, it is the
consequence of considering the motion in a rotating (and therefore
accelerating) frame.

Now, we switch to the particular case of an attractive inverse square
force, $F=-\alpha/r^2$, and show that the trajectory, $r(\phi)$, is
an ellipse. To do this we transform derivatives w.r.t. time to
derivatives w.r.t. $\phi$ using the chain rule combined with angular
momentum conservation, $\dot{\phi}=L/mr^2$.

<!-- Equation labels as ordinary links -->
<div id="eq:rtotheta"></div>

$$
\begin{eqnarray}
\label{eq:rtotheta} \tag{5}
\dot{r}&=&\frac{dr}{d\phi}\dot{\phi}=\frac{dr}{d\phi}\frac{L}{mr^2},\\
\nonumber
\ddot{r}&=&\frac{d^2r}{d\phi^2}\dot{\phi}^2
+\frac{dr}{d\phi}\left(\frac{d}{dr}\frac{L}{mr^2}\right)\dot{r}\\
\nonumber
&=&\frac{d^2r}{d\phi^2}\left(\frac{L}{mr^2}\right)^2
-2\frac{dr}{d\phi}\frac{L}{mr^3}\dot{r}\\
\nonumber
&=&\frac{d^2r}{d\phi^2}\left(\frac{L}{mr^2}\right)^2
-\frac{2}{r}\left(\frac{dr}{d\phi}\right)^2\left(\frac{L}{mr^2}\right)^2
\end{eqnarray}
$$

Equating the two expressions for $\ddot{r}$ in Eq.s ([3](#eq:radialeqofmotion2)) and ([5](#eq:rtotheta)) eliminates all the derivatives w.r.t. time, and provides a differential equation with only derivatives w.r.t. $\phi$,

<!-- Equation labels as ordinary links -->
<div id="eq:rdotdot"></div>

$$
\begin{equation}
\label{eq:rdotdot} \tag{6}
\frac{d^2r}{d\phi^2}\left(\frac{L}{mr^2}\right)^2
-\frac{2}{r}\left(\frac{dr}{d\phi}\right)^2\left(\frac{L}{mr^2}\right)^2
=\frac{F}{m}+\frac{L^2}{m^2r^3},
\end{equation}
$$

that when solved yields the trajectory, i.e. $r(\phi)$. Up to this
point the expressions work for any radial force, not just forces that
fall as $1/r^2$.

The trick to simplifying this differential equation for the inverse
square problems is to make a substitution, $u\equiv 1/r$, and rewrite
the differential equation for $u(\phi)$.

$$
\begin{eqnarray}
r&=&1/u,\\
\nonumber
\frac{dr}{d\phi}&=&-\frac{1}{u^2}\frac{du}{d\phi},\\
\nonumber
\frac{d^2r}{d\phi^2}&=&\frac{2}{u^3}\left(\frac{du}{d\phi}\right)^2-\frac{1}{u^2}\frac{d^2u}{d\phi^2}.
\end{eqnarray}
$$

Plugging these expressions into Eq. ([6](#eq:rdotdot)) gives an
expression in terms of $u$, $du/d\phi$, and $d^2u/d\phi^2$. After
some tedious algebra,

<!-- Equation labels as ordinary links -->
<div id="_auto3"></div>

$$
\begin{equation}
\frac{d^2u}{d\phi^2}=-u-\frac{F m}{L^2u^2}.
\label{_auto3} \tag{7}
\end{equation}
$$

For the attractive inverse square law force, $F=-\alpha u^2$,

<!-- Equation labels as ordinary links -->
<div id="_auto4"></div>

$$
\begin{equation}
\frac{d^2u}{d\phi^2}=-u+\frac{m\alpha}{L^2}.
\label{_auto4} \tag{8}
\end{equation}
$$

The solution has two arbitrary constants, $A$ and $\phi_0$,

<!-- Equation labels as ordinary links -->
<div id="eq:Ctrajectory"></div>

$$
\begin{eqnarray}
\label{eq:Ctrajectory} \tag{9}
u&=&\frac{m\alpha}{L^2}+A\cos(\phi-\phi_0),\\
\nonumber
r&=&\frac{1}{(m\alpha/L^2)+A\cos(\phi-\phi_0)}.
\end{eqnarray}
$$

The radius will be at a minimum when $\phi=\phi_0$ and at a
maximum when $\phi=\phi_0+\pi$. The constant $A$ is related to the
eccentricity of the orbit. When $A=0$ the radius is a constant
$r=L^2/(m\alpha)$, and the motion is circular. If one solved the
expression $mv^2/r=-\alpha/r^2$ for a circular orbit, using the
substitution $v=L/(mr)$, one would reproduce the expression
$r=L^2/(m\alpha)$.

The form describing the elliptical trajectory in
Eq. ([9](#eq:Ctrajectory)) can be identified as an ellipse with one
focus being the center of the ellipse by considering the definition of
an ellipse as being the points such that the sum of the two distances
between the two foci are a constant. Making that distance $2D$, the
distance between the two foci as $2a$, and putting one focus at the
origin,

$$
\begin{eqnarray}
2D&=&r+\sqrt{(r\cos\phi-2a)^2+r^2\sin^2\phi},\\
\nonumber
4D^2+r^2-4Dr&=&r^2+4a^2-4ar\cos\phi,\\
\nonumber
r&=&\frac{D^2-a^2}{D+a\cos\phi}=\frac{1}{D/(D^2-a^2)-a\cos\phi/(D^2-a^2)}.
\end{eqnarray}
$$

By inspection, this is the same form as Eq. ([9](#eq:Ctrajectory)) with $D/(D^2-a^2)=m\alpha/L^2$ and $a/(D^2-a^2)=A$.


Let us remind ourselves about what an ellipse is before we proceed.

%matplotlib inline

import numpy as np
from matplotlib import pyplot as plt
from math import pi

u=1.     #x-position of the center
v=0.5    #y-position of the center
a=2.     #radius on the x-axis
b=1.5    #radius on the y-axis

t = np.linspace(0, 2*pi, 100)
plt.plot( u+a*np.cos(t) , v+b*np.sin(t) )
plt.grid(color='lightgray',linestyle='--')
plt.show()

## Effective or Centrifugal Potential

The total energy of a particle is

$$
\begin{eqnarray}
E&=&V(r)+\frac{1}{2}mv_\phi^2+\frac{1}{2}m\dot{r}^2\\
\nonumber
&=&V(r)+\frac{1}{2}mr^2\dot{\phi}^2+\frac{1}{2}m\dot{r}^2\\
\nonumber
&=&V(r)+\frac{L^2}{2mr^2}+\frac{1}{2}m\dot{r}^2.
\end{eqnarray}
$$

The second term then contributes to the energy like an additional
repulsive potential. The term is sometimes referred to as the
"centrifugal" potential, even though it is actually the kinetic energy
of the angular motion. Combined with $V(r)$, it is sometimes referred
to as the "effective" potential,

$$
\begin{eqnarray}
V_{\rm eff}(r)&=&V(r)+\frac{L^2}{2mr^2}.
\end{eqnarray}
$$

Note that if one treats the effective potential like a real potential, one would expect to be able to generate an effective force,

$$
\begin{eqnarray}
F_{\rm eff}&=&-\frac{d}{dr}V(r) -\frac{d}{dr}\frac{L^2}{2mr^2}\\
\nonumber
&=&F(r)+\frac{L^2}{mr^3}=F(r)+m\frac{v_\perp^2}{r},
\end{eqnarray}
$$

which is indeed matches the form for $m\ddot{r}$ in Eq. ([3](#eq:radialeqofmotion2)), which included the **centrifugal** force.

The following code plots this effective potential for a simple choice of parameters, with a standard gravitational potential $-\alpha/r$. Here we have chosen $L=m=\alpha=1$.

# Common imports
import numpy as np
from math import *
import matplotlib.pyplot as plt

Deltax = 0.01
#set up arrays
xinitial = 0.3
xfinal = 5.0
alpha = 1.0   # spring constant
m = 1.0   # mass, you can change these
AngMom = 1.0  #  The angular momentum
n = ceil((xfinal-xinitial)/Deltax)
x = np.zeros(n)
for i in range(n):
    x[i] = xinitial+i*Deltax
V = np.zeros(n)
V = -alpha/x+0.5*AngMom*AngMom/(m*x*x)
# Plot potential
fig, ax = plt.subplots()
ax.set_xlabel('r[m]')
ax.set_ylabel('V[J]')
ax.plot(x, V)
fig.tight_layout()
plt.show()

### Gravitational force example

Using the above parameters, we can now study the evolution of the system using for example the velocity Verlet method.
This is done in the code here for an initial radius equal to the minimum of the potential well.  We seen then that the radius is always the same and corresponds to a circle (the radius is always constant).

# Common imports
import numpy as np
import pandas as pd
from math import *
import matplotlib.pyplot as plt
import os

# Where to save the figures and data files
PROJECT_ROOT_DIR = "Results"
FIGURE_ID = "Results/FigureFiles"
DATA_ID = "DataFiles/"

if not os.path.exists(PROJECT_ROOT_DIR):
    os.mkdir(PROJECT_ROOT_DIR)

if not os.path.exists(FIGURE_ID):
    os.makedirs(FIGURE_ID)

if not os.path.exists(DATA_ID):
    os.makedirs(DATA_ID)

def image_path(fig_id):
    return os.path.join(FIGURE_ID, fig_id)

def data_path(dat_id):
    return os.path.join(DATA_ID, dat_id)

def save_fig(fig_id):
    plt.savefig(image_path(fig_id) + ".png", format='png')


# Simple Gravitational Force   -alpha/r
    
DeltaT = 0.01
#set up arrays 
tfinal = 100.0
n = ceil(tfinal/DeltaT)
# set up arrays for t, v and r
t = np.zeros(n)
v = np.zeros(n)
r = np.zeros(n)
# Constants of the model, setting all variables to one for simplicity
alpha = 1.0
AngMom = 1.0  #  The angular momentum
m = 1.0  # scale mass to one
c1 = AngMom*AngMom/(m*m)
c2 = AngMom*AngMom/m
rmin = (AngMom*AngMom/m/alpha)
# Initial conditions
r0 = rmin
v0 = 0.0
r[0] = r0
v[0] = v0
# Start integrating using the Velocity-Verlet  method
for i in range(n-1):
    # Set up acceleration
    a = -alpha/(r[i]**2)+c1/(r[i]**3)
    # update velocity, time and position using the Velocity-Verlet method
    r[i+1] = r[i] + DeltaT*v[i]+0.5*(DeltaT**2)*a
    anew = -alpha/(r[i+1]**2)+c1/(r[i+1]**3)
    v[i+1] = v[i] + 0.5*DeltaT*(a+anew)
    t[i+1] = t[i] + DeltaT
    # Plot position as function of time
fig, ax = plt.subplots(2,1)
ax[0].set_xlabel('time')
ax[0].set_ylabel('radius')
ax[0].plot(t,r)
ax[1].set_xlabel('time')
ax[1].set_ylabel('Velocity')
ax[1].plot(t,v)
save_fig("RadialGVV")
plt.show()

Changing the value of the initial position to a value where the energy is positive, leads to an increasing radius with time, a so-called unbound orbit. Choosing on the other hand an initial radius that corresponds to a negative energy and different from the minimum value leads to a radius that oscillates back and forth between two values. 

### Harmonic Oscillator in two dimensions

Consider a particle of mass $m$ in a 2-dimensional harmonic oscillator with potential

$$
V=\frac{1}{2}kr^2=\frac{1}{2}k(x^2+y^2).
$$

If the orbit has angular momentum $L$, we can find the radius and angular velocity of the circular orbit as well as the b) the angular frequency of small radial perturbations.

We consider the effective potential. The radius of a circular orbit is at the minimum of the potential (where the effective force is zero).
The potential is plotted here with the parameters $k=m=0.1$ and $L=1.0$.

# Common imports
import numpy as np
from math import *
import matplotlib.pyplot as plt

Deltax = 0.01
#set up arrays
xinitial = 0.5
xfinal = 3.0
k = 1.0   # spring constant
m = 1.0   # mass, you can change these
AngMom = 1.0  #  The angular momentum
n = ceil((xfinal-xinitial)/Deltax)
x = np.zeros(n)
for i in range(n):
    x[i] = xinitial+i*Deltax
V = np.zeros(n)
V = 0.5*k*x*x+0.5*AngMom*AngMom/(m*x*x)
# Plot potential
fig, ax = plt.subplots()
ax.set_xlabel('r[m]')
ax.set_ylabel('V[J]')
ax.plot(x, V)
fig.tight_layout()
plt.show()

$$
\begin{eqnarray*}
V_{\rm eff}&=&\frac{1}{2}kr^2+\frac{L^2}{2mr^2}
\end{eqnarray*}
$$

The effective potential looks like that of a harmonic oscillator for
large $r$, but for small $r$, the centrifugal potential repels the
particle from the origin. The combination of the two potentials has a
minimum for at some radius $r_{\rm min}$.

$$
\begin{eqnarray*}
0&=&kr_{\rm min}-\frac{L^2}{mr_{\rm min}^3},\\
r_{\rm min}&=&\left(\frac{L^2}{mk}\right)^{1/4},\\
\dot{\phi}&=&\frac{L}{mr_{\rm min}^2}=\sqrt{k/m}.
\end{eqnarray*}
$$

For particles at $r_{\rm min}$ with $\dot{r}=0$, the particle does not
accelerate and $r$ stays constant, i.e. a circular orbit. The radius
of the circular orbit can be adjusted by changing the angular momentum
$L$.

For the above parameters this minimum is at $r_{\rm min}=1$.

 Now consider small vibrations about $r_{\rm min}$. The effective spring constant is the curvature of the effective potential.

$$
\begin{eqnarray*}
k_{\rm eff}&=&\left.\frac{d^2}{dr^2}V_{\rm eff}(r)\right|_{r=r_{\rm min}}=k+\frac{3L^2}{mr_{\rm min}^4}\\
&=&4k,\\
\omega&=&\sqrt{k_{\rm eff}/m}=2\sqrt{k/m}=2\dot{\phi}.
\end{eqnarray*}
$$

Here, the second step used the result of the last step from part
(a). Because the radius oscillates with twice the angular frequency,
the orbit has two places where $r$ reaches a minimum in one
cycle. This differs from the inverse-square force where there is one
minimum in an orbit. One can show that the orbit for the harmonic
oscillator is also elliptical, but in this case the center of the
potential is at the center of the ellipse, not at one of the foci.

The solution is also simple to write down exactly in Cartesian coordinates. The $x$ and $y$ equations of motion separate,

$$
\begin{eqnarray*}
\ddot{x}&=&-kx,\\
\ddot{y}&=&-ky.
\end{eqnarray*}
$$

So the general solution can be expressed as

$$
\begin{eqnarray*}
x&=&A\cos\omega_0 t+B\sin\omega_0 t,\\
y&=&C\cos\omega_0 t+D\sin\omega_0 t.
\end{eqnarray*}
$$

The code here finds the solution for $x$ and $y$ using the code we developed in homework 5 and 6 and the midterm.  Note that this code is tailored to run in Cartesian coordinates. There is thus no angular momentum dependent term.


DeltaT = 0.01
#set up arrays 
tfinal = 10.0
n = ceil(tfinal/DeltaT)
# set up arrays
t = np.zeros(n)
v = np.zeros((n,2))
r = np.zeros((n,2))
radius = np.zeros(n)
# Constants of the model
k = 1.0   # spring constant
m = 1.0   # mass, you can change these
omega02 = sqrt(k/m)  # Frequency
AngMom = 1.0  #  The angular momentum
rmin = (AngMom*AngMom/k/m)**0.25
# Initial conditions as compact 2-dimensional arrays
x0 = rmin-0.5; y0= sqrt(rmin*rmin-x0*x0)
r0 = np.array([x0,y0]) 
v0 = np.array([0.0,0.0])
r[0] = r0
v[0] = v0
# Start integrating using the Velocity-Verlet  method
for i in range(n-1):
    # Set up the acceleration
    a =  -r[i]*omega02  
    # update velocity, time and position using the Velocity-Verlet method
    r[i+1] = r[i] + DeltaT*v[i]+0.5*(DeltaT**2)*a
    anew = -r[i+1]*omega02  
    v[i+1] = v[i] + 0.5*DeltaT*(a+anew)
    t[i+1] = t[i] + DeltaT
# Plot position as function of time
radius = np.sqrt(r[:,0]**2+r[:,1]**2)
fig, ax = plt.subplots(3,1)
ax[0].set_xlabel('time')
ax[0].set_ylabel('radius squared')
ax[0].plot(t,r[:,0]**2+r[:,1]**2)
ax[1].set_xlabel('time')
ax[1].set_ylabel('x position')
ax[1].plot(t,r[:,0])
ax[2].set_xlabel('time')
ax[2].set_ylabel('y position')
ax[2].plot(t,r[:,1])

fig.tight_layout()
save_fig("2DimHOVV")
plt.show()

With some work using double angle formulas, one can calculate

$$
\begin{eqnarray*}
r^2&=&x^2+y^2\\
\nonumber
&=&(A^2+C^2)\cos^2(\omega_0t)+(B^2+D^2)\sin^2\omega_0t+(AB+CD)\cos(\omega_0t)\sin(\omega_0t)\\
\nonumber
&=&\alpha+\beta\cos 2\omega_0 t+\gamma\sin 2\omega_0 t,\\
\alpha&=&\frac{A^2+B^2+C^2+D^2}{2},~~\beta=\frac{A^2-B^2+C^2-D^2}{2},~~\gamma=AB+CD,\\
r^2&=&\alpha+(\beta^2+\gamma^2)^{1/2}\cos(2\omega_0 t-\delta),~~~\delta=\arctan(\gamma/\beta),
\end{eqnarray*}
$$

and see that radius oscillates with frequency $2\omega_0$. The
factor of two comes because the oscillation $x=A\cos\omega_0t$ has two
maxima for $x^2$, one at $t=0$ and one a half period later.

The following code shows first how we can solve this problem using the radial degrees of freedom only.

DeltaT = 0.01
#set up arrays 
tfinal = 10.0
n = ceil(tfinal/DeltaT)
# set up arrays for t, v and r
t = np.zeros(n)
v = np.zeros(n)
r = np.zeros(n)
E = np.zeros(n)
# Constants of the model
AngMom = 1.0  #  The angular momentum
m = 1.0
k = 1.0
omega02 = k/m
c1 = AngMom*AngMom/(m*m)
c2 = AngMom*AngMom/m
rmin = (AngMom*AngMom/k/m)**0.25
# Initial conditions
r0 = rmin
v0 = 0.0
r[0] = r0
v[0] = v0
E[0] = 0.5*m*v0*v0+0.5*k*r0*r0+0.5*c2/(r0*r0)
# Start integrating using the Velocity-Verlet  method
for i in range(n-1):
    # Set up acceleration
    a = -r[i]*omega02+c1/(r[i]**3)    
    # update velocity, time and position using the Velocity-Verlet method
    r[i+1] = r[i] + DeltaT*v[i]+0.5*(DeltaT**2)*a
    anew = -r[i+1]*omega02+c1/(r[i+1]**3)
    v[i+1] = v[i] + 0.5*DeltaT*(a+anew)
    t[i+1] = t[i] + DeltaT
    E[i+1] = 0.5*m*v[i+1]*v[i+1]+0.5*k*r[i+1]*r[i+1]+0.5*c2/(r[i+1]*r[i+1])
    # Plot position as function of time
fig, ax = plt.subplots(2,1)
ax[0].set_xlabel('time')
ax[0].set_ylabel('radius')
ax[0].plot(t,r)
ax[1].set_xlabel('time')
ax[1].set_ylabel('Energy')
ax[1].plot(t,E)
save_fig("RadialHOVV")
plt.show()

## Stability of Orbits

The effective force can be extracted from the effective potential, $V_{\rm eff}$. Beginning from the equations of motion, Eq. ([1](#eq:radialeqofmotion)), for $r$,

$$
\begin{eqnarray}
m\ddot{r}&=&F+\frac{L^2}{mr^3}\\
\nonumber
&=&F_{\rm eff}\\
\nonumber
&=&-\partial_rV_{\rm eff},\\
\nonumber
F_{\rm eff}&=&-\partial_r\left[V(r)+(L^2/2mr^2)\right].
\end{eqnarray}
$$

For a circular orbit, the radius must be fixed as a function of time,
so one must be at a maximum or a minimum of the effective
potential. However, if one is at a maximum of the effective potential
the radius will be unstable. For the attractive Coulomb force the
effective potential will be dominated by the $-\alpha/r$ term for
large $r$ because the centrifugal part falls off more quickly, $\sim
1/r^2$. At low $r$ the centrifugal piece wins and the effective
potential is repulsive. Thus, the potential must have a minimum
somewhere with negative potential. The circular orbits are then stable
to perturbation.


The effective potential is sketched for two cases, a $1/r$ attractive
potential and a $1/r^3$ attractive potential. The $1/r$ case has a
stable minimum, whereas the circular orbit in the $1/r^3$ case is
unstable.


If one considers a potential that falls as $1/r^3$, the situation is
reversed and the point where $\partial_rV$ disappears will be a local
maximum rather than a local minimum. **Fig to come here with code**

The repulsive centrifugal piece dominates at large $r$ and the attractive
Coulomb piece wins out at small $r$. The circular orbit is then at a
maximum of the effective potential and the orbits are unstable. It is
the clear that for potentials that fall as $r^n$, that one must have
$n>-2$ for the orbits to be stable.


Consider a potential $V(r)=\beta r$. For a particle of mass $m$ with
angular momentum $L$, find the angular frequency of a circular
orbit. Then find the angular frequency for small radial perturbations.


For the circular orbit you search for the position $r_{\rm min}$ where the effective potential is minimized,

$$
\begin{eqnarray*}
\partial_r\left\{\beta r+\frac{L^2}{2mr^2}\right\}&=&0,\\
\beta&=&\frac{L^2}{mr_{\rm min}^3},\\
r_{\rm min}&=&\left(\frac{L^2}{\beta m}\right)^{1/3},\\
\dot{\phi}&=&\frac{L}{mr_{\rm min}^2}=\frac{\beta^{2/3}}{(mL)^{1/3}}
\end{eqnarray*}
$$

Now, we can find the angular frequency of small perturbations about the circular orbit. To do this we find the effective spring constant for the effective potential,

$$
\begin{eqnarray*}
k_{\rm eff}&=&\partial_r^2 \left.V_{\rm eff}\right|_{r_{\rm min}}\\
&=&\frac{3L^2}{mr_{\rm min}^4},\\
\omega&=&\sqrt{\frac{k_{\rm eff}}{m}}\\
&=&\frac{\beta^{2/3}}{(mL)^{1/3}}\sqrt{3}.
\end{eqnarray*}
$$

If the two frequencies, $\dot{\phi}$ and $\omega$, differ by an
integer factor, the orbit's trajectory will repeat itself each time
around. This is the case for the inverse-square force,
$\omega=\dot{\phi}$, and for the harmonic oscillator,
$\omega=2\dot{\phi}$. In this case, $\omega=\sqrt{3}\dot{\phi}$,
and the angles at which the maxima and minima occur change with each
orbit.


### Code example with gravitional force

The code example here is meant to illustrate how we can make a plot of the final orbit. We solve the equations in polar coordinates (the example here uses the minimum of the potential as initial value) and then we transform back to cartesian coordinates and plot $x$ versus $y$. We see that we get a perfect circle when we place ourselves at the minimum of the potential energy, as expected.


# Simple Gravitational Force   -alpha/r
    
DeltaT = 0.01
#set up arrays 
tfinal = 8.0
n = ceil(tfinal/DeltaT)
# set up arrays for t, v and r
t = np.zeros(n)
v = np.zeros(n)
r = np.zeros(n)
phi = np.zeros(n)
x = np.zeros(n)
y = np.zeros(n)
# Constants of the model, setting all variables to one for simplicity
alpha = 1.0
AngMom = 1.0  #  The angular momentum
m = 1.0  # scale mass to one
c1 = AngMom*AngMom/(m*m)
c2 = AngMom*AngMom/m
rmin = (AngMom*AngMom/m/alpha)
# Initial conditions, place yourself at the potential min
r0 = rmin
v0 = 0.0  # starts at rest
r[0] = r0
v[0] = v0
phi[0] = 0.0
# Start integrating using the Velocity-Verlet  method
for i in range(n-1):
    # Set up acceleration
    a = -alpha/(r[i]**2)+c1/(r[i]**3)
    # update velocity, time and position using the Velocity-Verlet method
    r[i+1] = r[i] + DeltaT*v[i]+0.5*(DeltaT**2)*a
    anew = -alpha/(r[i+1]**2)+c1/(r[i+1]**3)
    v[i+1] = v[i] + 0.5*DeltaT*(a+anew)
    t[i+1] = t[i] + DeltaT
    phi[i+1] = t[i+1]*c2/(r0**2)
# Find cartesian coordinates for easy plot    
x = r*np.cos(phi)
y = r*np.sin(phi)
fig, ax = plt.subplots(3,1)
ax[0].set_xlabel('time')
ax[0].set_ylabel('radius')
ax[0].plot(t,r)
ax[1].set_xlabel('time')
ax[1].set_ylabel('Angle $\cos{\phi}$')
ax[1].plot(t,np.cos(phi))
ax[2].set_ylabel('y')
ax[2].set_xlabel('x')
ax[2].plot(x,y)

save_fig("Phasespace")
plt.show()

Try to change the initial value for $r$ and see what kind of orbits you get.
In order to test different energies, it can be useful to look at the plot of the effective potential discussed above.

However, for orbits different from a circle the above code would need modifications in order to allow us to display say an ellipse. For the latter, it is much easier to run our code in cartesian coordinates, as done here. In this code we test also energy conservation and see that it is conserved to numerical precision. The code here is a simple extension of the code we developed for homework 4.

# Common imports
import numpy as np
import pandas as pd
from math import *
import matplotlib.pyplot as plt

DeltaT = 0.01
#set up arrays 
tfinal = 10.0
n = ceil(tfinal/DeltaT)
# set up arrays
t = np.zeros(n)
v = np.zeros((n,2))
r = np.zeros((n,2))
E = np.zeros(n)
# Constants of the model
m = 1.0   # mass, you can change these
alpha = 1.0
# Initial conditions as compact 2-dimensional arrays
x0 = 0.5; y0= 0.
r0 = np.array([x0,y0]) 
v0 = np.array([0.0,1.0])
r[0] = r0
v[0] = v0
rabs = sqrt(sum(r[0]*r[0]))
E[0] = 0.5*m*(v[0,0]**2+v[0,1]**2)-alpha/rabs
# Start integrating using the Velocity-Verlet  method
for i in range(n-1):
    # Set up the acceleration
    rabs = sqrt(sum(r[i]*r[i]))
    a =  -alpha*r[i]/(rabs**3)
    # update velocity, time and position using the Velocity-Verlet method
    r[i+1] = r[i] + DeltaT*v[i]+0.5*(DeltaT**2)*a
    rabs = sqrt(sum(r[i+1]*r[i+1]))
    anew = -alpha*r[i+1]/(rabs**3)
    v[i+1] = v[i] + 0.5*DeltaT*(a+anew)
    E[i+1] = 0.5*m*(v[i+1,0]**2+v[i+1,1]**2)-alpha/rabs
    t[i+1] = t[i] + DeltaT
# Plot position as function of time
fig, ax = plt.subplots(3,1)
ax[0].set_ylabel('y')
ax[0].set_xlabel('x')
ax[0].plot(r[:,0],r[:,1])
ax[1].set_xlabel('time')
ax[1].set_ylabel('y position')
ax[1].plot(t,r[:,0])
ax[2].set_xlabel('time')
ax[2].set_ylabel('y position')
ax[2].plot(t,r[:,1])

fig.tight_layout()
save_fig("2DimGravity")
plt.show()
print(E)

## Scattering and Cross Sections

Scattering experiments don't measure entire trajectories. For elastic
collisions, they measure the distribution of final scattering angles
at best. Most experiments use targets thin enough so that the number
of scatterings is typically zero or one. The cross section, $\sigma$,
describes the cross-sectional area for particles to scatter with an
individual target atom or nucleus. Cross section measurements form the
basis for MANY fields of physics. BThe cross section, and the
differential cross section, encapsulates everything measurable for a
collision where all that is measured is the final state, e.g. the
outgoing particle had momentum $\boldsymbol{p}_f$. y studying cross sections,
one can infer information about the potential interaction between the
two particles. Inferring, or constraining, the potential from the
cross section is a classic {\it inverse} problem. Collisions are
either elastic or inelastic. Elastic collisions are those for which
the two bodies are in the same internal state before and after the
collision. If the collision excites one of the participants into a
higher state, or transforms the particles into different species, or
creates additional particles, the collision is inelastic. Here, we
consider only elastic collisions.

For Coulomb forces, the cross section is infinite because the range of
the Coulomb force is infinite, but for interactions such as the strong
interaction in nuclear or particle physics, there is no long-range
force and cross-sections are finite. Even for Coulomb forces, the part
of the cross section that corresponds to a specific scattering angle,
$d\sigma/d\Omega$, which is a function of the scattering angle
$\phi_s$ is still finite.

If a particle travels through a thin target, the chance the particle
scatters is $P_{\rm scatt}=\sigma dN/dA$, where $dN/dA$ is the number
of scattering centers per area the particle encounters. If the density
of the target is $\rho$ particles per volume, and if the thickness of
the target is $t$, the areal density (number of target scatterers per
area) is $dN/dA=\rho t$. Because one wishes to quantify the collisions
independently of the target, experimentalists measure scattering
probabilities, then divide by the areal density to obtain
cross-sections,

$$
\begin{eqnarray}
\sigma=\frac{P_{\rm scatt}}{dN/dA}.
\end{eqnarray}
$$

Instead of merely stating that a particle collided, one can measure
the probability the particle scattered by a given angle. The
scattering angle $\phi_s$ is defined so that at zero the particle is
unscattered and at $\phi_s=\pi$ the particle is scattered directly
backward. Scattering angles are often described in the center-of-mass
frame, but that is a detail we will neglect for this first discussion,
where we will consider the scattering of particles moving classically
under the influence of fixed potentials $U(\boldsymbol{r})$. Because the
distribution of scattering angles can be measured, one expresses the
differential cross section,

<!-- Equation labels as ordinary links -->
<div id="_auto5"></div>

$$
\begin{equation}
\frac{d^2\sigma}{d\cos\phi_s~d\phi}.
\label{_auto5} \tag{10}
\end{equation}
$$

Usually, the literature expresses differential cross sections as

<!-- Equation labels as ordinary links -->
<div id="_auto6"></div>

$$
\begin{equation}
d\sigma/d\Omega=\frac{d\sigma}{d\cos\phi d\phi}=\frac{1}{2\pi}\frac{d\sigma}{d\cos\phi},
\label{_auto6} \tag{11}
\end{equation}
$$

where the last equivalency is true when the scattering does not depend
on the azimuthal angle $\phi$, as is the case for spherically
symmetric potentials.

The differential solid angle $d\Omega$ can be thought of as the area
subtended by a measurement, $dA_d$, divided by $r^2$, where $r$ is the
distance to the detector,

$$
\begin{eqnarray}
dA_d=r^2 d\Omega.
\end{eqnarray}
$$

With this definition $d\sigma/d\Omega$ is independent of the distance
from which one places the detector, or the size of the detector (as
long as it is small).

Differential scattering cross sections are calculated by assuming a
random distribution of impact parameters $b$. These represent the
distance in the $xy$ plane for particles moving in the $z$ direction
relative to the scattering center. An impact parameter $b=0$ refers to
being aimed directly at the target's center. The impact parameter
describes the transverse distance from the $z=0$ axis for the
trajectory when it is still far away from the scattering center and
has not yet passed it. The differential cross section can be expressed
in terms of the impact parameter,

<!-- Equation labels as ordinary links -->
<div id="_auto7"></div>

$$
\begin{equation}
d\sigma=2\pi bdb,
\label{_auto7} \tag{12}
\end{equation}
$$

which is the area of a thin ring of radius $b$ and thickness $db$. In
classical physics, one can calculate the trajectory given the incoming
kinetic energy $E$ and the impact parameter if one knows the mass and
potential. From the trajectory, one then finds the scattering angle
$\phi_s(b)$. The differential cross section is then

<!-- Equation labels as ordinary links -->
<div id="_auto8"></div>

$$
\begin{equation}
\frac{d\sigma}{d\Omega}=\frac{1}{2\pi}\frac{d\sigma}{d\cos\phi_s}=b\frac{db}{d\cos\phi_s}=\frac{b}{(d/db)\cos\phi_s(b)}.
\label{_auto8} \tag{13}
\end{equation}
$$

Typically, one would calculate $\cos\phi_s$ and $(d/db)\cos\phi_s$
as functions of $b$. This is sufficient to plot the differential cross
section as a function of $\phi_s$.

The total cross section is

<!-- Equation labels as ordinary links -->
<div id="_auto9"></div>

$$
\begin{equation}
\sigma_{\rm tot}=\int d\Omega\frac{d\sigma}{d\Omega}=2\pi\int d\cos\phi_s~\frac{d\sigma}{d\Omega}. 
\label{_auto9} \tag{14}
\end{equation}
$$

Even if the total cross section is infinite, e.g. Coulomb forces, one
can still have a finite differential cross section as we will see
later on.


An asteroid of mass $m$ and kinetic energy $E$ approaches a planet of
radius $R$ and mass $M$. What is the cross section for the asteroid to
impact the planet?

### Solution

Calculate the maximum impact parameter, $b_{\rm max}$, for which the asteroid will hit the planet. The total cross  section for impact is $\sigma_{\rm impact}=\pi b_{\rm max}^2$. The maximum cross-section can be found with the help of angular momentum conservation. The asteroid's incoming momentum is $p_0=\sqrt{2mE}$ and the angular momentum is $L=p_0b$. If the asteroid just grazes the planet, it is moving with zero radial kinetic energy at impact. Combining energy and angular momentum conservation and having $p_f$ refer to the momentum of the asteroid at a distance $R$,

$$
\begin{eqnarray*}
\frac{p_f^2}{2m}-\frac{GMm}{R}&=&E,\\
p_fR&=&p_0b_{\rm max},
\end{eqnarray*}
$$

allows one to solve for $b_{\rm max}$,

$$
\begin{eqnarray*}
b_{\rm max}&=&R\frac{p_f}{p_0}\\
&=&R\frac{\sqrt{2m(E+GMm/R)}}{\sqrt{2mE}}\\
\sigma_{\rm impact}&=&\pi R^2\frac{E+GMm/R}{E}.
\end{eqnarray*}
$$

## Rutherford Scattering

This refers to the calculation of $d\sigma/d\Omega$ due to an inverse
square force, $F_{12}=\pm\alpha/r^2$ for repulsive/attractive
interaction. Rutherford compared the scattering of $\alpha$ particles
($^4$He nuclei) off of a nucleus and found the scattering angle at
which the formula began to fail. This corresponded to the impact
parameter for which the trajectories would strike the nucleus. This
provided the first measure of the size of the atomic nucleus. At the
time, the distribution of the positive charge (the protons) was
considered to be just as spread out amongst the atomic volume as the
electrons. After Rutherford's experiment, it was clear that the radius
of the nucleus tended to be roughly 4 orders of magnitude smaller than
that of the atom, which is less than the size of a football relative
to Spartan Stadium.



The incoming and outgoing angles of the trajectory are at
$\pm\phi'$. They are related to the scattering angle by
$2\phi'=\pi+\phi_s$.

In order to calculate differential cross section, we must find how the
impact parameter is related to the scattering angle. This requires
analysis of the trajectory. We consider our previous expression for
the trajectory where we derived the elliptic form for the trajectory,
Eq. ([9](#eq:Ctrajectory)). For that case we considered an attractive
force with the particle's energy being negative, i.e. it was
bound. However, the same form will work for positive energy, and
repulsive forces can be considered by simple flipping the sign of
$\alpha$. For positive energies, the trajectories will be hyperbolas,
rather than ellipses, with the asymptotes of the trajectories
representing the directions of the incoming and outgoing
tracks. Rewriting Eq. ([9](#eq:Ctrajectory)),

<!-- Equation labels as ordinary links -->
<div id="eq:ruthtraj"></div>

$$
\begin{equation}\label{eq:ruthtraj} \tag{15}
r=\frac{1}{\frac{m\alpha}{L^2}+A\cos\phi}.
\end{equation}
$$

Once $A$ is large enough, which will happen when the energy is
positive, the denominator will become negative for a range of
$\phi$. This is because the scattered particle will never reach
certain angles. The asymptotic angles $\phi'$ are those for which
the denominator goes to zero,

<!-- Equation labels as ordinary links -->
<div id="_auto10"></div>

$$
\begin{equation}
\cos\phi'=-\frac{m\alpha}{AL^2}.
\label{_auto10} \tag{16}
\end{equation}
$$

The trajectory's point of closest approach is at $\phi=0$ and the
two angles $\phi'$, which have this value of $\cos\phi'$, are the
angles of the incoming and outgoing particles. From
Fig (**to come**), one can see that the scattering angle
$\phi_s$ is given by,

<!-- Equation labels as ordinary links -->
<div id="eq:sthetover2"></div>

$$
\begin{eqnarray}
\label{eq:sthetover2} \tag{17}
2\phi'-\pi&=&\phi_s,~~~\phi'=\frac{\pi}{2}+\frac{\phi_s}{2},\\
\nonumber
\sin(\phi_s/2)&=&-\cos\phi'\\
\nonumber
&=&\frac{m\alpha}{AL^2}.
\end{eqnarray}
$$

Now that we have $\phi_s$ in terms of $m,\alpha,L$ and $A$, we wish
to re-express $L$ and $A$ in terms of the impact parameter $b$ and the
energy $E$. This will set us up to calculate the differential cross
section, which requires knowing $db/d\phi_s$. It is easy to write
the angular momentum as

<!-- Equation labels as ordinary links -->
<div id="_auto11"></div>

$$
\begin{equation}
L^2=p_0^2b^2=2mEb^2.
\label{_auto11} \tag{18}
\end{equation}
$$

Finding $A$ is more complicated. To accomplish this we realize that
the point of closest approach occurs at $\phi=0$, so from
Eq. ([15](#eq:ruthtraj))

<!-- Equation labels as ordinary links -->
<div id="eq:rminofA"></div>

$$
\begin{eqnarray}
\label{eq:rminofA} \tag{19}
\frac{1}{r_{\rm min}}&=&\frac{m\alpha}{L^2}+A,\\
\nonumber
A&=&\frac{1}{r_{\rm min}}-\frac{m\alpha}{L^2}.
\end{eqnarray}
$$

Next, $r_{\rm min}$ can be found in terms of the energy because at the
point of closest approach the kinetic energy is due purely to the
motion perpendicular to $\hat{r}$ and

<!-- Equation labels as ordinary links -->
<div id="_auto12"></div>

$$
\begin{equation}
E=-\frac{\alpha}{r_{\rm min}}+\frac{L^2}{2mr_{\rm min}^2}.
\label{_auto12} \tag{20}
\end{equation}
$$

One can solve the quadratic equation for $1/r_{\rm min}$,

<!-- Equation labels as ordinary links -->
<div id="_auto13"></div>

$$
\begin{equation}
\frac{1}{r_{\rm min}}=\frac{m\alpha}{L^2}+\sqrt{(m\alpha/L^2)^2+2mE/L^2}.
\label{_auto13} \tag{21}
\end{equation}
$$

We can plug the expression for $r_{\rm min}$ into the expression for $A$, Eq. ([19](#eq:rminofA)),

<!-- Equation labels as ordinary links -->
<div id="_auto14"></div>

$$
\begin{equation}
A=\sqrt{(m\alpha/L^2)^2+2mE/L^2}=\sqrt{(\alpha^2/(4E^2b^4)+1/b^2}
\label{_auto14} \tag{22}
\end{equation}
$$

Finally, we insert the expression for $A$ into that for the scattering angle, Eq. ([17](#eq:sthetover2)),

<!-- Equation labels as ordinary links -->
<div id="eq:scattangle"></div>

$$
\begin{eqnarray}
\label{eq:scattangle} \tag{23}
\sin(\phi_s/2)&=&\frac{m\alpha}{AL^2}\\
\nonumber
&=&\frac{a}{\sqrt{a^2+b^2}}, ~~a\equiv \frac{\alpha}{2E}
\end{eqnarray}
$$

The differential cross section can now be found by differentiating the
expression for $\phi_s$ with $b$,

<!-- Equation labels as ordinary links -->
<div id="eq:rutherford"></div>

$$
\begin{eqnarray}
\label{eq:rutherford} \tag{24}
\frac{1}{2}\cos(\phi_s/2)d\phi_s&=&\frac{ab~db}{(a^2+b^2)^{3/2}}=\frac{bdb}{a^2}\sin^3(\phi_s/2),\\
\nonumber
d\sigma&=&2\pi bdb=\frac{\pi a^2}{\sin^3(\phi_s/2)}\cos(\phi_s/2)d\phi_s\\
\nonumber
&=&\frac{\pi a^2}{2\sin^4(\phi_s/2)}\sin\phi_s d\phi_s\\
\nonumber
\frac{d\sigma}{d\cos\phi_s}&=&\frac{\pi a^2}{2\sin^4(\phi_s/2)},\\
\nonumber
\frac{d\sigma}{d\Omega}&=&\frac{a^2}{4\sin^4(\phi_s/2)}.
\end{eqnarray}
$$

where $a= \alpha/2E$. This the Rutherford formula for the differential
cross section. It diverges as $\phi_s\rightarrow 0$ because
scatterings with arbitrarily large impact parameters still scatter to
arbitrarily small scattering angles. The expression for
$d\sigma/d\Omega$ is the same whether the interaction is positive or
negative.


Consider a particle of mass $m$ and charge $z$ with kinetic energy $E$
(Let it be the center-of-mass energy) incident on a heavy nucleus of
mass $M$ and charge $Z$ and radius $R$. Find the angle at which the
Rutherford scattering formula breaks down.

### Solution

Let $\alpha=Zze^2/(4\pi\epsilon_0)$. The scattering angle in Eq. ([23](#eq:scattangle)) is

$$
\sin(\phi_s/2)=\frac{a}{\sqrt{a^2+b^2}}, ~~a\equiv \frac{\alpha}{2E}.
$$

The impact parameter $b$ for which the point of closest approach
equals $R$ can be found by using angular momentum conservation,

$$
\begin{eqnarray*}
p_0b&=&b\sqrt{2mE}=Rp_f=R\sqrt{2m(E-\alpha/R)},\\
b&=&R\frac{\sqrt{2m(E-\alpha/R)}}{\sqrt{2mE}}\\
&=&R\sqrt{1-\frac{\alpha}{ER}}.
\end{eqnarray*}
$$

Putting these together

$$
\phi_s=2\sin^{-1}\left\{
\frac{a}{\sqrt{a^2+R^2(1-\alpha/(RE))}}
\right\},~~~a=\frac{\alpha}{2E}.
$$

It was from this departure of the experimentally measured
$d\sigma/d\Omega$ from the Rutherford formula that allowed Rutherford
to infer the radius of the gold nucleus, $R$.



Just like electrodynamics, one can define "fields", which for a small
additional mass $m$ are the force per mass and the additional
potential energy per mass. The {\it gravitational field} related to
the force has dimensions of force per mass, or acceleration, and can
be labeled $\boldsymbol{g}(\boldsymbol{r})$. The potential energy per mass has
dimensions of energy per mass. This is analogous to the
electromagnetic potential, which is the potential energy per charge,
and the electric field which is the force per charge.

Because the field $\boldsymbol{g}$ obeys the same inverse square law for a
point mass as the electric field does for a point charge, the
gravitational field also satisfies a version of Gauss's law,

<!-- Equation labels as ordinary links -->
<div id="eq:GravGauss"></div>

$$
\begin{equation}
\label{eq:GravGauss} \tag{25}
\oint d\boldsymbol{A}\cdot\boldsymbol{g}=-4\pi GM_{\rm inside}.
\end{equation}
$$

Here, $M_{\rm inside}$ is the net mass inside a closed area.

Gauss's law can be understood by considering a nozzle that sprays
paint in all directions uniformly from a point source. Let $B$ be the
number of gallons per minute of paint leaving the nozzle. If the
nozzle is at the center of a sphere of radius $r$, the paint per
square meter per minute that is deposited on some part of the sphere
is

$$
\begin{eqnarray}
F(r)&=&\frac{B}{4\pi r^2}.
\end{eqnarray}
$$

Now, let $F$ also be assigned a direction, so that it becomes a vector
pointing along the direction of the flying paint. For any surface that
surrounds the nozzle, not necessarily a sphere, one can state that

<!-- Equation labels as ordinary links -->
<div id="eq:paint"></div>

$$
\begin{eqnarray}
\label{eq:paint} \tag{26}
\oint \boldsymbol{dA}\cdot\boldsymbol{F}&=&B,
\end{eqnarray}
$$

regardless of the shape of the surface. This follows because the rate
at which paint is deposited on the surface should equal the rate at
which it leaves the nozzle. The dot product ensures that only the
component of $\boldsymbol{F}$ into the surface contributes to the deposition
of paint. Similarly, if $\boldsymbol{F}$ is any radial inverse-square forces,
that falls as $B/(4\pi r^2)$, then one can apply
Eq. ([26](#eq:paint)). For gravitational fields, $B/(4\pi)$ is replaced
by $GM$, and one quickly "derives" Gauss's law for gravity,
Eq. ([25](#eq:GravGauss)).


Consider Earth to have its mass $M$ uniformly distributed in a sphere
of radius $R$. Find the magnitude of the gravitational acceleration as
a function of the radius $r$ in terms of the acceleration of gravity
at the surface $g(R)$. Assume $r<R$, i.e. you are inside the surface.

{\bf Solution}: Take the ratio of Eq. ([25](#eq:GravGauss)) for two radii, $R$ and $r<R$,

$$
\begin{eqnarray*}
\frac{4\pi r^2 g(r)}{4\pi R^2 g(R)}&=&\frac{4\pi GM_{\rm inside~r}}{4\pi GM_{\rm inside~R}}\\
\nonumber
&=&\frac{r^3}{R^3}\\
\nonumber
g(r)&=&g(R)\frac{r}{R}~.
\end{eqnarray*}
$$

The potential energy per mass is similar conceptually to the voltage, or electric potential energy per charge, that was studied in electromagnetism, if $V\equiv U/m$, $\boldsymbol{g}=-\nabla V$.

## Tidal Forces


Consider a spherical planet of radius $r$ a distance $D$ from another
body of mass $M$. The magnitude of the force due to $M$ on an small
object of mass $\delta m$ on surface of the planet can be calculated
by performing a Taylor expansion about the center of the spherical
planet.

<!-- Equation labels as ordinary links -->
<div id="_auto15"></div>

$$
\begin{equation}
F=-\frac{GM\delta m}{D^2}+2\frac{GM\delta m}{D^3}\Delta D+\cdots
\label{_auto15} \tag{27}
\end{equation}
$$

If the $z$ direction points toward the large object, $\Delta D$ can be
referred to as $z$. In the accelerating frame of an observer at the
center of the planet,

<!-- Equation labels as ordinary links -->
<div id="_auto16"></div>

$$
\begin{equation}
\delta m\frac{d^2 z}{dt^2}=F-\delta ma'+{\rm other~forces~acting~on~} \delta m,
\label{_auto16} \tag{28}
\end{equation}
$$

where $a'$ is the acceleration of the observer. Because $\delta ma'$
equals the gravitational force on $\delta m$ if it were located at the
planet's center, one can write

<!-- Equation labels as ordinary links -->
<div id="_auto17"></div>

$$
\begin{equation}
m\frac{d^2z}{dt^2}=2\frac{GM\delta m}{D^3}z+{\rm other~forces~acting~on~}\delta m.
\label{_auto17} \tag{29}
\end{equation}
$$

Here the other forces could represent the forces acting on $\delta m$
from the spherical planet such as the gravitational force or the
contact force with the surface. If $\phi$ is the angle w.r.t. the
$z$ axis, the effective force acting on $\delta m$ is

<!-- Equation labels as ordinary links -->
<div id="_auto18"></div>

$$
\begin{equation}
F_{\rm eff}\approx 2\frac{GM\delta m}{D^3}r\cos\phi\hat{z}+{\rm other~forces~acting~on~}\delta m.
\label{_auto18} \tag{30}
\end{equation}
$$

This first force is the "tidal" force. It pulls objects outward from the center of the object. If the object were covered with water, it would distort the objects shape so that the shape would be elliptical, stretched out along the axis pointing toward the large mass $M$. The force is always along (either parallel or antiparallel to) the $\hat{z}$ direction.


Consider the Earth to be a sphere of radius $R$ covered with water,
with the gravitational acceleration at the surface noted by $g$. Now
assume that a distant body provides an additional constant
gravitational acceleration $\boldsymbol{a}$ pointed along the $z$ axis. Find
the distortion of the radius as a function of $\phi$. Ignore
planetary rotation and assume $a<<g$.

{\bf Solution}: Because Earth would then accelerate with $a$, the
field $a$ would seem invisible in the accelerating frame. A tidal
force would only appear if $a$ depended on position, i.e. $\nabla
\boldsymbol{a}\ne 0$.



Now consider that the field is no longer constant, but that instead $a=-kz$ with $|kR|<<g$.

{\bf Solution}: The surface of the planet needs to be at constant
potential (if the planet is not accelerating). The force per mass,
$-kz$ is like a spring, and the potential per mass is
$kz^2/2$. Otherwise water would move to a point of lower
potential. Thus, the potential energy for a sample mass $\delta m$ is

$$
\begin{eqnarray*}
V(R)+\delta m gh(\phi)-\frac{\delta m}{2}kr^2\cos^2\phi={\rm Constant}\\
V(R)+\delta mgh(\phi)-\frac{\delta m}{2}kR^2\cos^2\phi-\delta m kRh(\phi)\cos^2\phi-\frac{\delta m}{2}kh^2(\phi)\cos^2\phi={\rm Constant}.
\end{eqnarray*}
$$

Here, the potential due to the external field is $(1/2)kz^2$ so that $-\nabla U=-kz$. One now needs to solve for $h(\phi)$. Absorbing all the constant terms from both sides of the equation into one constant $C$, and because both $h$ and $kR$ are small, we can through away terms of order $h^2$ or $kRh$. This gives

$$
\begin{eqnarray*}
gh(\phi)-\frac{1}{2}kR^2\cos^2\phi&=&C,\\
h(\phi)&=&\frac{C}{g}+\frac{1}{2g}kR^2\cos^2\phi,\\
h(\phi)&=&\frac{1}{2g}kR^2(\cos^2\phi-1/3).
\end{eqnarray*}
$$

The term with the factor of $1/3$ replaced the constant and was chosen so that the average height of the water would be zero.

The Sun's mass is $27\times 10^6$ the Moon's mass, but the Sun is 390 times further away from Earth as the Sun. What is ratio of the tidal force of the Sun to that of the Moon.

{\bf Solution}: The gravitational force due to an object $M$ a distance $D$ away goes as $M/D^2$, but the tidal force is only the difference of that force over a distance $R$,

$$
F_{\rm tidal}\propto \frac{M}{D^3}R.
$$

Therefore the ratio of force is

$$
\begin{eqnarray*}
\frac{F_{\rm Sun's~tidal~force}}{F_{\rm Moon's~tidal~force}}
&=&\frac{M_{\rm sun}/D_{\rm sun}^3}{M_{\rm moon}/D_{\rm moon}^3}\\
&=&\frac{27\times 10^6}{390^3}=0.46.
\end{eqnarray*}
$$

The Moon more strongly affects tides than the Sun.










* 2d (10pt) With the solutions for $x$ and $y$, and $r^2=x^2+y^2$ and the definitions $\alpha=\frac{A^2+B^2+C^2+D^2}{2}$, $\beta=\frac{A^2-B^2+C^2-D^2}{2}$ and $\gamma=AB+CD$, show that

$$
r^2=\alpha+(\beta^2+\gamma^2)^{1/2}\cos(2\omega_0 t-\delta),
$$

with

$$
\delta=\arctan(\gamma/\beta).
$$

We start with $r^2 & = x^2+y^2$ and square the above analytical solutions and   after some **exciting algebraic manipulations** we arrive at

<!-- Equation labels as ordinary links -->
<div id="_auto19"></div>

$$
\begin{equation}
r^2  = x^2+y^2
\label{_auto19} \tag{31}
\end{equation}
$$

<!-- Equation labels as ordinary links -->
<div id="_auto20"></div>

$$
\begin{equation}  
 = \left(  A\cos\omega_0 t+B\sin\omega_0 t\right) ^2 + \left(  C\cos\omega_0 t+D\sin\omega_0 t\right) ^2
\label{_auto20} \tag{32}
\end{equation}
$$

<!-- Equation labels as ordinary links -->
<div id="_auto21"></div>

$$
\begin{equation}  
 = A^2\cos^2\omega_0 t+B^2\sin^2\omega_0 t + 2AB\sin\omega_0 t \cos\omega_0 t + C^2\cos^2\omega_0 t+D^2\sin^2\omega_0 t + 2CD\sin\omega_0 t \cos\omega_0 t
\label{_auto21} \tag{33}
\end{equation}
$$

<!-- Equation labels as ordinary links -->
<div id="_auto22"></div>

$$
\begin{equation} 
 = (A^2+C^2)\cos^2\omega_0 t + (B^2+D^2)\sin^2\omega_0 t + 2(AC + BD)\sin\omega_0 t \cos\omega_0 t
\label{_auto22} \tag{34}
\end{equation}
$$

<!-- Equation labels as ordinary links -->
<div id="_auto23"></div>

$$
\begin{equation} 
 = (B^2+D^2) + (A^2+C^2-B^2-D^2)\cos^2\omega_0 t + 2(AC + BD)2\sin2\omega_0 t
\label{_auto23} \tag{35}
\end{equation}
$$

<!-- Equation labels as ordinary links -->
<div id="_auto24"></div>

$$
\begin{equation} 
 = (B^2+D^2) + (A^2+C^2-B^2-D^2)\frac{1+\cos{2\omega_0 t}}{2} + 2(AC + BD)\frac{1}{2}\sin2\omega_0 t
\label{_auto24} \tag{36}
\end{equation}
$$

<!-- Equation labels as ordinary links -->
<div id="_auto25"></div>

$$
\begin{equation} 
 = \frac{2B^2+2D^2+A^2+C^2-B^2-D^2}{2} + (A^2+C^2-B^2-D^2)\frac{\cos{2\omega_0 t}}{2} + (AC + BD)\sin2\omega_0 t
\label{_auto25} \tag{37}
\end{equation}
$$

<!-- Equation labels as ordinary links -->
<div id="_auto26"></div>

$$
\begin{equation} 
 = \frac{B^2+D^2+A^2+C^2}{2} + \frac{A^2+C^2-B^2-D^2}{2}\cos{2\omega_0 t} + (AC + BD)\sin2\omega_0 t
\label{_auto26} \tag{38}
\end{equation}
$$

<!-- Equation labels as ordinary links -->
<div id="_auto27"></div>

$$
\begin{equation} 
 = \alpha + \beta\cos{2\omega_0 t} + \gamma\sin2\omega_0 t
\label{_auto27} \tag{39}
\end{equation}
$$

<!-- Equation labels as ordinary links -->
<div id="_auto28"></div>

$$
\begin{equation} 
 = \alpha + \sqrt{\beta^2+\gamma^2}\left( \frac{\beta}{\sqrt{\beta^2+\gamma^2}}\cos{2\omega_0 t} + \frac{\gamma}{\sqrt{\beta^2+\gamma^2}}\sin2\omega_0 t\right) 
\label{_auto28} \tag{40}
\end{equation}
$$

<!-- Equation labels as ordinary links -->
<div id="_auto29"></div>

$$
\begin{equation} 
 = \alpha + \sqrt{\beta^2+\gamma^2}\left( \cos{\delta}\cos{2\omega_0 t} + \sin{\delta}\sin2\omega_0 t\right) 
\label{_auto29} \tag{41}
\end{equation}
$$

<!-- Equation labels as ordinary links -->
<div id="_auto30"></div>

$$
\begin{equation} 
 = \alpha + \sqrt{\beta^2+\gamma^2}\cos{\left( 2\omega_0 t - \delta\right) },
\label{_auto30} \tag{42}
\end{equation}
$$

which is what we wanted to show.  





### Exercise 4, equations for an ellipse (10pt)

Consider an ellipse defined by the sum of the distances from the two foci being $2D$, which expressed in a Cartesian coordinates with the middle of the ellipse being at the origin becomes

$$
\sqrt{(x-a)^2+y^2}+\sqrt{(x+a)^2+y^2}=2D.
$$

Here the two foci are at $(a,0)$ and $(-a,0)$. Show that this form is can be written as

$$
\frac{x^2}{D^2}+\frac{y^2}{D^2-a^2}=1.
$$

We start by squaring the two sides and, again,  after some **exciting algebraic manipulations** we arrive at

$$
\sqrt{(x-a)^2+y^2}+\sqrt{(x+a)^2+y^2} =2D
\\ (x-a)^2 + y^2 + (x+a)^2 + y^2 + 2\sqrt{(x-a)^2 + y^2}\sqrt{(x+a)^2+y^2}  = 4D^2
\\ 2y^2 + 2x^2 + 2a^2 + 2\sqrt{(x-a)^2(x+a)^2 + y^4 + y^2[(x-a)^2+(x+a)^2]}  = 4D^2
\\ y^2 + x^2 + a^2 + \sqrt{(x^2-a^2)^2 + y^4 + y^2(2x^2+2a^2)}  = 2D^2
\\ \sqrt{(x^2-a^2)^2 + y^4 + y^2(2x^2+2a^2)}  = 2D^2 -( y^2 + x^2 + a^2 )
\\ (x^2-a^2)^2 + y^4 + y^2(2x^2+2a^2)  = 4D^4 + y^4 + x^4 + a^4 - 4D^2( y^2 + x^2 + a^2 ) + 2(y^2x^2+y^2a^2+x^2a^2)
\\ x^4-2x^2a^2+a^4 + y^4 + 2y^2x^2+2y^2a^2  = 4D^4 + y^4 + x^4 + a^4 - 4D^2y^2 -4D^2 x^2 -4D^2 a^2 + 2y^2x^2+2y^2a^2+2x^2a^2
\\ 4D^4 - 4D^2y^2 -4D^2 x^2 -4D^2 a^2 +4x^2a^2 = 0
\\ D^4 - D^2y^2 -D^2 x^2 -D^2 a^2 +x^2a^2 = 0
\\ D^2(D^2-a^2) - x^2(D^2-a^2) = D^2y^2
\\ D^2 - x^2 = \frac{D^2y^2}{D^2-a^2}
\\ 1 - \frac{x^2}{D^2} = \frac{y^2}{D^2-a^2}
\\ \frac{x^2}{D^2} + \frac{y^2}{D^2-a^2} = 1,
$$

where the last line is indeed the equation for an ellipse. 




Consider a particle in an attractive potential

$$
U(r)=-\alpha/r.
$$

The quantity $r$ is the absolute value of the relative position. We
will use the reduced mass $\mu$ and the angular momentum $L$, as
discussed during the lectures. With the transformation of a two-body
problem to the center-of-mass frame, the actual equations look like an
*effective* one-body problem. The energy of the system is $E$ and the
minimum of the effective potential is $r_{\rm min}$.


The analytical solution to the radial equation of motion is

$$
r(\phi) = \frac{1}{\frac{\mu\alpha}{L^2}+A\cos{(\phi)}}.
$$

Find the value of $A$. Hint: Use the fact that at $r_{\rm min}$
there is no radial kinetic energy and $E=-\alpha/r_{\rm min}+L^2/2mr_{\rm min}^2$.

At  $r_{\mathrm{min}}$  and $r_{\mathrm{max}}$ , all the kinetic energy is stored in the velocity in the direction perpendicular to $r$  since the radial velocity is set to zero . We can calculate using angular momentum and from there, find  𝐴  in terms of the energy  𝐸  which is constant. But first, we need to find  𝑟min  from the conservation of energy:

$$
E = U(r) + \frac{1}{2} \mu(v_{\perp}^2 + v_{\parallel})
\\
E = \frac{-\alpha}{r_{\min}} + \frac{1}{2} \mu\left( \frac{L}{\mu r_{\min}}\right) ^2
\\
E r_{\min}^2 - \frac{1}{2}\mu\left( \frac{L}{\mu}\right) ^2 + \alpha r_{\min} = 0
\\
r_{\min}^2 + \frac{\alpha}{E} r_{\min} - \frac{L^2}{2E\mu} = 0
\\
r_{\min} = - \frac{\alpha}{2E} \pm \frac{1}{2} \sqrt{\frac{\alpha^2}{E^2} + 2\frac{L^2}{E\mu}}
$$

Since we're looking for the minimum, the  ±  sign must be negative (then  𝑟min  will not be negative since  𝐸<0 ). Therefore, we have

$$
frac{1}{\frac{\mu\alpha}{L^2}+A} = -\frac{\alpha}{2E} - \frac{1}{2} \sqrt{\frac{\alpha^2}{E^2} + 2\frac{L^2}{E\mu}}
\\
A = - \frac{\mu\alpha}{L^2} - \frac{2E}{\alpha + \sqrt{\alpha^2 + 2\frac{L^2E}{\mu}}}
$$

### Exercise 2 (20pt) Inverse-square force

Consider again the same effective potential as in exercise 1. This leads to an attractive inverse-square-law force, $F=-\alpha/r^2$. Consider a particle of mass $m$ with angular momentum $L$. Taylor sections 8.4-8.7 are relevant background material.  See also the harmonic oscillator potential from hw8. The equation of motion for the radial degrees of freedom is (see also hw8) in the center-of-mass frame in two dimensions with $x=r\cos{(\phi)}$ and $y=r\sin{(\phi)}$ and
$r\in [0,\infty)$, $\phi\in [0,2\pi]$ and $r=\sqrt{x^2+y^2}$ are given by

$$
\ddot{r}=-\frac{1}{m}\frac{dV(r)}{dr}+r\dot{\phi}^2,
$$

and

$$
\dot{\phi}=\frac{L}{m r^2}.
$$

Here $V(r)$ is any central force which depends only on the relative coordinate.


* 2a (5pt)  Find the radius of a circular orbit by solving for the position of the minimum of the effective potential.

<!-- Equation labels as ordinary links -->
<div id="_auto31"></div>

$$
\begin{equation}
\frac{1}{m}\frac{dV(r)}{dr}  = r\dot{\phi}^2
\label{_auto31} \tag{43}
\end{equation}
$$

<!-- Equation labels as ordinary links -->
<div id="_auto32"></div>

$$
\begin{equation}  \frac{1}{m}\left( -\frac{-\alpha}{r^2}\right)   = r \frac{L^2}{m^2r^4}
\label{_auto32} \tag{44}
\end{equation}
$$

<!-- Equation labels as ordinary links -->
<div id="_auto33"></div>

$$
\begin{equation}  \frac{\alpha}{mr^2}  = \frac{L^2}{m^2r^3}
\label{_auto33} \tag{45}
\end{equation}
$$

<!-- Equation labels as ordinary links -->
<div id="_auto34"></div>

$$
\begin{equation}  r  = \frac{L^2}{m\alpha}
\label{_auto34} \tag{46}
\end{equation}
$$

* 2b (5pt) At the minimum, the radial velocity is zero and it is only the [centripetal velocity](https://en.wikipedia.org/wiki/Centripetal_force) which is nonzero. This implies that $\ddot{r}=0$.  What is the angular frequency, $\dot{\theta}$, of the orbit? Solve this by setting $\ddot{r}=0=F/m+\dot{\theta}^2r$.

<!-- Equation labels as ordinary links -->
<div id="_auto35"></div>

$$
\begin{equation}
\dot{\theta}^2 r  = - \frac{F}{m}
\label{_auto35} \tag{47}
\end{equation}
$$

<!-- Equation labels as ordinary links -->
<div id="_auto36"></div>

$$
\begin{equation}  \dot{\theta}^2 r  = - \frac{-\frac{\alpha}{r^2}}{m}
\label{_auto36} \tag{48}
\end{equation}
$$

<!-- Equation labels as ordinary links -->
<div id="_auto37"></div>

$$
\begin{equation}  \dot{\theta}^2  = \frac{\alpha}{mr^3}
\label{_auto37} \tag{49}
\end{equation}
$$

<!-- Equation labels as ordinary links -->
<div id="_auto38"></div>

$$
\begin{equation}  \dot{\theta}  = \pm \sqrt{\frac{\alpha}{mr^3}}
\label{_auto38} \tag{50}
\end{equation}
$$

<!-- Equation labels as ordinary links -->
<div id="_auto39"></div>

$$
\begin{equation}  \dot{\theta}  = \pm \sqrt{\frac{\alpha}{m\frac{L^6}{m^3\alpha^3}}}
\label{_auto39} \tag{51}
\end{equation}
$$

<!-- Equation labels as ordinary links -->
<div id="_auto40"></div>

$$
\begin{equation}  \dot{\theta}  = \pm \sqrt{\frac{\alpha^4m^2}{L^6}}
\label{_auto40} \tag{52}
\end{equation}
$$

<!-- Equation labels as ordinary links -->
<div id="_auto41"></div>

$$
\begin{equation}  \dot{\theta}  = \pm \frac{\alpha^2m}{L^3}
\label{_auto41} \tag{53}
\end{equation}
$$

* 2c (5pt) Find the effective spring constant for the particle at the minimum.

We have shown in class that from the taylor expansion, we have

$$
k = \frac{d^2V_{\text{eff}}}{dr^2}
$$

Therefore, all we have to do is find the second derivative of $V_{\text{eff}}$ around the minimum point of $V_{\text{eff}}$ where $\dot{r} = \ddot{r} = 0$.

<!-- Equation labels as ordinary links -->
<div id="_auto42"></div>

$$
\begin{equation}
k  = \frac{d^2V_{\text{eff}}}{dr^2}
\label{_auto42} \tag{54}
\end{equation}
$$

<!-- Equation labels as ordinary links -->
<div id="_auto43"></div>

$$
\begin{equation}   = \frac{d^2\left( -\frac{\alpha}{r} + \frac{1}{2} \frac{L^2}{mr^2}\right) }{dr^2}
\label{_auto43} \tag{55}
\end{equation}
$$

<!-- Equation labels as ordinary links -->
<div id="_auto44"></div>

$$
\begin{equation}   = -\frac{2\alpha}{r^3} + \frac{3L^2}{mr^4}
\label{_auto44} \tag{56}
\end{equation}
$$

<!-- Equation labels as ordinary links -->
<div id="_auto45"></div>

$$
\begin{equation}   = -\frac{2\alpha}{\frac{L^6}{m^3\alpha^3}} + \frac{3L^2}{m\frac{L^8}{m^4\alpha^4}}
\label{_auto45} \tag{57}
\end{equation}
$$

<!-- Equation labels as ordinary links -->
<div id="_auto46"></div>

$$
\begin{equation}   = -\frac{2m^3\alpha^4}{L^6} + \frac{3m^3\alpha^4}{L^6}
\label{_auto46} \tag{58}
\end{equation}
$$

<!-- Equation labels as ordinary links -->
<div id="_auto47"></div>

$$
\begin{equation}   = \frac{m^3\alpha^4}{L^6}
\label{_auto47} \tag{59}
\end{equation}
$$

* 2d (5pt) What is the angular frequency for small vibrations about the minimum? How does this compare with the answer to (3b)?

For small deviations $\delta r$ of $r$,

$$
m\frac{d^2\left(  \delta r \right) }{dt^2} = -k \delta r
$$

The solution of this differential equation is of the form

$$
\delta r = A \cos(\omega t + \phi)
$$

where

<!-- Equation labels as ordinary links -->
<div id="_auto48"></div>

$$
\begin{equation}
\omega =  \sqrt{\frac{k}{m}}
\label{_auto48} \tag{60}
\end{equation}
$$

<!-- Equation labels as ordinary links -->
<div id="_auto49"></div>

$$
\begin{equation}   = \sqrt{\frac{m^2\alpha^4}{L^6}} 
\label{_auto49} \tag{61}
\end{equation}
$$

<!-- Equation labels as ordinary links -->
<div id="_auto50"></div>

$$
\begin{equation}   = \frac{m\alpha^2}{L^3}
\label{_auto50} \tag{62}
\end{equation}
$$

This is in fact equal to the expression for $\dot{\theta}$. This means that small perturbations oscillate in sync with the orbit and this traces out an ellipse with a very small eccentricity, a very nice physical result.


### Exercise 3, Inverse-square force again (10pt)

Consider again a  particle of mass $m$ in the same attractive potential, $U(r)=-\alpha/r$, with angular momentum $L$ with just the right energy so that

$$
A=m\alpha/L^2
$$

where $A$ comes from the expression

$$
r=\frac{1}{(m\alpha/L^2)+A\cos{(\phi)}}.
$$

The trajectory can then be rewritten as

$$
r=\frac{2r_0}{1+\cos\theta},~~~r_0=\frac{L^2}{2m\alpha}.
$$

* 3a (5pt) Show that for this case the total energy $E$ approaches zero.

<!-- Equation labels as ordinary links -->
<div id="_auto51"></div>

$$
\begin{equation}
E  = - \frac{\alpha}{r} + \frac{1}{2} m \left(  (\dot{\theta}r)^2+\dot{r}^2\right) 
\label{_auto51} \tag{63}
\end{equation}
$$

<!-- Equation labels as ordinary links -->
<div id="_auto52"></div>

$$
\begin{equation}   = - \frac{\alpha}{r} + \frac{1}{2} m \left[  \left( \frac{L}{mr^2}r\right) ^2+\left( \frac{dr}{d\theta}\dot{\theta}\right) ^2\right] 
\label{_auto52} \tag{64}
\end{equation}
$$

<!-- Equation labels as ordinary links -->
<div id="_auto53"></div>

$$
\begin{equation}   = - \frac{\alpha}{2r_0}(1+\cos\theta) + \frac{1}{2} m \left[  \left( \frac{L(1+\cos\theta)}{2mr_0}\right) ^2+\left( 2r_0\frac{-1}{(1+\cos\theta)^2}(-\sin\theta)\frac{L}{mr^2}\right) ^2\right] 
\label{_auto53} \tag{65}
\end{equation}
$$

<!-- Equation labels as ordinary links -->
<div id="_auto54"></div>

$$
\begin{equation}   = - \frac{\alpha}{2r_0}(1+\cos\theta) + \frac{1}{2} m \left[  \left( \frac{L(1+\cos\theta)}{2mr_0}\right) ^2+\left( 2r_0\frac{-1}{(1+\cos\theta)^2}(-\sin\theta)\frac{L(1+\cos\theta)^2}{4mr_0^2}\right) ^2\right] 
\label{_auto54} \tag{66}
\end{equation}
$$

<!-- Equation labels as ordinary links -->
<div id="_auto55"></div>

$$
\begin{equation}   = - \frac{\alpha}{2r_0}(1+\cos\theta) + 
\frac{1}{2} m \left[  \left( \frac{L(1+\cos\theta)}{2mr_0}\right) ^2+\left( \sin\theta\frac{L}{2mr_0}\right) ^2\right] 
\label{_auto55} \tag{67}
\end{equation}
$$

<!-- Equation labels as ordinary links -->
<div id="_auto56"></div>

$$
\begin{equation}   = - \frac{\alpha}{2r_0}(1+\cos\theta) + 
\frac{1}{2} m \left[  \left( \frac{L(1+\cos\theta)}{2mr_0}\right) ^2+\left( \sin\theta\frac{L}{2mr_0}\right) ^2\right] 
\label{_auto56} \tag{68}
\end{equation}
$$

<!-- Equation labels as ordinary links -->
<div id="_auto57"></div>

$$
\begin{equation}   = - \frac{\alpha}{2r_0}(1+\cos\theta) + 
\frac{1}{2} m \frac{L^2}{4m^2r_0^2} \left[  \left( 1+\cos\theta\right) ^2+\left( \sin\theta\right) ^2\right] 
\label{_auto57} \tag{69}
\end{equation}
$$

<!-- Equation labels as ordinary links -->
<div id="_auto58"></div>

$$
\begin{equation}   = - \frac{\alpha}{2r_0}(1+\cos\theta) + 
\frac{1}{2} \frac{L^2}{4mr_0^2} \left(  1 + \cos^2\theta + 2\cos \theta + \sin^2\theta\right) 
\label{_auto58} \tag{70}
\end{equation}
$$

<!-- Equation labels as ordinary links -->
<div id="_auto59"></div>

$$
\begin{equation}   = - \frac{\alpha}{2r_0}(1+\cos\theta) + 
\frac{1}{2} \frac{L^2}{4mr_0^2} \left(  2 + 2\cos \theta \right) 
\label{_auto59} \tag{71}
\end{equation}
$$

<!-- Equation labels as ordinary links -->
<div id="_auto60"></div>

$$
\begin{equation}   = (1+\cos\theta) \left( - \frac{\alpha}{2r_0} + \frac{L^2}{4mr_0^2}\right) 
\label{_auto60} \tag{72}
\end{equation}
$$

<!-- Equation labels as ordinary links -->
<div id="_auto61"></div>

$$
\begin{equation}   = (1+\cos\theta) \left( - \frac{\alpha}{2\frac{L^2}{2m\alpha}} + \frac{L^2}{4m\frac{L^4}{4m^2\alpha^2}}\right) 
\label{_auto61} \tag{73}
\end{equation}
$$

<!-- Equation labels as ordinary links -->
<div id="_auto62"></div>

$$
\begin{equation}   = (1+\cos\theta) \left( - \frac{m\alpha^2}{L^2} + \frac{m\alpha^2}{L^2}\right) 
\label{_auto62} \tag{74}
\end{equation}
$$

<!-- Equation labels as ordinary links -->
<div id="_auto63"></div>

$$
\begin{equation}   = 0
\label{_auto63} \tag{75}
\end{equation}
$$

* 3b (5pt) With zero energy $E=0$, write this trajectory in a more recognizable parabolic form, that is express $x_0$ and $R$ in terms of $r_0$ using

$$
x=x_0-\frac{y^2}{R}.
$$

We have that

<!-- Equation labels as ordinary links -->
<div id="_auto64"></div>

$$
\begin{equation}
x  = r \cos\theta
\label{_auto64} \tag{76}
\end{equation}
$$

<!-- Equation labels as ordinary links -->
<div id="_auto65"></div>

$$
\begin{equation} 
y  = r \sin \theta,
\label{_auto65} \tag{77}
\end{equation}
$$

we obtain

<!-- Equation labels as ordinary links -->
<div id="_auto66"></div>

$$
\begin{equation}
y  = r \sin\theta
\label{_auto66} \tag{78}
\end{equation}
$$

<!-- Equation labels as ordinary links -->
<div id="_auto67"></div>

$$
\begin{equation} 
 = \frac{2r_0}{1+\cos\theta}\sin\theta
\label{_auto67} \tag{79}
\end{equation}
$$

<!-- Equation labels as ordinary links -->
<div id="_auto68"></div>

$$
\begin{equation} 
 = \frac{2r_0}{1-\cos^2\theta}\sin\theta(1-\cos\theta)
\label{_auto68} \tag{80}
\end{equation}
$$

<!-- Equation labels as ordinary links -->
<div id="_auto69"></div>

$$
\begin{equation} 
 = \frac{2r_0(1-\cos\theta)}{\sin\theta},
\label{_auto69} \tag{81}
\end{equation}
$$

and

<!-- Equation labels as ordinary links -->
<div id="_auto70"></div>

$$
\begin{equation}
x  = r \sin\theta
\label{_auto70} \tag{82}
\end{equation}
$$

<!-- Equation labels as ordinary links -->
<div id="_auto71"></div>

$$
\begin{equation} 
 = \frac{2r_0}{1+\cos\theta}\cos\theta
\label{_auto71} \tag{83}
\end{equation}
$$

<!-- Equation labels as ordinary links -->
<div id="_auto72"></div>

$$
\begin{equation} 
 = \frac{2r_0}{1-\cos^2\theta}\cos\theta(1-\cos\theta)
\label{_auto72} \tag{84}
\end{equation}
$$

<!-- Equation labels as ordinary links -->
<div id="_auto73"></div>

$$
\begin{equation} 
 = \frac{2r_0(\cos\theta-\cos^2\theta)}{\sin^2 \theta}.
\label{_auto73} \tag{85}
\end{equation}
$$

Here  we notice that the denominator of $x$ is the square of the denominator of $y$. We also have

$$
y^2 = \frac{4r_0^2(1-2\cos\theta+\cos^2\theta)}{\sin^2\theta}.
$$

Let try to add them such that $\cos\theta$ cancels out, that is

<!-- Equation labels as ordinary links -->
<div id="_auto74"></div>

$$
\begin{equation}
x + \frac{y^2}{4r_0}  = \frac{2r_0(\cos\theta-\cos^2\theta)}{\sin^2 \theta} + \frac{4r_0^2(1-2\cos\theta+\cos^2\theta)}{\sin^2\theta}\frac{1}{4r_0}
\label{_auto74} \tag{86}
\end{equation}
$$

<!-- Equation labels as ordinary links -->
<div id="_auto75"></div>

$$
\begin{equation}   = \frac{r_0}{\sin^2\theta}\left(  2\cos\theta-2\cos^2\theta + 1 - 2\cos\theta + \cos^2\theta\right) 
\label{_auto75} \tag{87}
\end{equation}
$$

<!-- Equation labels as ordinary links -->
<div id="_auto76"></div>

$$
\begin{equation}   = \frac{r_0}{\sin^2\theta}\left(  -2\cos^2\theta + 1 + \cos^2\theta\right) 
\label{_auto76} \tag{88}
\end{equation}
$$

<!-- Equation labels as ordinary links -->
<div id="_auto77"></div>

$$
\begin{equation}   = \frac{r_0}{\sin^2\theta}\left(  1 - \cos^2\theta\right) 
\label{_auto77} \tag{89}
\end{equation}
$$

<!-- Equation labels as ordinary links -->
<div id="_auto78"></div>

$$
\begin{equation}   = \frac{r_0}{\sin^2\theta}\left(  \sin^2\theta\right) 
\label{_auto78} \tag{90}
\end{equation}
$$

<!-- Equation labels as ordinary links -->
<div id="_auto79"></div>

$$
\begin{equation}   = r_0
\label{_auto79} \tag{91}
\end{equation}
$$

Thus, we have

$$
x = r_0 - \frac{y^2}{4r_0}
$$

### Exercise 4, parabolic and hyperbolic orbits (10pt)

The solution to the radial function for an inverse-square-law force, see for example Taylor equation (8.59) or the equation above, is

$$
r(\phi) = \frac{c}{1+\epsilon\cos{(\phi)}}.
$$

For $\epsilon=1$ (or the energy $E=0$) the orbit reduces to a parabola as we saw in the previous exercise,
while for $\epsilon > 1$ (or energy positive) the orbit becomes a hyperbola. The equation for a hyperbola in Cartesian coordinates is

$$
\frac{(x-\delta)^2}{\alpha^2}-\frac{y^2}{\beta^2}=1.
$$

For a hyperbola, identify the constants $\alpha$, $\beta$ and $\delta$ in terms of the constants $c$ and $\epsilon$ for $r(\phi)$.

<!-- Equation labels as ordinary links -->
<div id="_auto80"></div>

$$
\begin{equation}
x  = r\cos\phi
\label{_auto80} \tag{92}
\end{equation}
$$

<!-- Equation labels as ordinary links -->
<div id="_auto81"></div>

$$
\begin{equation}   = \frac{c\cos\phi}{1+\epsilon\cos\phi}
\label{_auto81} \tag{93}
\end{equation}
$$

<!-- Equation labels as ordinary links -->
<div id="_auto82"></div>

$$
\begin{equation}
y  = r\sin\phi 
\label{_auto82} \tag{94}
\end{equation}
$$

<!-- Equation labels as ordinary links -->
<div id="_auto83"></div>

$$
\begin{equation}   = \frac{c\sin\phi}{1+\epsilon\cos\phi}
\label{_auto83} \tag{95}
\end{equation}
$$

Therefore,

<!-- Equation labels as ordinary links -->
<div id="_auto84"></div>

$$
\begin{equation}
\frac{(x-\delta)^2}{\alpha^2} - \frac{y^2}{\beta^2} 
 = \frac{(\frac{c\cos\phi-\delta(1+\epsilon\cos\phi)}{1+\epsilon\cos\phi})^2}{\alpha^2} - \frac{(\frac{c\sin\phi}{1+\epsilon\cos\phi})^2}{\beta^2}
\label{_auto84} \tag{96}
\end{equation}
$$

<!-- Equation labels as ordinary links -->
<div id="_auto85"></div>

$$
\begin{equation}   = \frac{\beta^2 c^2\cos^2\phi + \beta^2\delta^2 + \beta^2\delta^2 \epsilon^2 \cos^2 \phi - 2\beta^2\delta c \cos\phi - 2 \beta^2\delta c \epsilon \cos^2 \phi + 2\beta^2\delta^2 \epsilon \cos \phi - \alpha^2 c^2 \sin^2 \phi}{\alpha^2\beta^2(1 + 2\epsilon\cos\phi + \epsilon^2\cos^2\phi)}
\label{_auto85} \tag{97}
\end{equation}
$$

<!-- Equation labels as ordinary links -->
<div id="_auto86"></div>

$$
\begin{equation}   = \frac{
\beta^2\cos^2\phi (c^2 + \delta^2 \epsilon^2 - 2 \delta c \epsilon) - \alpha^2 c^2 \sin^2 \phi + \beta^2\delta^2 + 2\beta^2\delta \cos\phi (-c + \delta \epsilon)
}{\alpha^2\beta^2(1 + 2\epsilon\cos\phi + \epsilon^2\cos^2\phi)}
\label{_auto86} \tag{98}
\end{equation}
$$

<!-- Equation labels as ordinary links -->
<div id="_auto87"></div>

$$
\begin{equation}   = \frac{
(\beta^2\delta^2 - \alpha^2 c^2)
 + 2\beta^2\delta \cos\phi (\delta \epsilon-c)
 + \cos^2\phi (\beta^2c^2 + \beta^2\delta^2 \epsilon^2 - 2\beta^2 \delta c \epsilon + \alpha^2 c^2)
}{\alpha^2\beta^2(1 + 2\epsilon\cos\phi + \epsilon^2\cos^2\phi)}
\label{_auto87} \tag{99}
\end{equation}
$$

<!-- Equation labels as ordinary links -->
<div id="_auto88"></div>

$$
\begin{equation}   = 1
\label{_auto88} \tag{100}
\end{equation}
$$

We can seperate this into several equations:

$$
\frac{\beta^2\delta^2 - \alpha^2 c^2}{\alpha^2\beta^2} = 1
\\ \frac{2\beta^2\delta \cos\phi (\delta \epsilon-c)}{\alpha^2\beta^2} = 2\epsilon\cos\phi
\\ \frac{\cos^2\phi (\beta^2c^2 + \beta^2\delta^2 \epsilon^2 - 2\beta^2 \delta c \epsilon + \alpha^2 c^2)}{\alpha^2\beta^2} = \epsilon^2\cos^2\phi
$$

These can further be simplified:

$$
\frac{\delta^2}{\alpha^2} - \frac{c^2}{\beta^2} = 1
\\
\frac{\delta^2\epsilon}{\alpha^2} - \frac{\delta c}{\beta^2} = \epsilon
\\
\frac{c^2}{\alpha^2} + \frac{\delta^2\epsilon^2}{\alpha^2} - 2\frac{\delta c \epsilon}{\alpha^2} + \frac{c^2}{\beta^2}
= \epsilon^2
$$

Now, all we have to do is solve these three equations for the three unknowns $\alpha$, $\beta$, and $\gamma$:

From the first equation, we have

$$
\frac{1}{\beta^2} = \frac{\delta^2}{c^2\alpha^2} - \frac{1}{c^2}
$$

Therefore,

$$
\frac{\delta^2\epsilon}{\alpha^2} - \left(  \frac{\delta^2}{c^2\alpha^2} - \frac{1}{c^2} \right) \delta c = 
\frac{\delta^2\epsilon}{\alpha^2} - \frac{\delta^3}{c\alpha^2} + \frac{\delta}{c}
= \epsilon
\\
\frac{c^2}{\alpha^2} + \frac{\delta^2\epsilon^2}{\alpha^2} - 2\frac{\delta c \epsilon}{\alpha^2} + c^2\left(  \frac{\delta^2}{c^2\alpha^2} - \frac{1}{c^2} \right)  =
\frac{c^2}{\alpha^2} + \frac{\delta^2\epsilon^2}{\alpha^2} - 2\frac{\delta c \epsilon}{\alpha^2}
+ \frac{\delta^2}{\alpha^2} - 1
= \epsilon^2
$$

From here  we obtain

$$
\frac{1}{\alpha^2} = \frac{\epsilon-\frac{\delta}{c}}{\delta^2\epsilon - \frac{\delta^3}{c}} = \frac{1}{\delta^2}\frac{\epsilon-\frac{\delta}{c}}{\epsilon-\frac{\delta}{c}}
$$

This means we have two possibilities: either $\delta^2 = \alpha^2$ or $\delta = c$. Since the first option would mean $\beta \rightarrow \pm \infty$, the second option must be true. Hence,

$$
\frac{c^2}{\alpha^2} + \frac{c^2\epsilon^2}{\alpha^2} - 2\frac{c^2 \epsilon}{\alpha^2}
+ \frac{c^2}{\alpha^2} - 1
= \epsilon^2
\\
\frac{c^2}{\alpha^2} (1 + \epsilon^2 - 2 \epsilon) = 1 + \epsilon^2
\\ \frac{c^2}{\alpha^2} = \frac{1 + \epsilon^2}{(1-\epsilon)^2}
\\ \alpha = \pm c \sqrt{\frac{(1-\epsilon)^2}{1 + \epsilon^2}}.
$$

And we have

<!-- Equation labels as ordinary links -->
<div id="_auto89"></div>

$$
\begin{equation}
\beta  = \pm \sqrt{\frac{1}{\frac{\delta^2}{c^2\alpha^2} - \frac{1}{c^2}}}
\label{_auto89} \tag{101}
\end{equation}
$$

<!-- Equation labels as ordinary links -->
<div id="_auto90"></div>

$$
\begin{equation}   = \pm \sqrt{\frac{1}{\frac{1 + \epsilon^2}{(1-\epsilon)^2} - \frac{1}{c^2}}}
\label{_auto90} \tag{102}
\end{equation}
$$

<!-- Equation labels as ordinary links -->
<div id="_auto91"></div>

$$
\begin{equation}   = \pm c \sqrt{\frac{1}{\frac{1 + \epsilon^2}{1-2\epsilon+\epsilon^2} - \frac{1-2\epsilon+\epsilon^2}{1-2\epsilon+\epsilon^2}}}
\label{_auto91} \tag{103}
\end{equation}
$$

<!-- Equation labels as ordinary links -->
<div id="_auto92"></div>

$$
\begin{equation}   = \pm c \sqrt{\frac{(1-\epsilon)^2}{2\epsilon}}
\label{_auto92} \tag{104}
\end{equation}
$$

Summing up, we have

$$
\delta = c
\\
\alpha = \pm c \sqrt{\frac{(1-\epsilon)^2}{1 + \epsilon^2}}
\\
\beta = \pm c \sqrt{\frac{(1-\epsilon)^2}{2\epsilon}}
$$

## Different Potential

Let us now try another potential, given by

$$
V(r) = \beta r,
$$

where $\beta$ is constant we assume is larger than zero. This type of potential has played an importan role in modeling confinement of quarks in non-relativistic models for the interactions among quarks, see for example <https://journals.aps.org/prl/pdf/10.1103/PhysRevLett.44.1369> 


Adding the angular momentum part, we obtain the effective potential

$$
V_{\mathrm{eff}}(r) = \beta r+\frac{L^2}{2\mu r^2},
$$

and taking the derivative with respect to $r$, we get the radial force

$$
F_r=-\frac{dV_{\mathrm{eff}}(r)}{dr} = -\beta+\frac{L^2}{\mu r^3}.
$$

It gives us in turn a radial acceleration $a_r$

$$
a_r= -\frac{\beta}{\mu}+\frac{L^2}{\mu^2 r^3}.
$$

This is the equation we need to include in our code. I have not been able to find out if there is an analytical solution to the above equation. If you can find one, there is a reward of $50$ USD to the first one who finds. Numerically life is very easy, we just define a new acceleration, as seen below.



First however, we plot the effective potential in order to get a feeling of what we may expect.

The following code plots this effective potential for a simple choice of parameters, with a potential $\beta r $. Here we have chosen $L=m=\beta=1$.

# Common imports
import numpy as np
from math import *
import matplotlib.pyplot as plt

Deltax = 0.01
#set up arrays
xinitial = 0.3
xfinal = 5.0
beta = 1.0   # spring constant
m = 1.0   # mass, you can change these
AngMom = 1.0  #  The angular momentum
n = ceil((xfinal-xinitial)/Deltax)
x = np.zeros(n)
for i in range(n):
    x[i] = xinitial+i*Deltax
V = np.zeros(n)
V = beta*x+0.5*AngMom*AngMom/(m*x*x)
# Plot potential
fig, ax = plt.subplots()
ax.set_xlabel('r[m]')
ax.set_ylabel('V[J]')
ax.plot(x, V)
fig.tight_layout()
plt.show()

We take now the derivative of the effective potential in order to find its minimum, that is

$$
\frac{dV_{\mathrm{eff}}(r)}{dr} = \beta-\frac{L^2}{\mu r^3}=0,
$$

which gives us $r_{\mathrm{min}}$

$$
r_{\mathrm{min}}=\left [\frac{L^2}{\beta \mu}\right ]^{1/3}.
$$

With the above choice of parameters this gives $r_{\mathrm{min}}=1$. 

In the code here we solve the equations of motion and find the time-evolution of the radius $r$.

DeltaT = 0.01
#set up arrays 
tfinal = 8.0
n = ceil(tfinal/DeltaT)
# set up arrays for t, v and r
t = np.zeros(n)
v = np.zeros(n)
r = np.zeros(n)
# Constants of the model, setting all variables to one for simplicity
beta = 1.0
AngMom = 1.0  #  The angular momentum
m = 1.0  # scale mass to one
c1 = AngMom*AngMom/(m*m)
c2 = AngMom*AngMom/m
rmin = (AngMom*AngMom/m/beta)**(1./3.)
# Initial conditions, place yourself at the potential min
r0 = rmin
v0 = 0.0  # starts at rest
r[0] = r0
v[0] = v0
# Start integrating using the Velocity-Verlet  method
for i in range(n-1):
    # Set up acceleration
    a = -beta+c1/(r[i]**3)
    # update velocity, time and position using the Velocity-Verlet method
    r[i+1] = r[i] + DeltaT*v[i]+0.5*(DeltaT**2)*a
    anew = -beta+c1/(r[i+1]**3)
    v[i+1] = v[i] + 0.5*DeltaT*(a+anew)
    t[i+1] = t[i] + DeltaT
#plotting
plt.xlabel('time')
plt.ylabel('radius')
plt.plot(t,r)
save_fig("LinearPotential")
plt.show()

We see that if we run with the initial condition corresponding to a circular orbit, our radius stays constant as function of time. 

What kind of orbits do we have here? Will it be bounded or unbounded?