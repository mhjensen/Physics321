#!/usr/bin/env python
# coding: utf-8

# <!-- HTML file automatically generated from DocOnce source (https://github.com/doconce/doconce/)
# doconce format html Firstmidterm2022.do.txt --no_mako -->
# <!-- dom:TITLE: PHY321: Classical Mechanics 1 -->

# # PHY321: Classical Mechanics 1
# **First midterm project, due Friday March 4**
# 
# Date: **Mar 1, 2022**

# ### Practicalities about  homeworks and projects
# 
# 1. You can work in groups (optimal groups are often 2-3 people) or by yourself. If you work as a group you can hand in one answer only if you wish. **Remember to write your name(s)**!
# 
# 2. How do I(we)  hand in?  You can hand in the paper and pencil exercises as a hand-written document. Alternatively, you can hand in everyhting (if you are ok with typing mathematical formulae using say Latex) as a jupyter notebook at D2L. The numerical part should always be handed in as a jupyter notebook by the deadline at D2L.

# ### Introduction to the first midterm project, total score 140 points
# 
# The relevant reading background is
# 1. chapters 2-5 of Taylor.
# 
# 2. chapters 6-14 of Malthe-Sørenssen.
# 
# In this midterm project we will start with a potential similar to the
# one we discussed in exercise 1 in homework 5. There are some elements
# of that exercise which are repeated here, similarly, a good fraction
# of the codes you have developed for homeworks 3-5 can be used here.
# We start with a one-dimensional potential and motion.  Thereafter we
# extend this potential model to a two-dimensional model and study the
# numerical solution of the corresponding problem.

# ### Part 1, Particle in a one-dimensional  potential
# 
# We consider a particle (for example an atom) of mass $m$ moving in a one-dimensional potential,

# $$
# V(x)=\frac{V_0}{d^4}\left(x^4-2x^2d^2+d^4\right).
# $$

# We will assume all other forces on the particle are small in comparison, and neglect them in our model.  The parameters $V_0$ and $d$ are known constants. 
# 
# 1. (5pt) Plot the potential and find the  equilibrium points (stable and unstable) by requiring that the first derivative of the potential is zero. Make an energy diagram (see for example Malthe-Sørenssen chapter 11.3) and mark the equilibrium points on the diagram and characterize their stability. The position of the particle is $x$. 
# 
# 2. (5pt) Choose two different energies that give two distinct types of motions, draw them into the energy diagram, and describe the motion in each case.
# 
# 3. (5pt) If the particle  starts at rest at $x=2d$, what is the velocity of the particle at the point $x=d$?
# 
# 4. (5pt) If the particle  starts at $x=d$ with velocity $v_0$, how large must $v_0$ be for the  particle to reach the point $x=−d$?
# 
# 5. (5pt) Use the above potential to set up the total forces acting on the particle.  Find the acceleration acting on the particle. Is this a conservative force? Calculate also the **curl** of the force  $\boldsymbol{\nabla}\times \boldsymbol{F}$ in order to validate your conclusion. 
# 
# 6. (5pt) Are linear momentum and angular momentum conserved? You need to show this by calculating the quantities.
# 
# 7. (10pt) Write a numerical algorithm to find the position and velocity of the particle at a time $t+\Delta t$ given the position and velocity at a time $t$. Here you can use either the standard forward Euler, or the Euler-Cromer or the Velocity Verlet algorithms.   You need to justify your choice here (hint: consider energy conservation).
# 
# 8. (10pt) Use now your program to find the position of the particle as function of time from $t=0$ to $t=30$ s using a mass  $m=1.0$ kg, the parameter $V_0=1$ J and $d=0.1$ m. Make a plot of three distinct positions with initial conditions $x_0=d$ and $v_0=0.5$ m/s, $x_0=d$ and $v_0=1.5$ m/s, and $x_0=d$ and $v_0=2.5$ m/s. Plot also the velocity.  Perform calculations with and without the term $x^4$ in the potential. Do you see a difference? 
# 
# 9. (10pt) Describe the behavior of the particle for the three initial conditions  and sketch the motion in an energy diagram. Is energy conserved in your simulations?

# ### Part 2, two dimensions
# 
# We move then to two dimensions. Our particle/object interacts with a surface potential given by

# $$
# V(r)=\frac{V_0}{d^4}\left(r^4-2r^2d^2+d^4\right),
# $$

# where $r=\sqrt{x^2+y^2}$ is the distance to the origin.
# 
# 1. (5pt) Show that the acceleration is now $\boldsymbol{a}=-\frac{4V_0}{md^4}\left(r^3-rd^2\right)\frac{\boldsymbol{r}}{r}$.
# 
# 2. (10pt) Rewrite your program to find the velocity and position of the atom using the new expression for the force $\boldsymbol{F}$. Use vectorized expressions in your code as you did in homework 5 for the Earth-Sun system or in homework 3 and 4. See eventually the code from the [lectures](https://mhjensen.github.io/Physics321/doc/pub/week7/html/week7.html).  We recommend to revisit the Earth-Sun problem from homework 5 since it has several similarities with the problem here.
# 
# 3. (10pt) Plot the motion of a particle starting in $\boldsymbol{r}_0=(d,0)$ from $t=0$ s to $t=20$ s for the initial velocities $\boldsymbol{v}_0=(0,0.5)$ m/s, $\boldsymbol{v}_0=(0,1)$ m/s, and $\boldsymbol{v}_0=(0,1.5)$ m/s. The parameters $d$ and $V_0$ are as before.
# 
# 4. (5pt) Is energy conserved? 
# 
# 5. (10pt) Can you choose initial conditions $r_0$ and $v_0$ in such a manner that the particle moves in a circular orbit with a constant radius? If so, what initial conditions are those? Plot the motion for these conditions.

# ### Part 3, a potential with confinement
# 
# In the final part we are going to study a new potential. This potential contains the basic mathematical components needed to describe the confinement of quarks through a term $\kappa x$. The aim of this exercise is to try to develop your intuition about the motion of physical objects due to specific forces. Then we will test our intution by running simulations. The potential, in one dimension only is defined for $x\in [0.2,\infty)$.  It reads

# $$
# V(x) = -\frac{\gamma}{x}+\frac{\delta}{x^2}+\kappa x,
# $$

# where the last term is the one which ensures confinement of for example quarks.
# 
# 1. (5pt) Plot the potential for $x\in [0.2,10]$ and set $\gamma=10$, $\delta = 3$ and $\kappa =1$. Find the value of $x$ where the potential has a minimum.
# 
# 2. (5pt) Show that this potential leads to an energy conserving force by calculating the **curl** of the resulting force.
# 
# 3. (10pt) Assume now that at $x=2$ the particle moving in this potential is at rest, that is its velocity is zero. Find the total energy and describe what kind of motion you can expect. The point $x=2$ is a so-called turning point. Can you find the other turning point where the kinetic energy is zero. If you keep increasing $x$, will the particle ever be able to escape the potential well?
# 
# 4. (20pt) Finally we will now change our program (using either the Euler-Cromer or the Velocity-Verlet method) and compute the position and the velocity as functions of time using the force computed from the above potential. Use as initial condition at time $t=0$ that the particle is $x_0=2$ and has initial velocity $v_0=0$. Test numerically that energy is conserved as function of time. And test that the particle moves according to your analysis from the previous exercise.

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
# <tr><th align="center">  HW/Project </th> <th align="center">Due Date</th> <th align="center">Extra Credit Assignment</th> </tr>
# </thead>
# <tbody>
# <tr><td align="center">   HW 3             </td> <td align="center">   2-8         </td> <td align="center">   Abstract                   </td> </tr>
# <tr><td align="center">   HW 4             </td> <td align="center">   2-15        </td> <td align="center">   Introduction               </td> </tr>
# <tr><td align="center">   HW 5             </td> <td align="center">   2-22        </td> <td align="center">   Methods                    </td> </tr>
# <tr><td align="center">   HW 6             </td> <td align="center">   3-1         </td> <td align="center">   Results and Discussion     </td> </tr>
# <tr><td align="center">   **Midterm 1**    </td> <td align="center">   **3-12**    </td> <td align="center">   *Full Written Report*      </td> </tr>
# <tr><td align="center">   HW 7             </td> <td align="center">   3-22        </td> <td align="center">   Abstract                   </td> </tr>
# <tr><td align="center">   HW 8             </td> <td align="center">   3-29        </td> <td align="center">   Introduction               </td> </tr>
# <tr><td align="center">   HW 9             </td> <td align="center">   4-5         </td> <td align="center">   Results and Discussion     </td> </tr>
# <tr><td align="center">   **Midterm 2**    </td> <td align="center">   **4-16**    </td> <td align="center">   *Full Written Report*      </td> </tr>
# <tr><td align="center">   HW 10            </td> <td align="center">   4-26        </td> <td align="center">   Abstract                   </td> </tr>
# <tr><td align="center">   **Final**        </td> <td align="center">   **4-30**    </td> <td align="center">   *Full Written Report*      </td> </tr>
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
