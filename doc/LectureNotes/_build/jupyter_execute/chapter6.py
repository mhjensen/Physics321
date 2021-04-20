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



## Exercises


### The Earth-Sun System

We start with a simpler case first, the Earth-Sun system  in two dimensions only.  The gravitational force $F_G$ on the earth from the sun is

$$
\boldsymbol{F}_G=-\frac{GM_{\odot}M_E}{r^3}\boldsymbol{r},
$$

where $G$ is the gravitational constant,

$$
M_E=6\times 10^{24}\mathrm{Kg},
$$

the mass of Earth,

$$
M_{\odot}=2\times 10^{30}\mathrm{Kg},
$$

the mass of the Sun and

$$
r=1.5\times 10^{11}\mathrm{m},
$$

is the distance between Earth and the Sun. The latter defines what we call an astronomical unit **AU**.
From Newton's second law we have then for the $x$ direction

$$
\frac{d^2x}{dt^2}=-\frac{F_{x}}{M_E},
$$

and

$$
\frac{d^2y}{dt^2}=-\frac{F_{y}}{M_E},
$$

for the $y$ direction.

Here we will use  that  $x=r\cos{(\theta)}$, $y=r\sin{(\theta)}$ and

$$
r = \sqrt{x^2+y^2}.
$$

We can rewrite these equations

$$
F_{x}=-\frac{GM_{\odot}M_E}{r^2}\cos{(\theta)}=-\frac{GM_{\odot}M_E}{r^3}x,
$$

and

$$
F_{y}=-\frac{GM_{\odot}M_E}{r^2}\sin{(\theta)}=-\frac{GM_{\odot}M_E}{r^3}y,
$$

as four first-order coupled differential equations

$$
\frac{dv_x}{dt}=-\frac{GM_{\odot}}{r^3}x,
$$

and

$$
\frac{dx}{dt}=v_x,
$$

and

$$
\frac{dv_y}{dt}=-\frac{GM_{\odot}}{r^3}y,
$$

and

$$
\frac{dy}{dt}=v_y.
$$

The four coupled differential equations

$$
\frac{dv_x}{dt}=-\frac{GM_{\odot}}{r^3}x,
$$

and

$$
\frac{dx}{dt}=v_x,
$$

and

$$
\frac{dv_y}{dt}=-\frac{GM_{\odot}}{r^3}y,
$$

and

$$
\frac{dy}{dt}=v_y,
$$

can be turned into dimensionless equations or we can introduce astronomical units with $1$ AU = $1.5\times 10^{11}$. 

Using the equations from circular motion (with $r =1\mathrm{AU}$)

$$
\frac{M_E v^2}{r} = F = \frac{GM_{\odot}M_E}{r^2},
$$

we have

$$
GM_{\odot}=v^2r,
$$

and using that the velocity of Earth (assuming circular motion) is
$v = 2\pi r/\mathrm{yr}=2\pi\mathrm{AU}/\mathrm{yr}$, we have

$$
GM_{\odot}= v^2r = 4\pi^2 \frac{(\mathrm{AU})^3}{\mathrm{yr}^2}.
$$

The four coupled differential equations can then be discretized using Euler's method as (with step length $h$)

$$
v_{x,i+1}=v_{x,i}-h\frac{4\pi^2}{r_i^3}x_i,
$$

and

$$
x_{i+1}=x_i+hv_{x,i},
$$

and

$$
v_{y,i+1}=v_{y,i}-h\frac{4\pi^2}{r_i^3}y_i,
$$

and

$$
y_{i+1}=y_i+hv_{y,i},
$$

The code here implements Euler's method for the Earth-Sun system using a more compact way of representing the vectors. Alternatively, you could have spelled out all the variables $v_x$, $v_y$, $x$ and $y$ as one-dimensional arrays.

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


DeltaT = 0.01
#set up arrays 
tfinal = 10 # in years
n = ceil(tfinal/DeltaT)
# set up arrays for t, a, v, and x
t = np.zeros(n)
v = np.zeros((n,2))
r = np.zeros((n,2))
# Initial conditions as compact 2-dimensional arrays
r0 = np.array([1.0,0.0])
v0 = np.array([0.0,2*pi])
r[0] = r0
v[0] = v0
Fourpi2 = 4*pi*pi
# Start integrating using Euler's method
for i in range(n-1):
    # Set up the acceleration
    # Here you could have defined your own function for this
    rabs = sqrt(sum(r[i]*r[i]))
    a =  -Fourpi2*r[i]/(rabs**3)
    # update velocity, time and position using Euler's forward method
    v[i+1] = v[i] + DeltaT*a
    r[i+1] = r[i] + DeltaT*v[i]
    t[i+1] = t[i] + DeltaT
# Plot position as function of time    
fig, ax = plt.subplots()
#ax.set_xlim(0, tfinal)
ax.set_xlabel('x[AU]')
ax.set_ylabel('y[AU]')
ax.plot(r[:,0], r[:,1])
fig.tight_layout()
save_fig("EarthSunEuler")
plt.show()

We notice here that Euler's method doesn't give a stable orbit with for example $\Delta t =0.01$. It
means that we cannot trust Euler's method. Euler's method does not conserve energy. It is an
example of an integrator which is not
[symplectic](https://en.wikipedia.org/wiki/Symplectic_integrator).

Here we present thus two methods, which with simple changes allow us
to avoid these pitfalls. The simplest possible extension is the
so-called Euler-Cromer method.  The changes we need to make to our
code are indeed marginal here.  We need simply to replace

    r[i+1] = r[i] + DeltaT*v[i]

in the above code with the velocity at the new time $t_{i+1}$

    r[i+1] = r[i] + DeltaT*v[i+1]

By this simple caveat we get stable orbits.  Below we derive the
Euler-Cromer method as well as one of the most utlized algorithms for
solving the above type of problems, the so-called Velocity-Verlet
method.


Let us repeat Euler's method.
We have a differential equation

<!-- Equation labels as ordinary links -->
<div id="_auto19"></div>

$$
\begin{equation}
  y'(t_i)=f(t_i,y_i)   
\label{_auto19} \tag{31}
\end{equation}
$$

and if we truncate at the first derivative, we have from the Taylor expansion

<!-- Equation labels as ordinary links -->
<div id="eq:euler"></div>

$$
\begin{equation}
   y_{i+1}=y(t_i) + (\Delta t) f(t_i,y_i) + O(\Delta t^2), \label{eq:euler} \tag{32}
\end{equation}
$$

which when complemented with $t_{i+1}=t_i+\Delta t$ forms
the algorithm for the well-known Euler method. 
Note that at every step we make an approximation error
of the order of $O(\Delta t^2)$, however the total error is the sum over all
steps $N=(b-a)/(\Delta t)$ for $t\in [a,b]$, yielding thus a global error which goes like
$NO(\Delta t^2)\approx O(\Delta t)$. 

To make Euler's method more precise we can obviously
decrease $\Delta t$ (increase $N$), but this can lead to loss of numerical precision.
Euler's method is not recommended for precision calculation,
although it is handy to use in order to get a first
view on how a solution may look like.

Euler's method is asymmetric in time, since it uses information about the derivative at the beginning
of the time interval. This means that we evaluate the position at $y_1$ using the velocity
at $v_0$. A simple variation is to determine $x_{n+1}$ using the velocity at
$v_{n+1}$, that is (in a slightly more generalized form)

<!-- Equation labels as ordinary links -->
<div id="_auto20"></div>

$$
\begin{equation} 
   y_{n+1}=y_{n}+ v_{n+1}+O(\Delta t^2)
\label{_auto20} \tag{33}
\end{equation}
$$

and

<!-- Equation labels as ordinary links -->
<div id="_auto21"></div>

$$
\begin{equation}
   v_{n+1}=v_{n}+(\Delta t) a_{n}+O(\Delta t^2).
\label{_auto21} \tag{34}
\end{equation}
$$

The acceleration $a_n$ is a function of $a_n(y_n, v_n, t_n)$ and needs to be evaluated
as well. This is the Euler-Cromer method. It is easy to change the above code and see that with the same 
time step we get stable results.


Let us stay with $x$ (position) and $v$ (velocity) as the quantities we are interested in.

We have the Taylor expansion for the position given by

$$
x_{i+1} = x_i+(\Delta t)v_i+\frac{(\Delta t)^2}{2}a_i+O((\Delta t)^3).
$$

The corresponding expansion for the velocity is

$$
v_{i+1} = v_i+(\Delta t)a_i+\frac{(\Delta t)^2}{2}v^{(2)}_i+O((\Delta t)^3).
$$

Via Newton's second law we have normally an analytical expression for the derivative of the velocity, namely

$$
a_i= \frac{d^2 x}{dt^2}\vert_{i}=\frac{d v}{dt}\vert_{i}= \frac{F(x_i,v_i,t_i)}{m}.
$$

If we add to this the corresponding expansion for the derivative of the velocity

$$
v^{(1)}_{i+1} = a_{i+1}= a_i+(\Delta t)v^{(2)}_i+O((\Delta t)^2)=a_i+(\Delta t)v^{(2)}_i+O((\Delta t)^2),
$$

and retain only terms up to the second derivative of the velocity since our error goes as $O(h^3)$, we have

$$
(\Delta t)v^{(2)}_i\approx a_{i+1}-a_i.
$$

We can then rewrite the Taylor expansion for the velocity as

$$
v_{i+1} = v_i+\frac{(\Delta t)}{2}\left( a_{i+1}+a_{i}\right)+O((\Delta t)^3).
$$

Our final equations for the position and the velocity become then

$$
x_{i+1} = x_i+(\Delta t)v_i+\frac{(\Delta t)^2}{2}a_{i}+O((\Delta t)^3),
$$

and

$$
v_{i+1} = v_i+\frac{(\Delta t)}{2}\left(a_{i+1}+a_{i}\right)+O((\Delta t)^3).
$$

Note well that the term $a_{i+1}$ depends on the position at $x_{i+1}$. This means that you need to calculate 
the position at the updated time $t_{i+1}$ before the computing the next velocity.  Note also that the derivative of the velocity at the time
$t_i$ used in the updating of the position can be reused in the calculation of the velocity update as well. 

We can now easily add the Verlet method to our original code as

DeltaT = 0.01
#set up arrays 
tfinal = 10
n = ceil(tfinal/DeltaT)
# set up arrays for t, a, v, and x
t = np.zeros(n)
v = np.zeros((n,2))
r = np.zeros((n,2))
# Initial conditions as compact 2-dimensional arrays
r0 = np.array([1.0,0.0])
v0 = np.array([0.0,2*pi])
r[0] = r0
v[0] = v0
Fourpi2 = 4*pi*pi
# Start integrating using the Velocity-Verlet  method
for i in range(n-1):
    # Set up forces, air resistance FD, note now that we need the norm of the vecto
    # Here you could have defined your own function for this
    rabs = sqrt(sum(r[i]*r[i]))
    a =  -Fourpi2*r[i]/(rabs**3)
    # update velocity, time and position using the Velocity-Verlet method
    r[i+1] = r[i] + DeltaT*v[i]+0.5*(DeltaT**2)*a
    rabs = sqrt(sum(r[i+1]*r[i+1]))
    anew = -4*(pi**2)*r[i+1]/(rabs**3)
    v[i+1] = v[i] + 0.5*DeltaT*(a+anew)
    t[i+1] = t[i] + DeltaT
# Plot position as function of time    
fig, ax = plt.subplots()
ax.set_xlabel('x[AU]')
ax.set_ylabel('y[AU]')
ax.plot(r[:,0], r[:,1])
fig.tight_layout()
save_fig("EarthSunVV")
plt.show()

You can easily generalize the calculation of the forces by defining a function
which takes in as input the various variables. We leave this as a challenge to you.

Running the above code for various time steps we see that the Velocity-Verlet is fully stable for various time steps.

We can also play around with different initial conditions in order to find the escape velocity from an orbit around the sun with distance one astronomical unit, 1 AU. The theoretical value for the escape velocity, is given by

$$
v = \sqrt{8\pi^2}{r},
$$

and with $r=1$ AU, this means that the escape velocity is $2\pi\sqrt{2}$ AU/yr. To obtain this we required that the kinetic energy of Earth equals the potential energy given by the gravitational force.

Setting

$$
\frac{1}{2}M_{\mathrm{Earth}}v^2=\frac{GM_{\odot}}{r},
$$

and with $GM_{\odot}=4\pi^2$ we obtain the above relation for the velocity. Setting an initial velocity say equal to $9$ in the above code, yields a planet (Earth) which escapes a stable orbit around the sun, as seen by running the code here.

DeltaT = 0.01
#set up arrays 
tfinal = 100
n = ceil(tfinal/DeltaT)
# set up arrays for t, a, v, and x
t = np.zeros(n)
v = np.zeros((n,2))
r = np.zeros((n,2))
# Initial conditions as compact 2-dimensional arrays
r0 = np.array([1.0,0.0])
# setting initial velocity larger than escape velocity
v0 = np.array([0.0,9.0])
r[0] = r0
v[0] = v0
Fourpi2 = 4*pi*pi
# Start integrating using the Velocity-Verlet  method
for i in range(n-1):
    # Set up forces, air resistance FD, note now that we need the norm of the vecto
    # Here you could have defined your own function for this
    rabs = sqrt(sum(r[i]*r[i]))
    a =  -Fourpi2*r[i]/(rabs**3)
    # update velocity, time and position using the Velocity-Verlet method
    r[i+1] = r[i] + DeltaT*v[i]+0.5*(DeltaT**2)*a
    rabs = sqrt(sum(r[i+1]*r[i+1]))
    anew = -4*(pi**2)*r[i+1]/(rabs**3)
    v[i+1] = v[i] + 0.5*DeltaT*(a+anew)
    t[i+1] = t[i] + DeltaT
# Plot position as function of time    
fig, ax = plt.subplots()
ax.set_xlabel('x[AU]')
ax.set_ylabel('y[AU]')
ax.plot(r[:,0], r[:,1])
fig.tight_layout()
save_fig("EscapeEarthSunVV")
plt.show()

### Testing Energy conservation

The code here implements Euler's method for the Earth-Sun system using
a more compact way of representing the vectors. Alternatively, you
could have spelled out all the variables $v_x$, $v_y$, $x$ and $y$ as
one-dimensional arrays.  It tests conservation of potential and
kinetic energy as functions of time, in addition to the total energy,
again as function of time

**Note**: in all codes we have used scaled equations so that the gravitational constant times the mass of the sum is given by $4\pi^2$ and the mass of the earth is set to **one** in the calculations of kinetic and potential energies. Else, we would get very large results.

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

# Initial values, time step, positions and velocites

DeltaT = 0.0001
#set up arrays 
tfinal = 100 # in years
n = ceil(tfinal/DeltaT)
# set up arrays for t, a, v, and x
t = np.zeros(n)
v = np.zeros((n,2))
r = np.zeros((n,2))

# setting up the kinetic, potential and total energy, note only functions of time
EKinetic = np.zeros(n)
EPotential = np.zeros(n)
ETotal = np.zeros(n)

# Initial conditions as compact 2-dimensional arrays


r0 = np.array([1.0,0.0])
v0 = np.array([0.0,2*pi])
r[0] = r0
v[0] = v0
Fourpi2 = 4*pi*pi
# Setting up variables for the calculation of energies
#  distance that defines rabs in potential energy
rabs0 = sqrt(sum(r[0]*r[0]))
#  Initial kinetic energy. Note that we skip the mass of the Earth here, that is MassEarth=1 in all codes
EKinetic[0] = 0.5*sum(v0*v0)
#  Initial potential energy  (note negative sign, why?)
EPotential[0] = -4*pi*pi/rabs0
#  Initial total energy 
ETotal[0] = EPotential[0]+EKinetic[0]
# Start integrating using Euler's method
for i in range(n-1):
    # Set up the acceleration
    # Here you could have defined your own function for this
    rabs = sqrt(sum(r[i]*r[i]))
    a =  -Fourpi2*r[i]/(rabs**3)
    # update Energies, velocity, time and position using Euler's forward method
    v[i+1] = v[i] + DeltaT*a
    r[i+1] = r[i] + DeltaT*v[i]
    t[i+1] = t[i] + DeltaT
    EKinetic[i+1] = 0.5*sum(v[i+1]*v[i+1])
    EPotential[i+1] = -4*pi*pi/sqrt(sum(r[i+1]*r[i+1]))
    ETotal[i+1] = EPotential[i+1]+EKinetic[i+1]
# Plot energies as functions of time    

fig, axs = plt.subplots(3, 1)
axs[0].plot(t, EKinetic)
axs[0].set_xlim(0, tfinal)
axs[0].set_ylabel('Kinetic energy')
axs[1].plot(t, EPotential)
axs[1].set_ylabel('Potential Energy')
axs[2].plot(t, ETotal)
axs[2].set_xlabel('Time [yr]')
axs[2].set_ylabel('Total Energy')
fig.tight_layout()
save_fig("EarthSunEuler")
plt.show()

We see very clearly that Euler's method does not conserve energy!! Try to reduce the time step $\Delta t$. What do you see?


With the Euler-Cromer method, the only thing we need is to update the
position at a time $t+1$ with the update velocity from the same
time. Thus, the change in the code is extremely simply, and **energy is
suddenly conserved**. Note that the error runs like $O(\Delta t)$ and
this is why we see the larger oscillations. But within this
oscillating energy envelope, we see that the energies swing between a
max and a min value and never exceed these values.

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

# Initial values, time step, positions and velocites

DeltaT = 0.0001
#set up arrays 
tfinal = 100 # in years
n = ceil(tfinal/DeltaT)
# set up arrays for t, a, v, and x
t = np.zeros(n)
v = np.zeros((n,2))
r = np.zeros((n,2))

# setting up the kinetic, potential and total energy, note only functions of time
EKinetic = np.zeros(n)
EPotential = np.zeros(n)
ETotal = np.zeros(n)

# Initial conditions as compact 2-dimensional arrays


r0 = np.array([1.0,0.0])
v0 = np.array([0.0,2*pi])
r[0] = r0
v[0] = v0
Fourpi2 = 4*pi*pi
# Setting up variables for the calculation of energies
#  distance that defines rabs in potential energy
rabs0 = sqrt(sum(r[0]*r[0]))
#  Initial kinetic energy. Note that we skip the mass of the Earth here, that is MassEarth=1 in all codes
EKinetic[0] = 0.5*sum(v0*v0)
#  Initial potential energy 
EPotential[0] = -4*pi*pi/rabs0
#  Initial total energy 
ETotal[0] = EPotential[0]+EKinetic[0]
# Start integrating using Euler's method
for i in range(n-1):
    # Set up the acceleration
    # Here you could have defined your own function for this
    rabs = sqrt(sum(r[i]*r[i]))
    a =  -Fourpi2*r[i]/(rabs**3)
    # update velocity, time and position using Euler's forward method
    v[i+1] = v[i] + DeltaT*a
#   Only change when we add the Euler-Cromer method    
    r[i+1] = r[i] + DeltaT*v[i+1]
    t[i+1] = t[i] + DeltaT
    EKinetic[i+1] = 0.5*sum(v[i+1]*v[i+1])
    EPotential[i+1] = -4*pi*pi/sqrt(sum(r[i+1]*r[i+1]))
    ETotal[i+1] = EPotential[i+1]+EKinetic[i+1]
# Plot energies as functions of time    

fig, axs = plt.subplots(3, 1)
axs[0].plot(t, EKinetic)
axs[0].set_xlim(0, tfinal)
axs[0].set_ylabel('Kinetic energy')
axs[1].plot(t, EPotential)
axs[1].set_ylabel('Potential Energy')
axs[2].plot(t, ETotal)
axs[2].set_xlabel('Time [yr]')
axs[2].set_ylabel('Total Energy')
fig.tight_layout()
save_fig("EarthSunEulerCromer")
plt.show()

### Adding the  velocity Verlet method

Our final equations for the position and the velocity become then

$$
x_{i+1} = x_i+(\Delta t)v_i+\frac{(\Delta t)^2}{2}a_{i}+O((\Delta t)^3),
$$

and

$$
v_{i+1} = v_i+\frac{(\Delta t)}{2}\left(a_{i+1}+a_{i}\right)+O((\Delta t)^3).
$$

Note well that the term $a_{i+1}$ depends on the position at $x_{i+1}$. This means that you need to calculate 
the position at the updated time $t_{i+1}$ before the computing the next velocity.  Note also that the derivative of the velocity at the time
$t_i$ used in the updating of the position can be reused in the calculation of the velocity update as well. 



We can now easily add the Verlet method to our original code as

DeltaT = 0.001
#set up arrays 
tfinal = 100
n = ceil(tfinal/DeltaT)
# set up arrays for t, a, v, and x
t = np.zeros(n)
v = np.zeros((n,2))
r = np.zeros((n,2))
# Initial conditions as compact 2-dimensional arrays
r0 = np.array([1.0,0.0])
v0 = np.array([0.0,2*pi])
r[0] = r0
v[0] = v0
Fourpi2 = 4*pi*pi

# setting up the kinetic, potential and total energy, note only functions of time
EKinetic = np.zeros(n)
EPotential = np.zeros(n)
ETotal = np.zeros(n)

# Setting up variables for the calculation of energies
#  distance that defines rabs in potential energy
rabs0 = sqrt(sum(r[0]*r[0]))
#  Initial kinetic energy. Note that we skip the mass of the Earth here, that is MassEarth=1 in all codes
EKinetic[0] = 0.5*sum(v0*v0)
#  Initial potential energy 
EPotential[0] = -4*pi*pi/rabs0
#  Initial total energy 
ETotal[0] = EPotential[0]+EKinetic[0]

# Start integrating using the Velocity-Verlet  method
for i in range(n-1):
    # Set up forces, air resistance FD, note now that we need the norm of the vecto
    # Here you could have defined your own function for this
    rabs = sqrt(sum(r[i]*r[i]))
    a =  -Fourpi2*r[i]/(rabs**3)
    # update velocity, time and position using the Velocity-Verlet method
    r[i+1] = r[i] + DeltaT*v[i]+0.5*(DeltaT**2)*a
    rabs = sqrt(sum(r[i+1]*r[i+1]))
    anew = -4*(pi**2)*r[i+1]/(rabs**3)
    v[i+1] = v[i] + 0.5*DeltaT*(a+anew)
    t[i+1] = t[i] + DeltaT
    EKinetic[i+1] = 0.5*sum(v[i+1]*v[i+1])
    EPotential[i+1] = -4*pi*pi/sqrt(sum(r[i+1]*r[i+1]))
    ETotal[i+1] = EPotential[i+1]+EKinetic[i+1]
# Plot energies as functions of time    

fig, axs = plt.subplots(3, 1)
axs[0].plot(t, EKinetic)
axs[0].set_xlim(0, tfinal)
axs[0].set_ylabel('Kinetic energy')
axs[1].plot(t, EPotential)
axs[1].set_ylabel('Potential Energy')
axs[2].plot(t, ETotal)
axs[2].set_xlabel('Time [yr]')
axs[2].set_ylabel('Total Energy')
fig.tight_layout()
save_fig("EarthSunVelocityVerlet")
plt.show()

And we see that due to the smaller truncation error that energy conservation is improved as a function of time.
Try out different time steps $\Delta t$ and see if the results improve or worsen.





### Exercise: Center-of-Mass and Relative Coordinates and Reference Frames

We define the two-body center-of-mass coordinate and relative coordinate by expressing the trajectories for
$\boldsymbol{r}_1$ and $\boldsymbol{r}_2$ into the center-of-mass coordinate
$\boldsymbol{R}_{\rm cm}$

$$
\boldsymbol{R}_{\rm cm}\equiv\frac{m_1\boldsymbol{r}_1+m_2\boldsymbol{r}_2}{m_1+m_2},
$$

and the relative coordinate

$$
\boldsymbol{r}\equiv\boldsymbol{r}_1-\boldsymbol{r_2}.
$$

Here, we assume the two particles interact only with one another, so $\boldsymbol{F}_{12}=-\boldsymbol{F}_{21}$ (where $\boldsymbol{F}_{ij}$ is the force on $i$ due to $j$.

* 2a (5pt) Show that the equations of motion then become $\ddot{\boldsymbol{R}}_{\rm cm}=0$ and $\mu\ddot{\boldsymbol{r}}=\boldsymbol{F}_{12}$, with the reduced mass $\mu=m_1m_2/(m_1+m_2)$.

The first expression simply states that the center of mass coordinate $\boldsymbol{R}_{\rm cm}$ moves at a fixed velocity. The second expression can be rewritten in terms of the reduced mass $\mu$.

Let us first start with some basic definitions. We have the center of mass coordinate $\boldsymbol{R}$ defined as (for two particles)

$$
\boldsymbol{R}=\frac{m_1\boldsymbol{r}_1+m_2\boldsymbol{r}_2}{M},
$$

where $m_1$ and $m_2$ are the masses of the two objects and $\boldsymbol{r}_1$ and $\boldsymbol{r}_2$ their respective positions defined according to a chosen origin. Here $M=m_1+m_2$ is the total mass.

The relative position is defined as

$$
\boldsymbol{r} =\boldsymbol{r}_1-\boldsymbol{r}_2,
$$

and we then define $\boldsymbol{r}_1$ and $\boldsymbol{r}_2$ in terms of the relative and center of mass positions as

$$
\boldsymbol{r}_1=\boldsymbol{R}+\frac{m_2}{M}\boldsymbol{r},
$$

and

$$
\boldsymbol{r}_2=\boldsymbol{R}-\frac{m_1}{M}\boldsymbol{r},
$$

The total linear momentum is then defined as

$$
\boldsymbol{P}=\sum_{i=1}^Nm_i\frac{\boldsymbol{r}_i}{dt},
$$

where $N=2$ in our case. With the above definition of the center of mass position, we see that we can rewrite the total linear momentum as (multiplying the center of mass position with $M$)

$$
\boldsymbol{P}=M\frac{d\boldsymbol{R}}{dt}=M\dot{\boldsymbol{R}}.
$$

This result is also an answer to a part of exercise 2b, see below.

The net force acting on the system is given by the time derivative of the linear momentum (assuming mass is time independent)
and we have

$$
\boldsymbol{F}^{\mathrm{net}}=\dot{\boldsymbol{P}}=M\ddot{\boldsymbol{R}}.
$$

The net force acting on the system is given by the sum of the forces acting on the two object, that is we have

$$
\boldsymbol{F}^{\mathrm{net}}=\boldsymbol{F}_1+\boldsymbol{F}_2=\dot{\boldsymbol{P}}=M\ddot{\boldsymbol{R}}.
$$

In our case the forces are given by the internal forces only. The force acting on object $1$ is thus $\boldsymbol{F}_{12}$ and the one acting on object $2$ is $\boldsymbol{F}_{12}$. We have also defined that $\boldsymbol{F}_{12}=-\boldsymbol{F}_{21}$. This means thar we have

$$
\boldsymbol{F}_1+\boldsymbol{F}_2=\boldsymbol{F}_{12}+\boldsymbol{F}_{21}=0=\dot{\boldsymbol{P}}=M\ddot{\boldsymbol{R}},
$$

which is what we wanted to show. The center of mass velocity is thus a constant of the motion. We could also define the so-called center of mass reference frame where we simply set $\boldsymbol{R}=0$.

This has also another important consequence for our forces. If we assume that our force depends only on the positions, it means that the gradient of the potential with respect to the center of mass position is zero, that is

$$
M\ddot{d\boldsymbol{R}}=-\boldsymbol{\nabla}_{\boldsymbol{R}}V =0!
$$

An alternative way is

$$
\begin{eqnarray}
\ddot{\boldsymbol{R}}_{\rm cm}&=&\frac{1}{m_1+m_2}\left\{m_1\ddot{\boldsymbol{r}}_1+m_2\ddot{\boldsymbol{r}}_2\right\}\\
\nonumber
&=&\frac{1}{m_1+m_2}\left\{\boldsymbol{F}_{12}+\boldsymbol{F}_{21}\right\}=0.\\
\ddot{\boldsymbol{r}}&=&\ddot{\boldsymbol{r}}_1-\ddot{\boldsymbol{r}}_2=\left(\frac{\boldsymbol{F}_{12}}{m_1}-\frac{\boldsymbol{F}_{21}}{m_2}\right)\\
\nonumber
&=&\left(\frac{1}{m_1}+\frac{1}{m_2}\right)\boldsymbol{F}_{12}.
\end{eqnarray}
$$

The first expression simply states that the center of mass coordinate
$\boldsymbol{R}_{\rm cm}$ moves at a fixed velocity. The second expression
can be rewritten in terms of the reduced mass $\mu$.

$$
\begin{eqnarray}
\mu \ddot{\boldsymbol{r}}&=&\boldsymbol{F}_{12},\\
\frac{1}{\mu}&=&\frac{1}{m_1}+\frac{1}{m_2},~~~~\mu=\frac{m_1m_2}{m_1+m_2}.
\end{eqnarray}
$$

Thus, one can treat the trajectory as a one-body problem where the
reduced mass is $\mu$, and a second trivial problem for the center of
mass. The reduced mass is especially convenient when one is
considering gravitational problems, as we have seen during the lectures of weeks 11-13.




* 2b (5pt) Show that the linear momenta for the center-of-mass $\boldsymbol{P}$ motion and the relative motion $\boldsymbol{q}$ are given by $\boldsymbol{P}=M\dot{\boldsymbol{R}}_{\rm cm}$ with $M=m_1+m_2$ and $\boldsymbol{q}=\mu\dot{\boldsymbol{r}}$.  The linear momentum of the relative motion is defined $\boldsymbol{q} = (m_2\boldsymbol{p}_1-m_1\boldsymbol{p}_2)/(m_1+m_2)$.

In 2a we showed, as an intermediate step that the total linear momentum is given by

$$
\boldsymbol{P}=\sum_{i=1}^Nm_i\frac{d\boldsymbol{r}_i}{dt}=M\dot{\boldsymbol{R}}.
$$

For the relative momentum $\boldsymbol{q}$, we have that the time derivative of $\boldsymbol{r}$ is

$$
\dot{\boldsymbol{r}} =\dot{\boldsymbol{r}}_1-\dot{\boldsymbol{r}}_2,
$$

We now also that the momenta $\boldsymbol{p}_1=m_1\dot{\boldsymbol{r}}_1$ and
$\boldsymbol{p}_2=m_2\dot{\boldsymbol{r}}_2$. Using these expressions we can rewrite

$$
\dot{\boldsymbol{r}} =\frac{\boldsymbol{p}_1}{m_1}-\frac{\boldsymbol{p}_2}{m_2},
$$

which we can rewrite as

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

When we introduce the Lagrangian formalism we will see that it is much easier to derive these equations.

* 2c (5pt) Show then that the  kinetic energy for two objects can then be written as

$$
K=\frac{P^2}{2M}+\frac{q^2}{2\mu}.
$$

Here we just need to use our definitions of kinetic energy in terms of the coordinates $\boldsymbol{r}_1$ and $\boldsymbol{r}_2$.

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

we obtain (after squaring the expressions for $\dot{\boldsymbol{r}}_1$ and $\dot{\boldsymbol{r}}_2$) we have

$$
K=\frac{(m_1+m_2)\dot{\boldsymbol{R}}^2}{2}+\frac{(m_1+m_2)m_1m_2\dot{\boldsymbol{r}}^2}{2M^2},
$$

which we simplify to

$$
K=\frac{\dot{\boldsymbol{P}}^2}{2M}+\frac{\mu\dot{\boldsymbol{q}}^2}{2},
$$

which is what we wanted to show.

* 2d (5pt) Show that the total angular momentum for two-particles in the center-of-mass frame $\boldsymbol{R}=0$, is given by

$$
\boldsymbol{L}=\boldsymbol{r}\times \mu\dot{\boldsymbol{r}}.
$$

Here we need again that

$$
\boldsymbol{r} =\boldsymbol{r}_1-\boldsymbol{r}_2,
$$

and we then define $\boldsymbol{r}_1$ and $\boldsymbol{r}_2$ in terms of the relative and center of mass positions with $\boldsymbol{R}=0$

$$
\boldsymbol{r}_1=\frac{m_2}{M}\boldsymbol{r},
$$

and

$$
\boldsymbol{r}_2=-\frac{m_1}{M}\boldsymbol{r},
$$

The angular momentum (the total one) is the sum of the individual angular momenta (see homework 4) and we have

$$
\boldsymbol{L} = \boldsymbol{r}_1 \times \boldsymbol{p}_1+\boldsymbol{r}_2 \times \boldsymbol{p}_2,
$$

and using that $m_1\dot{\boldsymbol{r}}_1=\boldsymbol{p}_1$ and $m_2\dot{\boldsymbol{r}}_2=\boldsymbol{p}_2$ we have

$$
\boldsymbol{L} = m_1\boldsymbol{r}_1 \times \dot{\boldsymbol{r}}_1+m_2\boldsymbol{r}_2 \times \dot{\boldsymbol{r}}_2.
$$

Inserting the equations for $\boldsymbol{r}_1$ and $\boldsymbol{r}_2$ in terms of the relative motion, we have

$$
\boldsymbol{L} = m_1 \frac{m_2}{M}\boldsymbol{r}\times\frac{m_2}{M}\boldsymbol{r} +m_2 \frac{m_1}{M}\boldsymbol{r} \times \frac{m_1}{M}\dot{\boldsymbol{r}}.
$$

We see that can rewrite this equation as

$$
\boldsymbol{L}=\boldsymbol{r}\times \mu\dot{\boldsymbol{r}},
$$

which is what we wanted to derive.




### Exercise: Conservation of Energy

The equations of motion in the center-of-mass frame in two dimensions with $x=r\cos{(\phi)}$ and $y=r\sin{(\phi)}$ and
$r\in [0,\infty)$, $\phi\in [0,2\pi]$ and $r=\sqrt{x^2+y^2}$ are given by

$$
\mu \ddot{r}=-\frac{dV(r)}{dr}+\mu r\dot{\phi}^2,
$$

and

$$
\dot{\phi}=\frac{L}{\mu r^2}.
$$

Here $V(r)$ is any central force which depends only on the relative coordinate.
* 1a (5pt) Show that you can rewrite the radial equation in terms of an effective potential $V_{\mathrm{eff}}(r)=V(r)+L^2/(2\mu r^2)$. 

Here we use that

$$
\dot{\phi}=\frac{L}{\mu r^2}.
$$

and rewrite the above equation of motion as

$$
\mu \ddot{r}=-\frac{dV(r)}{dr}+\frac{L^2}{\mu r^3}.
$$

If we now define an effective potential

$$
V_{\mathrm{eff}}=V(r)+\frac{L^2}{2\mu r^2},
$$

we can rewrite our equation of motion in terms of

$$
\mu \ddot{r}=-\frac{dV_{\mathrm{eff}}(r)}{dr}=-\frac{dV(r)}{dr}+\frac{L^2}{\mu r^3}.
$$

The addition due to the angular momentum comes from the kinetic energy
when we rewrote it in terms of polar coordinates. It introduces a
so-called centrifugal barrier due to the angular momentum. This
centrifugal barrier pushes the object farther away from the origin.

Alternatively,

<!-- Equation labels as ordinary links -->
<div id="_auto22"></div>

$$
\begin{equation}
-\frac{dV_{\text{eff}}(r)}{dr} = \mu \ddot{r}  =-\frac{dV(r)}{dr}+\mu\dot{\phi}^2r
\label{_auto22} \tag{35}
\end{equation}
$$

<!-- Equation labels as ordinary links -->
<div id="_auto23"></div>

$$
\begin{equation} 
-\frac{dV_{\text{eff}}(r)}{dr}  = -\frac{dV(r)}{dr}+\mu\left( \frac{L}{\mu r^2}\right) ^2r
\label{_auto23} \tag{36}
\end{equation}
$$

<!-- Equation labels as ordinary links -->
<div id="_auto24"></div>

$$
\begin{equation} 
 = -\frac{dV(r)}{dr}+\mu\frac{L^2}{\mu}r^{-3}
\label{_auto24} \tag{37}
\end{equation}
$$

<!-- Equation labels as ordinary links -->
<div id="_auto25"></div>

$$
\begin{equation} 
 = -\frac{d\left(  V(r)+\frac{1}{2} \frac{L^2}{\mu r^2}\right) }{dr}.
\label{_auto25} \tag{38}
\end{equation}
$$

Integrating we obtain

<!-- Equation labels as ordinary links -->
<div id="_auto26"></div>

$$
\begin{equation}
V_{\text{eff}}(r) = V(r) + \frac{L^2}{2\mu r^2} + C
\label{_auto26} \tag{39}
\end{equation}
$$

Imposing  the extra condition that $V_{\text{eff}}(r\rightarrow \infty) = V(r\rightarrow \infty)$,

<!-- Equation labels as ordinary links -->
<div id="_auto27"></div>

$$
\begin{equation}
V_{\text{eff}}(r) = V(r) + \frac{L^2}{2\mu r^2}
\label{_auto27} \tag{40}
\end{equation}
$$

Write out the final differential equation for the radial degrees of freedom when we specify that $V(r)=-\alpha/r$.  Plot the effective potential. You can choose values for $\alpha$ and $L$ and discuss (see Taylor section 8.4 and example 8.2) the physics of the system for two energies, one larger than zero and one smaller than zero. This is similar to what you did in the first midterm, except that the potential is different.

We insert now the explicit potential form $V(r)=-\alpha/r$. This gives us the following equation of motion

$$
\mu \ddot{r}=-\frac{dV_{\mathrm{eff}}(r)}{dr}=-\frac{d(-\alpha/r)}{dr}+\frac{L^2}{\mu r^3}=-\frac{\alpha}{r^2}+\frac{L^2}{\mu r^3}.
$$

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

If we select a potential energy below zero (and not necessarily one
which corresponds to the minimum point), the object will oscillate
between two values of $r$, a value $r_{\mathrm{min}}$ and a value
$r_{\mathrm{max}}$. We can assume that for example the kinetic energy
is zero at these two points. The object will thus oscillate back and
forth between these two points. As we will see in connection with the
solution of the equations of motion, this case corresponds to
elliptical orbits. If we select $r$ equal to the minimum of the
potential and use initial conditions for the velocity that correspond
to circular motion, the object will have a constant value of $r$ given
by the value at the minimum and the orbit is a circle.

If we select a potential energy larger than zero, then, since the
kinetic energy is always larger or equal to zero, the object will move
away from the origin. See also the discussion in Taylor, sections 8.4-8.6.

### Exercise: Harmonic oscillator again

Consider a particle of mass $m$ in a $2$-dimensional harmonic oscillator with potential

$$
V(r)=\frac{1}{2}kr^2=\frac{1}{2}k(x^2+y^2).
$$

We assume the orbit has a final non-zero angular momentum $L$.  The
effective potential looks like that of a harmonic oscillator for large
$r$, but for small $r$, the centrifugal potential repels the particle
from the origin. The combination of the two potentials has a minimum
for at some radius $r_{\rm min}$.


Set up the effective potential and plot it. Find $r_{\rm min}$ and $\dot{\phi}$. Show that the latter is given by $\dot{\phi}=\sqrt{k/m}$.  At $r_{\rm min}$ the particle does not accelerate and $r$ stays constant and the motion is circular. With fixed $k$ and $m$, which parameter can we adjust to change the value of $r$ at $r_{\rm min}$?

We consider the effective potential. The radius of a circular orbit is at the minimum of the potential (where the effective force is zero).
The potential is plotted here with the parameters $k=m=1.0$ and $L=1.0$.

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

We have an effective potential

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
\dot{\theta}&=&\frac{L}{mr_{\rm min}^2}=\sqrt{k/m}.
\end{eqnarray*}
$$

For particles at $r_{\rm min}$ with $\dot{r}=0$, the particle does not
accelerate and $r$ stays constant, i.e. a circular orbit. The radius
of the circular orbit can be adjusted by changing the angular momentum
$L$.

For the above parameters this minimum is at $r_{\rm min}=1$.



Now consider small vibrations about $r_{\rm min}$. The effective spring constant is the curvature of the effective potential.  Use the curvature at $r_{\rm min}$ to find the effective spring constant (hint, look at  exercise 4 in homework 6) $k_{\mathrm{eff}}$. Show also that $\omega=\sqrt{k_{\mathrm{eff}}/m}=2\dot{\phi}$

$$
\begin{eqnarray*}
k_{\rm eff}&=&\left.\frac{d^2}{dr^2}V_{\rm eff}(r)\right|_{r=r_{\rm min}}=k+\frac{3L^2}{mr_{\rm min}^4}\\
&=&4k,\\
\omega&=&\sqrt{k_{\rm eff}/m}=2\sqrt{k/m}=2\dot{\theta}.
\end{eqnarray*}
$$

Because the radius oscillates with twice the angular frequency,
the orbit has two places where $r$ reaches a minimum in one
cycle. This differs from the inverse-square force where there is one
minimum in an orbit. One can show that the orbit for the harmonic
oscillator is also elliptical, but in this case the center of the
potential is at the center of the ellipse, not at one of the foci.




The solution to the equations of motion in Cartesian coordinates is simple. The $x$ and $y$ equations of motion separate, and we have $\ddot{x}=-kx/m$ and $\ddot{y}=-ky/m$. The harmonic oscillator is indeed a system where the degrees of freedom separate and we can find analytical solutions. Define a natural frequency $\omega_0=\sqrt{k/m}$ and show that (where $A$, $B$, $C$ and $D$ are arbitrary constants defined by the initial conditions)

$$
\begin{eqnarray*}
x&=&A\cos\omega_0 t+B\sin\omega_0 t,\\
y&=&C\cos\omega_0 t+D\sin\omega_0 t.
\end{eqnarray*}
$$

The solution is also simple to write down exactly in Cartesian coordinates. The $x$ and $y$ equations of motion separate,

$$
\begin{eqnarray*}
\ddot{x}&=&-kx,\\
\ddot{y}&=&-ky.
\end{eqnarray*}
$$

We know from our studies of the harmonic oscillator that the general solution can be expressed as

$$
\begin{eqnarray*}
x&=&A\cos\omega_0 t+B\sin\omega_0 t,\\
y&=&C\cos\omega_0 t+D\sin\omega_0 t.
\end{eqnarray*}
$$

With the solutions for $x$ and $y$, and $r^2=x^2+y^2$ and the definitions $\alpha=\frac{A^2+B^2+C^2+D^2}{2}$, $\beta=\frac{A^2-B^2+C^2-D^2}{2}$ and $\gamma=AB+CD$, show that

$$
r^2=\alpha+(\beta^2+\gamma^2)^{1/2}\cos(2\omega_0 t-\delta),
$$

with

$$
\delta=\arctan(\gamma/\beta).
$$

We start with $r^2 & = x^2+y^2$ and square the above analytical solutions and   after some **exciting algebraic manipulations** we arrive at

<!-- Equation labels as ordinary links -->
<div id="_auto28"></div>

$$
\begin{equation}
r^2  = x^2+y^2
\label{_auto28} \tag{41}
\end{equation}
$$

<!-- Equation labels as ordinary links -->
<div id="_auto29"></div>

$$
\begin{equation}  
 = \left(  A\cos\omega_0 t+B\sin\omega_0 t\right) ^2 + \left(  C\cos\omega_0 t+D\sin\omega_0 t\right) ^2
\label{_auto29} \tag{42}
\end{equation}
$$

<!-- Equation labels as ordinary links -->
<div id="_auto30"></div>

$$
\begin{equation}  
 = A^2\cos^2\omega_0 t+B^2\sin^2\omega_0 t + 2AB\sin\omega_0 t \cos\omega_0 t + C^2\cos^2\omega_0 t+D^2\sin^2\omega_0 t + 2CD\sin\omega_0 t \cos\omega_0 t
\label{_auto30} \tag{43}
\end{equation}
$$

<!-- Equation labels as ordinary links -->
<div id="_auto31"></div>

$$
\begin{equation} 
 = (A^2+C^2)\cos^2\omega_0 t + (B^2+D^2)\sin^2\omega_0 t + 2(AC + BD)\sin\omega_0 t \cos\omega_0 t
\label{_auto31} \tag{44}
\end{equation}
$$

<!-- Equation labels as ordinary links -->
<div id="_auto32"></div>

$$
\begin{equation} 
 = (B^2+D^2) + (A^2+C^2-B^2-D^2)\cos^2\omega_0 t + 2(AC + BD)2\sin2\omega_0 t
\label{_auto32} \tag{45}
\end{equation}
$$

<!-- Equation labels as ordinary links -->
<div id="_auto33"></div>

$$
\begin{equation} 
 = (B^2+D^2) + (A^2+C^2-B^2-D^2)\frac{1+\cos{2\omega_0 t}}{2} + 2(AC + BD)\frac{1}{2}\sin2\omega_0 t
\label{_auto33} \tag{46}
\end{equation}
$$

<!-- Equation labels as ordinary links -->
<div id="_auto34"></div>

$$
\begin{equation} 
 = \frac{2B^2+2D^2+A^2+C^2-B^2-D^2}{2} + (A^2+C^2-B^2-D^2)\frac{\cos{2\omega_0 t}}{2} + (AC + BD)\sin2\omega_0 t
\label{_auto34} \tag{47}
\end{equation}
$$

<!-- Equation labels as ordinary links -->
<div id="_auto35"></div>

$$
\begin{equation} 
 = \frac{B^2+D^2+A^2+C^2}{2} + \frac{A^2+C^2-B^2-D^2}{2}\cos{2\omega_0 t} + (AC + BD)\sin2\omega_0 t
\label{_auto35} \tag{48}
\end{equation}
$$

<!-- Equation labels as ordinary links -->
<div id="_auto36"></div>

$$
\begin{equation} 
 = \alpha + \beta\cos{2\omega_0 t} + \gamma\sin2\omega_0 t
\label{_auto36} \tag{49}
\end{equation}
$$

<!-- Equation labels as ordinary links -->
<div id="_auto37"></div>

$$
\begin{equation} 
 = \alpha + \sqrt{\beta^2+\gamma^2}\left( \frac{\beta}{\sqrt{\beta^2+\gamma^2}}\cos{2\omega_0 t} + \frac{\gamma}{\sqrt{\beta^2+\gamma^2}}\sin2\omega_0 t\right) 
\label{_auto37} \tag{50}
\end{equation}
$$

<!-- Equation labels as ordinary links -->
<div id="_auto38"></div>

$$
\begin{equation} 
 = \alpha + \sqrt{\beta^2+\gamma^2}\left( \cos{\delta}\cos{2\omega_0 t} + \sin{\delta}\sin2\omega_0 t\right) 
\label{_auto38} \tag{51}
\end{equation}
$$

<!-- Equation labels as ordinary links -->
<div id="_auto39"></div>

$$
\begin{equation} 
 = \alpha + \sqrt{\beta^2+\gamma^2}\cos{\left( 2\omega_0 t - \delta\right) },
\label{_auto39} \tag{52}
\end{equation}
$$

which is what we wanted to show.  







### Exercise: Numerical Solution of the Harmonic Oscillator

Using the code we developed in homeworks 5 and/or 6 for the Earth-Sun system, we can solve the above harmonic oscillator problem in two dimensions using our code from this homework. We need however to change the acceleration from the gravitational force to the one given by the harmonic oscillator potential.


* 3a (20pt) Use for example the  code in the exercise set to set up the acceleration and use the initial conditions fixed by for example $r_{\rm min}$ from exercise 2. Which value should the initial velocity take if you place yourself at $r_{\rm min}$ and you require a circular motion? Hint: see the first midterm, part 2. There you used the centripetal acceleration.  

Instead of solving the equations in the cartesian frame we will now rewrite the above code in terms of the radial degrees of freedom only. Our differential equation is now

$$
\mu \ddot{r}=-\frac{dV(r)}{dr}+\mu\dot{\phi}^2,
$$

and

$$
\dot{\phi}=\frac{L}{\mu r^2}.
$$

* 3b (20pt) We will use $r_{\rm min}$ to fix a value of $L$, as seen in exercise 2. This fixes also $\dot{\phi}$. Write a code which now implements the radial equation for $r$ using the same $r_{\rm min}$ as you did in 3a. Compare the results with those from 3a with the same initial conditions. Do they agree? Use only one set of initial conditions.

The code here finds the solution for $x$ and $y$ using the code we
developed in homework 5 and 6 and the midterm.  Note that this code is
tailored to run in Cartesian coordinates. There is thus no angular
momentum dependent term.

Here we have chosen initial conditions that
correspond to the minimum of the effective potential
$r_{\mathrm{min}}$. We have chosen $x_0=r_{\mathrm{min}}$ and
$y_0=0$. Similarly, we use the centripetal acceleration to determine
the initial velocity so that we have a circular motion (see back to the
last question of the midterm). This means that we set the centripetal
acceleration $v^2/r$ equal to the force from the harmonic oscillator $-k\boldsymbol{r}$. Taking the
magnitude of $\boldsymbol{r}$ we have then
$v^2/r=k/mr$, which gives $v=\pm\omega_0r$. 

Since the code here solves the equations of motion in cartesian
coordinates and the harmonic oscillator potential leads to forces in
the $x$- and $y$-directions that are decoupled, we have to select the initial velocities and positions so that we don't get that for example $y(t)=0$.

We set $x_0$ to be different from zero and $v_{y0}$ to be different from zero.


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

DeltaT = 0.001
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
omega02 = k/m  # Frequency
AngMom = 1.0  #  The angular momentum
# Potential minimum
rmin = (AngMom*AngMom/k/m)**0.25
# Initial conditions as compact 2-dimensional arrays, x0=rmin and y0 = 0
x0 = rmin; y0= 0.0
r0 = np.array([x0,y0])
vy0 = sqrt(omega02)*rmin; vx0 = 0.0
v0 = np.array([vx0,vy0])
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

We see that the radius (to within a given error), we obtain a constant radius.


The following code shows first how we can solve this problem using the radial degrees of freedom only.
Here we need to add the explicit centrifugal barrier.  Note that the variable $r$ depends only on time. There is no $x$ and $y$ directions
since we have transformed the equations to polar coordinates.

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

### Exercise: Equations for an ellipse

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



### Exercise: Attractive Potential

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

At  $r_{\mathrm{min}}$  and $r_{\mathrm{max}}$ , all the kinetic energy is stored in the velocity in the direction perpendicular to $r$  since the radial velocity is set to zero . We can calculate using angular momentum and from there, find  𝐴  in terms of the energy  $E$  which is constant. But first, we need to find $r_{\mathrm{min}}$  from the conservation of energy (noting that the radial velocity $\ddot{r}$ at the mininum is zero):

$$
E = U(r) + \frac{1}{2} \mu(\ddot{r}^2 + (r\ddot{\phi})^2)
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
\frac{1}{\frac{\mu\alpha}{L^2}+A} = -\frac{\alpha}{2E} - \frac{1}{2} \sqrt{\frac{\alpha^2}{E^2} + 2\frac{L^2}{E\mu}}
\\
A = - \frac{\mu\alpha}{L^2} - \frac{2E}{\alpha + \sqrt{\alpha^2 + 2\frac{L^2E}{\mu}}}
$$

### Exercise: Inverse-square force

Consider again the same effective potential as in the previous exercise. This leads to an attractive inverse-square-law force, $F=-\alpha/r^2$. Consider a particle of mass $m$ with angular momentum $L$. Taylor sections 8.4-8.7 are relevant background material.  See also the harmonic oscillator potential from hw8. The equation of motion for the radial degrees of freedom is (see also hw8) in the center-of-mass frame in two dimensions with $x=r\cos{(\phi)}$ and $y=r\sin{(\phi)}$ and
$r\in [0,\infty)$, $\phi\in [0,2\pi]$ and $r=\sqrt{x^2+y^2}$ are given by

$$
\ddot{r}=-\frac{1}{m}\frac{dV(r)}{dr}+r\dot{\phi}^2,
$$

and

$$
\dot{\phi}=\frac{L}{m r^2}.
$$

Here $V(r)$ is any central force which depends only on the relative coordinate.


Find the radius of a circular orbit by solving for the position of the minimum of the effective potential.

<!-- Equation labels as ordinary links -->
<div id="_auto40"></div>

$$
\begin{equation}
\frac{1}{m}\frac{dV(r)}{dr}  = r\dot{\phi}^2
\label{_auto40} \tag{53}
\end{equation}
$$

<!-- Equation labels as ordinary links -->
<div id="_auto41"></div>

$$
\begin{equation}  \frac{1}{m}\left( -\frac{-\alpha}{r^2}\right)   = r \frac{L^2}{m^2r^4}
\label{_auto41} \tag{54}
\end{equation}
$$

<!-- Equation labels as ordinary links -->
<div id="_auto42"></div>

$$
\begin{equation}  \frac{\alpha}{mr^2}  = \frac{L^2}{m^2r^3}
\label{_auto42} \tag{55}
\end{equation}
$$

<!-- Equation labels as ordinary links -->
<div id="_auto43"></div>

$$
\begin{equation}  r  = \frac{L^2}{m\alpha}
\label{_auto43} \tag{56}
\end{equation}
$$

At the minimum, the radial velocity is zero and it is only the [centripetal velocity](https://en.wikipedia.org/wiki/Centripetal_force) which is nonzero. This implies that $\ddot{r}=0$.  What is the angular frequency, $\dot{\theta}$, of the orbit? Solve this by setting $\ddot{r}=0=F/m+\dot{\theta}^2r$.

<!-- Equation labels as ordinary links -->
<div id="_auto44"></div>

$$
\begin{equation}
\dot{\theta}^2 r  = - \frac{F}{m}
\label{_auto44} \tag{57}
\end{equation}
$$

<!-- Equation labels as ordinary links -->
<div id="_auto45"></div>

$$
\begin{equation}  \dot{\theta}^2 r  = - \frac{-\frac{\alpha}{r^2}}{m}
\label{_auto45} \tag{58}
\end{equation}
$$

<!-- Equation labels as ordinary links -->
<div id="_auto46"></div>

$$
\begin{equation}  \dot{\theta}^2  = \frac{\alpha}{mr^3}
\label{_auto46} \tag{59}
\end{equation}
$$

<!-- Equation labels as ordinary links -->
<div id="_auto47"></div>

$$
\begin{equation}  \dot{\theta}  = \pm \sqrt{\frac{\alpha}{mr^3}}
\label{_auto47} \tag{60}
\end{equation}
$$

<!-- Equation labels as ordinary links -->
<div id="_auto48"></div>

$$
\begin{equation}  \dot{\theta}  = \pm \sqrt{\frac{\alpha}{m\frac{L^6}{m^3\alpha^3}}}
\label{_auto48} \tag{61}
\end{equation}
$$

<!-- Equation labels as ordinary links -->
<div id="_auto49"></div>

$$
\begin{equation}  \dot{\theta}  = \pm \sqrt{\frac{\alpha^4m^2}{L^6}}
\label{_auto49} \tag{62}
\end{equation}
$$

<!-- Equation labels as ordinary links -->
<div id="_auto50"></div>

$$
\begin{equation}  \dot{\theta}  = \pm \frac{\alpha^2m}{L^3}
\label{_auto50} \tag{63}
\end{equation}
$$

Find the effective spring constant for the particle at the minimum.

We have shown in class that from the taylor expansion, we have

$$
k = \frac{d^2V_{\text{eff}}}{dr^2}
$$

Therefore, all we have to do is find the second derivative of $V_{\text{eff}}$ around the minimum point of $V_{\text{eff}}$ where $\dot{r} = \ddot{r} = 0$.

<!-- Equation labels as ordinary links -->
<div id="_auto51"></div>

$$
\begin{equation}
k  = \frac{d^2V_{\text{eff}}}{dr^2}
\label{_auto51} \tag{64}
\end{equation}
$$

<!-- Equation labels as ordinary links -->
<div id="_auto52"></div>

$$
\begin{equation}   = \frac{d^2\left( -\frac{\alpha}{r} + \frac{1}{2} \frac{L^2}{mr^2}\right) }{dr^2}
\label{_auto52} \tag{65}
\end{equation}
$$

<!-- Equation labels as ordinary links -->
<div id="_auto53"></div>

$$
\begin{equation}   = -\frac{2\alpha}{r^3} + \frac{3L^2}{mr^4}
\label{_auto53} \tag{66}
\end{equation}
$$

<!-- Equation labels as ordinary links -->
<div id="_auto54"></div>

$$
\begin{equation}   = -\frac{2\alpha}{\frac{L^6}{m^3\alpha^3}} + \frac{3L^2}{m\frac{L^8}{m^4\alpha^4}}
\label{_auto54} \tag{67}
\end{equation}
$$

<!-- Equation labels as ordinary links -->
<div id="_auto55"></div>

$$
\begin{equation}   = -\frac{2m^3\alpha^4}{L^6} + \frac{3m^3\alpha^4}{L^6}
\label{_auto55} \tag{68}
\end{equation}
$$

<!-- Equation labels as ordinary links -->
<div id="_auto56"></div>

$$
\begin{equation}   = \frac{m^3\alpha^4}{L^6}
\label{_auto56} \tag{69}
\end{equation}
$$

What is the angular frequency for small vibrations about the minimum? How does this compare with the answer to (3b)?

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
<div id="_auto57"></div>

$$
\begin{equation}
\omega =  \sqrt{\frac{k}{m}}
\label{_auto57} \tag{70}
\end{equation}
$$

<!-- Equation labels as ordinary links -->
<div id="_auto58"></div>

$$
\begin{equation}   = \sqrt{\frac{m^2\alpha^4}{L^6}} 
\label{_auto58} \tag{71}
\end{equation}
$$

<!-- Equation labels as ordinary links -->
<div id="_auto59"></div>

$$
\begin{equation}   = \frac{m\alpha^2}{L^3}
\label{_auto59} \tag{72}
\end{equation}
$$

This is in fact equal to the expression for $\dot{\theta}$. This means that small perturbations oscillate in sync with the orbit and this traces out an ellipse with a very small eccentricity, a very nice physical result.


### Exercise: Inverse-square force again

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

Show that for this case the total energy $E$ approaches zero.

<!-- Equation labels as ordinary links -->
<div id="_auto60"></div>

$$
\begin{equation}
E  = - \frac{\alpha}{r} + \frac{1}{2} m \left(  (\dot{\theta}r)^2+\dot{r}^2\right) 
\label{_auto60} \tag{73}
\end{equation}
$$

<!-- Equation labels as ordinary links -->
<div id="_auto61"></div>

$$
\begin{equation}   = - \frac{\alpha}{r} + \frac{1}{2} m \left[  \left( \frac{L}{mr^2}r\right) ^2+\left( \frac{dr}{d\theta}\dot{\theta}\right) ^2\right] 
\label{_auto61} \tag{74}
\end{equation}
$$

<!-- Equation labels as ordinary links -->
<div id="_auto62"></div>

$$
\begin{equation}   = - \frac{\alpha}{2r_0}(1+\cos\theta) + \frac{1}{2} m \left[  \left( \frac{L(1+\cos\theta)}{2mr_0}\right) ^2+\left( 2r_0\frac{-1}{(1+\cos\theta)^2}(-\sin\theta)\frac{L}{mr^2}\right) ^2\right] 
\label{_auto62} \tag{75}
\end{equation}
$$

<!-- Equation labels as ordinary links -->
<div id="_auto63"></div>

$$
\begin{equation}   = - \frac{\alpha}{2r_0}(1+\cos\theta) + \frac{1}{2} m \left[  \left( \frac{L(1+\cos\theta)}{2mr_0}\right) ^2+\left( 2r_0\frac{-1}{(1+\cos\theta)^2}(-\sin\theta)\frac{L(1+\cos\theta)^2}{4mr_0^2}\right) ^2\right] 
\label{_auto63} \tag{76}
\end{equation}
$$

<!-- Equation labels as ordinary links -->
<div id="_auto64"></div>

$$
\begin{equation}   = - \frac{\alpha}{2r_0}(1+\cos\theta) + 
\frac{1}{2} m \left[  \left( \frac{L(1+\cos\theta)}{2mr_0}\right) ^2+\left( \sin\theta\frac{L}{2mr_0}\right) ^2\right] 
\label{_auto64} \tag{77}
\end{equation}
$$

<!-- Equation labels as ordinary links -->
<div id="_auto65"></div>

$$
\begin{equation}   = - \frac{\alpha}{2r_0}(1+\cos\theta) + 
\frac{1}{2} m \left[  \left( \frac{L(1+\cos\theta)}{2mr_0}\right) ^2+\left( \sin\theta\frac{L}{2mr_0}\right) ^2\right] 
\label{_auto65} \tag{78}
\end{equation}
$$

<!-- Equation labels as ordinary links -->
<div id="_auto66"></div>

$$
\begin{equation}   = - \frac{\alpha}{2r_0}(1+\cos\theta) + 
\frac{1}{2} m \frac{L^2}{4m^2r_0^2} \left[  \left( 1+\cos\theta\right) ^2+\left( \sin\theta\right) ^2\right] 
\label{_auto66} \tag{79}
\end{equation}
$$

<!-- Equation labels as ordinary links -->
<div id="_auto67"></div>

$$
\begin{equation}   = - \frac{\alpha}{2r_0}(1+\cos\theta) + 
\frac{1}{2} \frac{L^2}{4mr_0^2} \left(  1 + \cos^2\theta + 2\cos \theta + \sin^2\theta\right) 
\label{_auto67} \tag{80}
\end{equation}
$$

<!-- Equation labels as ordinary links -->
<div id="_auto68"></div>

$$
\begin{equation}   = - \frac{\alpha}{2r_0}(1+\cos\theta) + 
\frac{1}{2} \frac{L^2}{4mr_0^2} \left(  2 + 2\cos \theta \right) 
\label{_auto68} \tag{81}
\end{equation}
$$

<!-- Equation labels as ordinary links -->
<div id="_auto69"></div>

$$
\begin{equation}   = (1+\cos\theta) \left( - \frac{\alpha}{2r_0} + \frac{L^2}{4mr_0^2}\right) 
\label{_auto69} \tag{82}
\end{equation}
$$

<!-- Equation labels as ordinary links -->
<div id="_auto70"></div>

$$
\begin{equation}   = (1+\cos\theta) \left( - \frac{\alpha}{2\frac{L^2}{2m\alpha}} + \frac{L^2}{4m\frac{L^4}{4m^2\alpha^2}}\right) 
\label{_auto70} \tag{83}
\end{equation}
$$

<!-- Equation labels as ordinary links -->
<div id="_auto71"></div>

$$
\begin{equation}   = (1+\cos\theta) \left( - \frac{m\alpha^2}{L^2} + \frac{m\alpha^2}{L^2}\right) 
\label{_auto71} \tag{84}
\end{equation}
$$

<!-- Equation labels as ordinary links -->
<div id="_auto72"></div>

$$
\begin{equation}   = 0
\label{_auto72} \tag{85}
\end{equation}
$$

With zero energy $E=0$, write this trajectory in a more recognizable parabolic form, that is express $x_0$ and $R$ in terms of $r_0$ using

$$
x=x_0-\frac{y^2}{R}.
$$

We have that

<!-- Equation labels as ordinary links -->
<div id="_auto73"></div>

$$
\begin{equation}
x  = r \cos\theta
\label{_auto73} \tag{86}
\end{equation}
$$

<!-- Equation labels as ordinary links -->
<div id="_auto74"></div>

$$
\begin{equation} 
y  = r \sin \theta.
\label{_auto74} \tag{87}
\end{equation}
$$

Using the general solution with eccintricity $\epsilon=1$, we have

$$
r(\theta)=\frac{c}{1+\cos\theta},
$$

and multiplying both sides with $1+\cos\theta$ and using that $x=r\cos\theta$,

$$
r = c -x,
$$

and using that $r^2=x^2+y^2$, we square both sides

$$
r^2 = x^2+y^2=c^2 +x^2-2cx,
$$

leading to

$$
y^2=c^2-2cx,
$$

and using that we defined

$$
c=2r_0=\frac{L^2}{m\alpha},
$$

we divide by $2c$ 
and we get the final answer

$$
x = r_0 - \frac{y^2}{4r_0}
$$

### Exercise: Parabolic and hyperbolic orbits

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
<div id="_auto75"></div>

$$
\begin{equation}
x  = r\cos\phi
\label{_auto75} \tag{88}
\end{equation}
$$

<!-- Equation labels as ordinary links -->
<div id="_auto76"></div>

$$
\begin{equation}   = \frac{c\cos\phi}{1+\epsilon\cos\phi}
\label{_auto76} \tag{89}
\end{equation}
$$

<!-- Equation labels as ordinary links -->
<div id="_auto77"></div>

$$
\begin{equation}
y  = r\sin\phi 
\label{_auto77} \tag{90}
\end{equation}
$$

<!-- Equation labels as ordinary links -->
<div id="_auto78"></div>

$$
\begin{equation}   = \frac{c\sin\phi}{1+\epsilon\cos\phi}
\label{_auto78} \tag{91}
\end{equation}
$$

Here $\epsilon>1$.  We use our equation for $r$, multiply with the denominator $1+\epsilon\cos\phi$ on both sides and have

$$
r(1+\epsilon\cos\phi)=c,
$$

use $x=r\cos\phi$ and square and use that $r^2=x^2+y^2$ and we have

$$
r^2=x^2+y^2=c^2+\epsilon^2x^2-2cx\epsilon,
$$

and reorder

$$
x^2(\epsilon^2-1)-y^2-2cx\epsilon= -c^2.
$$

We complete the square in $x$ by adding and subtracting on both sides $\epsilon^2c^2/(\epsilon^2-1)$
and we obtain

$$
(\epsilon^2-1)(x-\delta)^2-y^2= -c^2+\frac{\epsilon^2c^2}{\epsilon^2-1}.
$$

Here we have defined

$$
\delta = \frac{c\epsilon}{\epsilon^2-1},
$$

and introducing the constants

$$
\alpha = \frac{c}{\epsilon^2-1},
$$

and

$$
\beta = \frac{c}{\sqrt{\epsilon^2-1}},
$$

we can rewrite the above equation as

$$
\frac{(x-\delta)^2}{\alpha^2}-\frac{y^2}{\beta^2}=1,
$$

which is nothing but the equation for a hyperbola.


### Exercise: Testing orbit types

In this exercise we can use the program for $r(\phi)$ we developed in hw8. We will use an inverse-square-law force as in the previous four exercises. The aim is to see that the orbits we get for $E<0$ become ellipses (or circles), parabola for $E=0$ and hyperbola for $E>0$.  An example code is shown here.

Here we have defined the constants $L=m=\alpha=1$. Feel free to set new values. **You need also to set the initial conditions** in order to study the different types of orbits. It may be useful to plot the potential here and find the values for the initial conditions that fit $E<0$, $E=0$ and $E>0$.

# Common imports
import numpy as np
import pandas as pd
from math import *
import matplotlib.pyplot as plt
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
# You need to specify the initial conditions
# Here we have chosen the conditions which lead to circular orbit and thereby a constant r
r0 = (AngMom*AngMom/m/alpha)
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

plt.show()

Run your code and study and discuss the situations where you have
elliptical, parabolic and hyperbolic orbits. Discuss the physics of
these cases. The results from the four previous exercises 4 may be useful
here.  In the code here we have chosen initial conditions which correspond to circular motion.
This corresponds to

$$
r_{\mathrm{min}} = \frac{L^2}{m\alpha}.
$$

Note well that the velocity is now the radial velocity. If we want to
study the angular velocity we would need to add the equations for this
quantity. The solution to exercises 1-4 give you the minimum $r$
values needed to find the elliptical, parabolic and hyperbolic
orbits. For elliptical orbits you should have $\frac{L^2}{2m\alpha} <
r_{\mathrm{min}} <\frac{L^2}{m\alpha}$. For parabolic orbits
$r_{\mathrm{min}} =\frac{L^2}{m\alpha}$ and for hyperbolic orbits we
have $0<r_{\mathrm{min}} <\frac{L^2}{m\alpha}$. Try out these
different initial conditions in order to test these different types of
motion.




### Exercise: New reference frame

Show that if one transforms to a reference frame where the total
momentum is zero, $\boldsymbol{p}_1=-\boldsymbol{p}_2$, that the relative momentum
$\boldsymbol{q}$ corresponds to either $\boldsymbol{p}_1$ or $-\boldsymbol{p}_2$. This
means that in this frame the magnitude of $\boldsymbol{q}$ is one half the
magnitude of $\boldsymbol{p}_1-\boldsymbol{p}_2$.

### Exercise: Center of mass and relative coordinates

Given the center of mass and relative coordinates $\boldsymbol{R}$ and $\boldsymbol{r}$, respectively, for
particles of mass $m_1$ and $m_2$, find the coordinates $\boldsymbol{r}_1$
and $\boldsymbol{r}_2$ in terms of the masses, $\boldsymbol{R}$ and $\boldsymbol{r}$.


### Exercise: Two-body problems

Consider a particle of mass $m$ moving in a potential

$$
V(r)=\alpha\ln(r/\alpha),
$$

where $\alpha$ is a constant.

* (a) If the particle is moving in a circular orbit of radius $R$, find the angular frequency $\dot{\theta}$. Solve this by setting $F=-m\dot{\theta}^2r$ (force and acceleration point inward).

* (b) Express the angular momentum $L$ in terms of the constant $\alpha$, the mass $m$ and the radius $R$. Also express $R$ in terms of $L$, $\alpha$ and $m$.

* (c) Sketch the effective radial potential, $V_{\rm eff}(r)$, for a particle with angular momentum $L$. (No longer necessarily moving in a circular orbit.)

* (d) Find the position of the minimum of $V_{\rm eff}$ in terms of $L$, $\alpha$ and $m$, then compare to the result of (b).

* (e)  What is the effective spring constant for a particle at the minimum of $V_{\rm eff}$? Express your answer in terms of $L$, $m$ and $\alpha$. 

* (f)   What is the angular frequency, $\omega$, for small oscillations of $r$ about the $R_{\rm min}$?  Express your answer in terms of $\dot{\theta}$ from part (3a).