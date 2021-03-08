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

alpha1=3
alpha2=1
alpha3=0.5
x=arange(0.025,6,0.025)
V=arange(0.025,6,0.025)
V=-alpha1/x + alpha2/(x*x)
V2=arange(0.025,6,0.025)
V2=-alpha3/(x*x*x)+2*alpha2/(x*x)


plt.plot(x,V,linestyle='-',linewidth=3,color='r')
plt.plot(x,V2,linestyle='-',linewidth=3,color='b')
ax.text(3.5, -1.7,'$U(r)=-\\alpha_1/r$',fontsize='20',ha='center',color='r')
ax.text(3, 0.7,'$U(r)=-\\alpha_2/r^3$',fontsize='20',ha='center',color='b')

ax.text(2.5, 3,'$V_{\\rm eff}(r)=U(r)+L^2/2mr^2$',fontsize='20',ha='center',color='k')

#ax.arrow(0, -3, 1.75, 0, head_width=0.5, head_length=0.25, shape='full', fc='k', ec='k')
#ax.arrow(2, -3, -1.75, 0, head_width=0.5, head_length=0.25, shape='full', fc='k', ec='k')

ax.tick_params(axis='both', which='major', labelsize=14)

ax.set_xticks(np.arange(-6,6,1), minor=False)
ax.set_xticklabels([], minor=False, family='serif')
ax.set_xticks(np.arange(-6,6,1), minor=True)
ax.axhline(linewidth=2, color='k', linestyle='--')
plt.xlim(0,5)

ax.set_yticks(np.arange(-6,10,2), minor=False)
ax.set_yticklabels(['','','','0'], minor=False, family='serif')
ax.set_yticks(np.arange(-10,10,2), minor=True)
plt.ylim(-5,7)

plt.xlabel('$r$', fontsize=30, weight='normal')
plt.ylabel('$V_{\\rm eff}(r)$',fontsize=30)
plt.subplots_adjust(top=0.85)
plt.savefig('Veff.pdf',format='pdf')
os.system('open -a Preview Veff.pdf')

#plt.show()
quit()
