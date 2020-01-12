import lsedata
import os

class lsedatasetRead:

    def __init__(self, path):
        self.path = path

    def load(self):
        data = []
        for r, d, f in os.walk(self.path):
            for file in f:
                if ('.mp4' in file)|('.webm' in file):
                    if ('.mp4' in file):
                        subtitle = os.path.join(r, file).replace('.mp4','.txt')
                    else:
                        subtitle = os.path.join(r, file).replace('.webm','.txt')
                    posesPath = os.path.join(r, file) + '.json'
                    posesFiles = []
                    for rjson, djson, fjson in os.walk(posesPath):
                        for filejson in fjson:
                            if ('.json' in filejson):
                                posesFiles.append(os.path.join(rjson,filejson))
                    aux = lsedata.Lsedata(os.path.join(r, file),subtitle,posesFiles)
                    data.append(aux)
        return data