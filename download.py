import requests
import numpy as np

'''
This script batch downloads LHD data using url interface

path: variable where downloaded data is stored
diagnostics: list of analyzed data names
shot: range of shots

Tony Qian - 26 Nov 2025
'''

#shot = 195112
#diag = 'fig_h2'
path = "/Users/tqian/Documents/Physics/LHD/251126" # no trailing /

def download(shot, diag, path):

    url = f"https://exp.lhd.nifs.ac.jp/opendata/LHD/webapi.fcgi?cmd=getfile&diag={diag}&shotno={shot}&subno=1"
    response = requests.get(url, stream=True, timeout=30)
    if response.status_code == 200:
        with open(f"{path}/{diag}@{shot}_1.txt", "wb") as file:
            #file.write(response.content)
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    file.write(chunk)
        print(f"{shot} {diag} downloaded successfully.")
    else:
        print(f"Failed to download the {shot} {diag}.")


#diagnostics = ['shotinfo', 'PIPS_TAE']
#diagnostics = ['shotinfo', 'ichpw', 'gas_puf', 'echpw', 'nbpwr_tot_temporal', 'bolo', 'ha2', 'thomson', 'fircall']
diagnostics = ['PIPS_TAE_2d', 'FILD']
#diagnostics = ['fig_h2', 'bolo', 'bolo_all', 'thomson', 'fircall', 'DivIis_tor_sum']

# 2025 1126 experiments
# first shot 197825
# last shot 197967
for diag in diagnostics:
    for s in np.arange(825, 968):
        shot = 197000 + s
        download(shot,diag,path)
