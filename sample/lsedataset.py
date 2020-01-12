import lsedatasetBuild
import lsedatasetRead
import lsedata
from sys import argv
import os

script, fileName = argv

        ######################
        #To build the DataSet#
        ######################

#build = lsedatasetBuild.lsedatasetBuild(fileName)
#build.download()
#build.buildPoses()

        ######################
        #To loadPaths DataSet#
        ######################

cwd = os.getcwd()
if ('sample' in cwd):
    os.chdir("..")
    os.chdir("data")
    cwd = os.getcwd()
read = lsedatasetRead.lsedatasetRead(cwd)
data = read.load()
for file in data:
    file.printPaths()
    

