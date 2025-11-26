from LHDdata import LHDdata
import sys

import numpy as np
import matplotlib.pyplot as plt

'''
This script either plots a single FILD, or loops over N files
'''


fin = sys.argv[1]
_save = 0 

fig,axs = plt.subplots(4,4, figsize=(11,9))

def plot(fin,fig,axs):
    data = LHDdata(fin)
    
    shot = data.parameters['ShotNo']
    name = data.parameters['Name']
    unit = data.parameters['DimUnit'][1:-1]
    vunit = data.parameters['ValUnit'][1:-1].split(',')
   
    for j,a in enumerate(axs.T.flatten()):
        a.clear()
        a.plot(data.time, data.data[:,j], '.', ms=3)
        #a.plot(data.time, data.data[:,j], lw=0.7)
        a.set_title(data.ValName[j])
        a.set_xlabel("time "+unit)
        a.set_ylabel(vunit[j])
    
        a.set_xlim(2.75, 7)
    
    fig.suptitle(f"{shot} {name}")
    fig.tight_layout()
   
    #if _save:
    #    tag = fin.split('/')[-1][:-4]
    #    path = "/Users/tqian/Documents/Physics/LHD/fig"
    #    fout = f"{path}/{tag}.png"
    #    plt.savefig(fout)
    #    print("saved", fout)

    if _save:
        fname = f"../fig-2/fild-{shot}.png"
        plt.savefig(fname)
        print(f"saved {fname}")

# plot single
plot(fin,fig,axs)

# save scan
#in_path = "../251126"
#for s in np.arange(825, 968):
#    shot = 197000 + s
#    fin = f"{in_path}/FILD@{shot}_1.txt"
#    plot(fin, fig,axs)

plt.show()
