from LHDdata import LHDdata
import sys

import numpy as np
import matplotlib.pyplot as plt


fin = sys.argv[1]
_save = False

fig,axs = plt.subplots(5,5, figsize=(15,9))

def plot(fin,fig,axs):
    data = LHDdata(fin)
    
    shot = data.parameters['ShotNo']
    name = data.parameters['Name']
    unit = data.parameters['DimUnit'][1:-1]
    vunit = data.parameters['ValUnit'][1:-1].split(',')
   
    for j,a in enumerate(axs.flatten()):
        if j+1 > data.data.shape[1]:
            continue
        a.plot(data.time, data.data[:,j], '.', ms=3)
        #a.plot(data.time, data.data[:,j], lw=0.7)
        a.set_title(data.ValName[j])
        a.set_xlabel("time "+unit)
        a.set_ylabel(vunit[j])
    
        a.set_xlim(2.75, 7)
    
    fig.suptitle(f"{shot} {name}")
    fig.tight_layout()
   
    if _save:
        tag = fin.split('/')[-1][:-4]
        path = "/Users/tqian/Documents/Physics/LHD/fig"
        fout = f"{path}/{tag}.png"
        plt.savefig(fout)
        print("saved", fout)

plot(fin,fig,axs)

# save scan
#in_path = "../251016"
#for s in np.arange(85,144): 
#    shot = 195000 + s
#    fin = f"{in_path}/DivIis_tor_sum@{shot}_1.txt"
#    plot2(fin, fig2,axs2)
#    #plot(fin, fig,axs)

plt.show()
