import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np
import os
from pylab import *
from matplotlib import ticker
from matplotlib.ticker import ScalarFormatter
sformatter=ScalarFormatter(useOffset=True,useMathText=True)
sformatter.set_scientific(True)
sformatter.set_powerlimits((-2,3))

#plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))

font = {'family' : 'serif',
        'weight' : 'normal',
        'size'   : 14}
plt.rc('font', **font)
plt.rc('text', usetex=False)
plt.figure(figsize=(6,5))
fig = plt.figure(1)
ax = fig.add_axes([0.11,0.09,0.88,0.89])

alpha1=4
alpha2=1
x=arange(-6,6,0.1)
V=-alpha1*0.5*x*x+alpha2*0.25*x*x*x*x


plt.plot(x,V,linestyle='-',linewidth=3,color='r')
ax.text(1, -3.7,'$x_0$',fontsize='20',ha='center')

ax.arrow(0, -3, 1.75, 0, head_width=0.5, head_length=0.25, shape='full', fc='k', ec='k')
ax.arrow(2, -3, -1.75, 0, head_width=0.5, head_length=0.25, shape='full', fc='k', ec='k')

ax.tick_params(axis='both', which='major', labelsize=14)

ax.set_xticks(np.arange(-6,6,1), minor=False)
ax.set_xticklabels([], minor=False, family='serif')
ax.set_xticks(np.arange(-6,6,1), minor=True)
ax.axhline(linewidth=2, color='blue', linestyle='--')
plt.xlim(-4,4)

ax.set_yticks(np.arange(-6,10,2), minor=False)
ax.set_yticklabels(['','','','0'], minor=False, family='serif')
ax.set_yticks(np.arange(-10,10,2), minor=True)
plt.ylim(-5,10)

plt.xlabel('$x$', fontsize=30, weight='normal')
plt.ylabel('$V(x)$',fontsize=30)
plt.subplots_adjust(top=0.85)
plt.savefig('sombrero.pdf',format='pdf')
os.system('open -a Preview sombrero.pdf')

#plt.show()
quit()
