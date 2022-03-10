#!/usr/bin/env python
# coding: utf-8

# <!-- HTML file automatically generated from DocOnce source (https://github.com/doconce/doconce/)
# doconce format html hw4.do.txt --no_mako -->
# <!-- dom:TITLE: PHY321: Classical Mechanics 1 -->

# # PHY321: Classical Mechanics 1
# **Homework 4, due Friday  February 11**
# 
# Date: **Jan 31, 2022**

# ### Practicalities about  homeworks and projects
# 
# 1. You can work in groups (optimal groups are often 2-3 people) or by yourself. If you work as a group you can hand in one answer only if you wish. **Remember to write your name(s)**!
# 
# 2. Homeworks are available ten days before the deadline.
# 
# 3. How do I(we)  hand in?  You can hand in the paper and pencil exercises as a scanned document. For this homework this applies to exercises 1-5. Alternatively, you can hand in everyhting (if you are ok with typing mathematical formulae using say Latex) as a jupyter notebook at D2L. The numerical exercise(s) (exercise 6 here) should always be handed in as a jupyter notebook by the deadline at D2L.

# ### Introduction to homework 4
# 
# This week's sets of classical pen and paper and computational
# exercises deal with simple motion problems and conservation laws;
# energy, momentum and angular momentum. These conservation laws are
# central in Physics and understanding them properly lays the foundation
# for understanding and analyzing more complicated physics problems.
# 
# The relevant reading background is
# 1. chapters 3, 4.1, 4.2 and 4.3 of Taylor (there are many good examples there) and
# 
# 2. chapters 10-13 of Malthe-Sørenssen.
# 
# In both textbooks there are many nice worked out examples. Malthe-Sørenssen's text contains also several coding examples you may find useful. 
# 
# The numerical homework focuses on another motion problem where you can
# use the code you developed in homework 3, almost entirely. Please take
# a look at the posted solution (jupyter-notebook) for homework 3. You
# need only to change the forces at play. The numerical problem this time is based
# on your code from homework 3 and we will try to make the motion of a falling object in two dimensions more realistic by allowing to bounce up again due to a normal force from the floor.

# ### Exercise 1 (10 pt), Conservation laws, Energy and momentum
# 
# * 1a (2pt) How do we define a conservative force?
# 
# * 1b (4pt) Use the work-energy theorem to show that energy is conserved with a conservative force.
# 
# * 1c (4pt) Assume that you have only internal two-body forces acting on $N$ objects in an isolated system. The force from object $i$ on object $j$ is $\boldsymbol{F}_{ij}$. Show that the linear momentum is conserved.

# ### Exercise 2 (10 pt), Conservation of angular momentum
# 
# * 2a (2pt) Define angular momentum and the torque for a single object with external forces only. 
# 
# * 2b (4pt) Define angular momentum and the torque for a system with $N$ objects/particles  with external and internal forces. The force from object $i$ on object $j$ is $\boldsymbol{F}_{ij}$.
# 
# * 2c (4pt) With internal forces only, what is the mathematical form of the forces that allows for angular momentum to be conserved?

# ### Exercise 3 (10pt), Example of potential
# 
# Consider a particle of mass $m$ moving according to the potential

# $$
# V(x,y,z)=A\exp\left\{-\frac{x^2+z^2}{2a^2}\right\}.
# $$

# * 3a (2pt) Is energy conserved? If so, why? 
# 
# * 3b (4pt) Which of  the quantities, $p_x,p_y,p_z$ are conserved?
# 
# * 3c (4pt) Which of  the quantities, $L_x,L_y,L_z$ are conserved?

# ### Exercise 4 (15pt), Angular momentum case
# 
# At $t=0$ we have a single object with position $\boldsymbol{r}_0=x_0\boldsymbol{e}_x+y_0\boldsymbol{e}_y$.We add also a force in the $x$-direction at $t=0$. We assume that the object is at rest at $t=0$.

# $$
# \boldsymbol{F} = F\boldsymbol{e}_x.
# $$

# * 4a (5pt) Find the velocity and momentum at a given time $t$ by integrating over time with the above initial conditions.
# 
# * 4b (5pt) Find also the position at a time $t$. 
# 
# * 4c (5pt) Use the position and the momentum to find the angular momentum and the torque. Is angular momentum conserved?

# ### Exercise 5 (15pt), forces  and potentials
# 
# A particle of mass $m$ has velocity $v=\alpha/x$, where $x$ is its displacement.
# 
# * 5a (5pt) Find the force $F(x)$ responsible for the motion.
# 
# A particle is thereafter under the influence of a force $F=-kx+kx^3/\alpha^2$, where $k$ and $\alpha$ are constants and $k$ is positive.
# 
# * 5b (5pt) Determine the potential $U(x)$  and discuss the motion. It can be convenient here to make a sketch/plot of the potential as function of $x$.
# 
# * 5c (5pt)  What happens when the energy of the particle is $E=(1/4)k\alpha^2$? Hint: what is the maximum value of the potential energy?

# ### Exercise 6 (40pt), Bouncing object
# 
# This exercise builds on the code you wrote for solving homework 3.
# There we introduced gravity and air resistance and studied their
# effects via a constant acceleration due to gravity and the force
# arising from air resistance. But what happens when the ball hits the
# floor? What if we would like to simulate the normal force from the
# floor acting on the ball?  This exercise shows how we can include more
# complicated forces with no pain! And the force we include here is an
# example of a case where analytical solutions may either be difficult
# to find or we cannot find an analytical solution at all.
# 
# We need then to include a force model for the normal force from the
# floor on the ball. The simplest approach to such a system is to
# introduce a contact force model represented by a spring model.  We
# model the interaction between the floor and the ball as a single
# spring. But the normal force is zero when there is no contact. Here we
# define a simple model that allows us to include such effects in our
# models.
# 
# The normal force from the floor on the ball is represented by a spring force. This
# is a strong simplification of the actual deformation process occurring at the contact
# between the ball and the floor due to the deformation of both the ball and the floor.
# 
# The deformed region corresponds roughly to the region of **overlap** between the
# ball and the floor. The depth of this region is $\Delta y = R − y(t)$, where $R$
# is the radius of the ball. This is supposed to represent the compression of the spring.
# Our model for the normal force acting on the ball is then

# $$
# \boldsymbol{N} = −k (R − y(t)) \boldsymbol{e}_y.
# $$

# The normal force must act upward when $y < R$,
# hence the sign must be negative.
# However, we must also ensure that the normal force only acts when the ball is in
# contact with the floor, otherwise the normal force is zero. The full formation of the
# normal force is therefore

# $$
# \boldsymbol{N} = −k (R − y(t)) \boldsymbol{e}_y,
# $$

# when $y(t) < R$ and zero when $y(t) \le R$.
# In the numerical calculations you can choose $R=0.1$ m and the spring constant $k=1000$ N/m.
# 
# * 6a (10pt) Identify the forces acting on the ball and set up a diagram with the forces acting on the ball. Find the acceleration of the falling ball now with the normal force as well.
# 
# * 6b (30pt) Choose a large enough final time so you can study the ball bouncing up and down several times. Add the normal force and compute the height of the ball as function of time with and without air resistance. Comment your results.

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
