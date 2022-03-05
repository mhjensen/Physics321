#!/usr/bin/env python
# coding: utf-8

# <!-- HTML file automatically generated from DocOnce source (https://github.com/doconce/doconce/)
# doconce format html hw5.do.txt --no_mako -->
# <!-- dom:TITLE: PHY321: Classical Mechanics 1 -->

# # PHY321: Classical Mechanics 1
# **Homework 5, due Friday   February 18**
# 
# Date: **Feb 6, 2022**

# ### Practicalities about  homeworks and projects
# 
# 1. You can work in groups (optimal groups are often 2-3 people) or by yourself. If you work as a group you can hand in one answer only if you wish. **Remember to write your name(s)**!
# 
# 2. Homeworks are available ten days before the deadline.
# 
# 3. How do I(we)  hand in?  You can hand in the paper and pencil exercises as a scanned document. For this homework this applies to exercises 1-5. Alternatively, you can hand in everyhting (if you are ok with typing mathematical formulae using say Latex) as a jupyter notebook at D2L. The numerical exercise(s) (exercise 6 here) should always be handed in as a jupyter notebook by the deadline at D2L.

# ### Introduction to homework 5
# 
# This week's sets of classical pen and paper and computational
# exercises are a continuation of the topics from the previous homework
# set and lectures from the last two weeks. We keep dealing with simple
# motion problems and conservation laws; energy, momentum and angular
# momentum. These conservation laws are central in Physics and
# understanding them properly lays the foundation for understanding and
# analyzing more complicated physics problems.
# 
# The relevant reading background is
# 1. chapters 3 and 4 of Taylor (there are many good examples there) and
# 
# 2. chapters 10-14 of Malthe-Sørenssen.
# 
# 3. For the numerical exercise, see Malthe-Sørenssen section 7.5
# 
# In both textbooks there are many nice worked out examples. Malthe-Sørenssen's text contains also several coding examples you may find useful. 
# 
# The numerical homework focuses on another motion problem where you can
# use the code you developed in homework sets 3 and 4, almost entirely. Please take
# a look at the posted solutions (jupyter-notebook) for homework sets 3 and 4. You
# need only to change the forces at play. The problem at hand is a
# classic, the gravitational force acting between the Sun and the
# Earth. Here you will notice also that the standard Euler-integration
# algorithm is not the best choice and we will introduce the so-called
# Euler-Cromer method and the Velocity-Verlet method. These methods will
# give much more stable numerical results with only few additions to
# your code.
# 
# The code you develop here will also be reused when we analyze energy
# conservation in homework set 6. And for those of you doing the honors
# project, it serves as a starting point for the solar system variant.

# ### Exercise 1 (15 pt), Work-energy theorem and conservation laws
# 
# This exercise was partly discussed during the lectures of the week of February 8-12, see <https://mhjensen.github.io/Physics321/doc/pub/week6/html/week6.html>.
# 
# We will study a classical electron which moves in the $x$-direction along a surface. The force from the surface is

# $$
# \boldsymbol{F}(x)=-F_0\sin{(\frac{2\pi x}{b})}\boldsymbol{e}_x.
# $$

# The constant $b$ represents the distance between atoms at the surface of the material, $F_0$ is a constant and $x$ is the position of the electron.
# 
# * 1a (2pt) Is this a conservative force? And if so, what does that imply?
# 
# * 1b (4pt) Use the work-energy theorem to find the velocity $v(x)$. 
# 
# * 1c (4pt) With the above expression for the force, find the potential energy.
# 
# * 1d (5pt) Make a plot of the potential energy and discuss the equilibrium points where the force on the electron is zero. Discuss the physical interpretation of stable and unstable equilibrium points. Use energy conservation. Recommended read here  is Malthe-Sørenssen chapter 11.3.2.

# ### Exsercise 2 (15pt), Rocket, Momentum and mass
# 
# Taylor exercise 3.11.   This exercise is meant to illustrate momentum conservation or not. 
# This exercise was partly discussed during the lectures, see the notes from the week of February 8-12 on [Energy and Momentum etc, see the part on Momentum conservation](https://mhjensen.github.io/Physics321/doc/pub/week6/html/week6.html). Taylor's chapter 3.2 covers also this example.

# ### Exercise 3 (10pt), More Rockets
# 
# Taylor exercises 3.13 (5pt) and 3.14 (5pt). This is a continuation of
# the previous exercise and most of the relevant background material can
# be found in Taylor chapter 3.2.

# ### Exercise 4 (10pt), Center of mass
# 
# Taylor exercise 3.20. Here Taylor's chapter 3.3 can be of use. This
# relation will turn out to be very useful when we discuss systems of
# many classical particles.

# ### Exercise 5 (10pt), Warming up for the Earth-Sun system, Scaling the Equations
# 
# The aim of this exercise (as well as the next) is to study the motion
# of objects under the influence of the gravitational force.  We will
# limit ourselves to the Earth-Sun system. Here we will scale the
# equations and sketch our first algorithm for solving the equations,
# namely using Euler's method again, as we did in homework sets 3 and 4.  This part
# together with the numerical part forms also the entry point for the
# solar system honors project. Furthermore, we will reuse parts of these
# results when analyzing energy conservation in homework 6.
# 
# We will limit ourselves (in order to test the algorithm) to a
# hypothetical solar system with the Earth only orbiting around the sun.
# The only force in the problem is gravity. Newton's law of gravitation
# is given by a force $F_G$

# $$
# F_G=\frac{GM_{\odot}M_{\mathrm{Earth}}}{r^2},
# $$

# where $M_{\odot}$ is the mass of the Sun and $M_{\mathrm{Earth}}$ is
# the mass of the Earth. The gravitational constant is $G$ and $r$ is
# the distance between the Earth and the Sun.  The Sun
# has a mass which is much larger than that of the Earth. We can
# therefore safely neglect the motion of the Sun in this problem.
# 
# We assume that the orbit of the Earth around the Sun 
# is co-planar, and we take this to be the $xy$-plane.
# Using Newton's second law of motion we get the following equations

# $$
# \frac{d^2x}{dt^2}=\frac{F_{G,x}}{M_{\mathrm{Earth}}},
# $$

# and

# $$
# \frac{d^2y}{dt^2}=\frac{F_{G,y}}{M_{\mathrm{Earth}}},
# $$

# where $F_{G,x}$ and $F_{G,y}$ are the $x$ and $y$ components of the
# gravitational force.
# 
# We will use so-called astronomical units when rewriting our equations.
# Using astronomical units (AU as abbreviation)it means that one
# astronomical unit of length, known as 1 AU, is the average distance
# between the Sun and Earth, that is $1$ AU = $1.5\times 10^{11}$ m.  It
# can also be convenient to use years instead of seconds since years
# match better the time evolution of the solar system. The mass of the
# Sun is $M_{\mathrm{sun}}=M_{\odot}=2\times 10^{30}$ kg. The mass of
# Earth is $M_{\mathrm{Earth}}=6\times 10^{24}$ kg with a distance 1AU.
# 
# In setting up the equations we limit ourselves to a co-planar
# motion and use only the $x$ and $y$ coordinates. But you should feel
# free to extend your equations to three dimensions, it is not very
# difficult and the data from NASA are all in three dimensions.
# 
# [NASA](http://www.nasa.gov/index.html) has an excellent site at <http://ssd.jpl.nasa.gov/horizons.cgi#top>.
# From there you can extract initial conditions in order to start your differential equation solver.
# At the above website you need to change from **OBSERVER** to **VECTOR** and then write in the planet you are interested in.
# The generated data contain the $x$, $y$ and $z$ values as well as their corresponding velocities. The velocities are in units of AU per day.
# Alternatively they can be obtained in terms of km and km/s. 
# 
# For the system below involving only the Earth and the Sun, you
# could just initialize the position with say $x=1$ AU and $y=0$ AU.
# 
# We assume that mass units can be obtained by using the fact that
# Earth's orbit is almost circular around the Sun.
# 
# For circular motion we know that the force must obey the following relation

# $$
# F_G= \frac{M_{\mathrm{Earth}}v^2}{r}=\frac{GM_{\odot}M_{\mathrm{Earth}}}{r^2},
# $$

# where $v$ is the velocity of Earth. 
# The latter equation can be used to show that

# $$
# v^2r=GM_{\odot}=4\pi^2\mathrm{AU}^3/\mathrm{yr}^2.
# $$

# * 5a (5pt) Show how to derive the last equation and use this to scale the differential equations, getting thus rid of the constant $G$ and the two masses. Split the differential equations for the motion in the $x$ and $y$ directions in terms of four coupled differential equations.
# 
# * 5b (5pt)  Discretize the above differential equations and set up an algorithm for solving these equations using Euler's forward algorithm and the so-called velocity Verlet method [discussed in the lecture notes](https://mhjensen.github.io/Physics321/doc/pub/week7/html/week7.html). Here you can reuse what you did in homework sets 3 and 4.

# ### Exercise 6 (40pt), Numerical elements, solving exercise 5 numerically
# 
# **This exercise should be handed in as a jupyter-notebook** at D2L. Remember to write your name(s). 
# 
# In homework sets 3 and 4 we:
# 1. studied  Euler's Method to find the position and the velocity of a falling object, including air resistance and gravity
# 
# 2. and added additional forces to our model and studied a bouncing ball.
# 
# This week we will reuse our code from homework 4 (exercises 6)
# and replace the air resistance and force from the ground with the
# gravitational force. Then we will study the stability of the system as function of initial conditions and the time step length.
# 
# We start by importing some standard packages

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')

# let's start by importing useful packages we are familiar with
import numpy as np
from math import *
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# * 6a (30 pt)  Write then a program which solves the above differential equations for the Earth-Sun system using Euler's  method and the velocity Verlet method.  Find out which initial value for the velocity that gives a circular orbit and test the stability of your algorithm as function of different time steps $\Delta t$.  Make a plot of the results you obtain for the position of the Earth (plot the $x$ and $y$ values and/or if you prefer to use three dimensions the $z$-value as well) orbiting  the Sun. Discuss eventual differences between the Verlet algorithm and the Euler algorithm. 
# 
# * 6b (10pt) Consider then a planet which begins at a distance of 1 AU from the sun. Find out by trial and error what the initial velocity must be in order for the planet to escape from the sun.  Can you find an exact answer?  How does that match your numerical results?
# 
# Here we add a code-example which may aid in the above studies using Euler's forward method.

# In[2]:


DeltaT = 0.001
#set up arrays 
tfinal = 10 # in years
n = ceil(tfinal/DeltaT)
# set up arrays for time t, velocity v, and position r
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


# ### Classical Mechanics Extra Credit Assignment: Scientific Writing and attending Talks
# 
# The following gives you an opportunity to earn **five extra credit
# points** on each of the remaining homeworks and **ten extra credit points**
# on the midterms and finals.  This assignment also covers an aspect of
# the scientific process that is not taught in most undergraduate
# programs: scientific writing.  Writing scientific reports is how
# scientist communicate their results to the rest of the field.  Knowing
# how to assemble a well written scientific report will greatly benefit
# you in you upper level classes, in graduate school, and in the work
# place.
# 
# The full information on extra credits is found at <https://github.com/mhjensen/Physics321/blob/master/doc/Homeworks/ExtraCredits/>. There you will also find examples on how to write a scientific article. 
# Below you can also find a description on how to gain extra credits by attending scientific talks.
# 
# This assignment allows you to gain extra credit points by practicing
# your scientific writing.  For each of the remaining homeworks you can
# submit the specified section of a scientific report (written about the
# numerical aspect of the homework) for five extra credit points on the
# assignment.  For the two midterms and the final, submitting a full
# scientific report covering the numerical analysis problem will be
# worth ten extra points.  For credit the grader must be able to tell
# that you put effort into the assignment (i.e. well written, well
# formatted, etc.).  If you are unfamiliar with writing scientific
# reports, [see the information here](https://github.com/mhjensen/Physics321/blob/master/doc/Homeworks/ExtraCredits/IntroductionScientificWriting.md)
# 
# The following table explains what aspect of a scientific report is due
# with which homework.  You can submit the assignment in any format you
# like, in the same document as your homework, or in a different one.
# Remember to cite any external references you use and include a
# reference list.  There are no length requirements, but make sure what
# you turn in is complete and through.  If you have any questions,
# please contact Julie Butler at butler@frib.msu.edu.
# 
# <table class="dotable" border="1">
# <thead>
# <tr><th align="center">  HW/Project </th> <th align="center"> Due Date</th> <th align="center">Extra Credit Assignment</th> </tr>
# </thead>
# <tbody>
# <tr><td align="center">   HW 3             </td> <td align="center">   2-8          </td> <td align="center">   Abstract                   </td> </tr>
# <tr><td align="center">   HW 4             </td> <td align="center">   2-15         </td> <td align="center">   Introduction               </td> </tr>
# <tr><td align="center">   HW 5             </td> <td align="center">   2-22         </td> <td align="center">   Methods                    </td> </tr>
# <tr><td align="center">   HW 6             </td> <td align="center">   3-1          </td> <td align="center">   Results and Discussion     </td> </tr>
# <tr><td align="center">   **Midterm 1**    </td> <td align="center">   **3-12**     </td> <td align="center">   *Full Written Report*      </td> </tr>
# <tr><td align="center">   HW 7             </td> <td align="center">   3-22         </td> <td align="center">   Abstract                   </td> </tr>
# <tr><td align="center">   HW 8             </td> <td align="center">   3-29         </td> <td align="center">   Introduction               </td> </tr>
# <tr><td align="center">   HW 9             </td> <td align="center">   4-5          </td> <td align="center">   Results and Discussion     </td> </tr>
# <tr><td align="center">   **Midterm 2      </td> <td align="center">   ** _4-16_    </td> <td align="center">   *Full Written Report*      </td> </tr>
# <tr><td align="center">   HW 10            </td> <td align="center">   4-26         </td> <td align="center">   Abstract                   </td> </tr>
# <tr><td align="center">   **Final**        </td> <td align="center">   **4-30**     </td> <td align="center">   *Full Written Report*      </td> </tr>
# </tbody>
# </table>
# 
# You can also gain extra credits if you attend scientific talks.
# This is described here.

# ### Integrating Classwork With Research
# 
# This opportunity will allow you to earn up to 5 extra credit points on a Homework per week. These points can push you above 100% or help make up for missed exercises.
# In order to earn all points you must:
# 
# 1. Attend an MSU research talk (recommended research oriented Clubs is  provided below)
# 
# 2. Summarize the talk using at least 150 words
# 
# 3. Turn in the summary along with your Homework.
# 
# Approved talks:
# Talks given by researchers through the following clubs:
# * Research and Idea Sharing Enterprise (RAISE)​: Meets Wednesday Nights Society for Physics Students (SPS)​: Meets Monday Nights
# 
# * Astronomy Club​: Meets Monday Nights
# 
# * Facility For Rare Isotope Beam (FRIB) Seminars: ​Occur multiple times a week
# 
# If you have any questions please consult Jeremy Rebenstock, rebensto@msu.edu.
# 
# All the material on extra credits is at <https://github.com/mhjensen/Physics321/blob/master/doc/Homeworks/ExtraCredits/>.
