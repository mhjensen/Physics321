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

omega=arange(0,10,0.1)
omega0=5
beta=0.5
Asquared=arange(0,10,0.1)
for i in range(0,100):
  Asquared[i]=30*omega0*omega0/((omega0*omega0-omega[i]*omega[i])**2+4*beta*beta*omega[i]*omega[i])
  print('omega=',omega[i],' A^2=',Asquared[i])

plt.plot(omega,Asquared,linestyle='-',linewidth=3,color='r')
ax.text(6.6, 13.8,'FWHM',fontsize='20',ha='center')

ax.arrow(4.4, 15, 0.7, 0, head_width=0.5, head_length=0.25, fc='k', ec='k')
ax.arrow(5.4, 15, -0.7, 0, head_width=0.5, head_length=0.25, fc='k', ec='k')

ax.tick_params(axis='both', which='major', labelsize=14)

ax.set_xticks(np.arange(0,21,5), minor=False)
ax.set_xticklabels([], minor=False, family='serif')
ax.set_xticks(np.arange(0,21,1), minor=True)
plt.xlim(0.0,10)

ax.set_yticks(np.arange(0,40,40), minor=False)
ax.set_yticklabels([], minor=False, family='serif')
ax.set_yticks(np.arange(0,40,40), minor=True)
plt.ylim(0.0,32.0)

plt.xlabel('$\omega$', fontsize=24, weight='normal')
plt.ylabel('$x_{\\rm max}^2$',fontsize=30)
plt.subplots_adjust(top=0.85)
plt.savefig('qfactor.pdf',format='pdf')
os.system('open -a Preview qfactor.pdf')

#plt.show()
quit()
