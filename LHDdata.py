import numpy as np 
import matplotlib.pyplot

class LHDdata:
    # works for probe

    def __init__(self, fname):

        self.fname = fname
        self.read()

    def read(self):

        with open(self.fname) as f:
            datain = f.readlines()

        # get data line
        for j,line in enumerate(datain):
            if line.find("[data]") > 0 or line.find("[Data]") > 0:
                j_data = j
                break

        # get comments line
        j_comment = j_data # no comment, default
        for j,line in enumerate(datain):
            if line.find("[Comments]") > 0:
                j_comment = j
                break

        # parse data blocks
        parameters = datain[:j_comment]
        comments = datain[j_comment:j_data]
        b_data = datain[j_data+1:]

        params = {}
        for line in parameters:
            if line.find('=') > 0:
                key, val = line.split('=')
                
                key = key.strip()[2:]
                params[key] = val.strip()



        self.DimNo = int(params['DimNo'])
        self.DimSize = np.array(params['DimSize'].split(','),int)
        self.DimName = [tag.strip()[1:-1] for tag in params['DimName'].split(',')]
        self.ValNo = int(params['ValNo'])

        try:
            self.ValName = [tag.strip()[1:-1] for tag in params['ValName'].split(',')]
        except:
            self.ValName = [tag.strip()[1:-1] for tag in params['Valname'].split(',')]

        coms = [line[2:] for line in comments]

        try:
            data = np.array([line.strip().split(',') for line in b_data], float)
        except:
            # handle case with trailing comma
            data = np.array([line.strip().split(',')[:-1] for line in b_data], float)

        self.data_dict = {key:data[:i+1] for i,key in enumerate(self.ValName)}

        # save
        self.parameters = params
        self.comments = ''.join(coms)
        self.data = data[:,self.DimNo:]

        self.time = data[:,0]

        # save dimensions
        for i,key in enumerate(self.DimName):
            setattr(self,key,data[:,i])

        # save copy of traces
        for i,key in enumerate(self.ValName):
            if key:
                # skip if key is blank
                setattr(self,key,data[:,i+self.DimNo])
                # some times this has an issue if the data name has a python character like @ or -
