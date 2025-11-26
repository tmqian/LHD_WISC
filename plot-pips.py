from LHDdata import LHDdata
import sys

import matplotlib.pyplot as plt
import numpy as np

_save = True

fin = sys.argv[1]
data = LHDdata(fin)


shot = data.parameters['ShotNo']
name = data.parameters['Name']

time = data.Time
unit = data.parameters['ValUnit'][0] # uW

signal, error = data.data.T / 1e3 # convert to kcps

upper = signal + error
lower = signal - error

fig,axs = plt.subplots(1,1, figsize=(15,8))
axs.plot(time,signal, lw=0.5)
axs.fill_between(time, lower, upper, alpha=0.7, color='C1')
axs.set_title(f"{shot} PIPS")

axs.set_xlabel("time [s]", fontsize=14)
axs.set_ylabel("kcps", fontsize=14)
axs.grid()

if _save:
    fname = f"../fig-2/pips-{shot}.png"
    plt.savefig(fname)
    print(f"saved {fname}")
else:
    plt.show()

plt.show()
