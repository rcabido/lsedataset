class TextFile(object):
    def __init__(self,filename):
        self.fileName=filename

    def listUrls(self):
        if((self.fileName!=None)|(self.fileName=="")):
            f=open(self.fileName,'r')
            mesage=f.readlines()
            f.close()
            list=[]
            for linea in mesage:
                l=linea.rstrip('\n')
                print(l)
                list.append(l)
            return list
        else:
            raise Exception('The file name is wrong')
