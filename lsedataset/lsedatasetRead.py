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
                    video = os.path.join(r, file)
                    posesPath = os.path.join(r, file) + '.json'
                    posesFiles = []
                    for rjson, djson, fjson in os.walk(posesPath):
                        for filejson in fjson:
                            if ('.json' in filejson):
                                posesFiles.append(os.path.join(rjson,filejson))
                    aux = lsedata.Lsedata(video,subtitle,posesFiles)
                    data.append(aux)
        return data

    def getElement(self):
        notvalid=True
        name=""
        name = input("Enter the name of the video: ")
        for r, d, f in os.walk(self.path):
            for file in f:
                if ('.mp4' in file)|('.webm' in file):
                    if (name in file):
                        video = os.path.join(r, file)
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
                        aux = lsedata.Lsedata(video,subtitle,posesFiles)
                        notvalid=False
                        return aux
        if (notvalid):
            print("Wrong file name, try again")
