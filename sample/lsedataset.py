import lsedatasetBuild
import lsedatasetRead
import lsedata
from sys import argv
import os

script = argv

def menu():
	print ("Choose an option")
	print ("\t1 - Build Dataset")
	print ("\t2 - Load Dataset")
	print ("\t3 - Exit")

def chooseOption():
    valid=False
    num=0
    while(not valid):
        try:
            num = int(input("Choose an option: "))
            valid=True
        except ValueError:
            print('Option wrong, try again')
    return num

def readUrlsFile():
    valid=False
    name=""
    while(not valid):
        try:
            name = input("Enter the name of the file: ")
            urlsFile = open(name, 'r').readlines()
            valid=True
        except FileNotFoundError:
            print("Wrong file name, try again")
    return name
 
exit = False
option = 0
 
while not exit:
 
    menu()
 
    option = chooseOption()
 
    if option == 1:
        print ("Building dataset...")
        ######################
        #To build the DataSet#
        ######################
        while not exit:
            fileName = readUrlsFile()
            build = lsedatasetBuild.lsedatasetBuild(fileName)
            build.download()
            build.buildPoses()
            exit = True
    elif option == 2:
        print ("Loading dataset...")
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
        element = read.getElement()
        element.printPaths()
    elif option == 3:
        print("Exiting...")
        exit = True
    else:
        print ("Choose a correct option, try again")
 
print ("Terminated")


#build = lsedatasetBuild.lsedatasetBuild(fileName)
#build.download()
#build.buildPoses()

#cwd = os.getcwd()
#        if ('sample' in cwd):
#            os.chdir("..")
#            os.chdir("data")
#            cwd = os.getcwd()
#        read = lsedatasetRead.lsedatasetRead(cwd)
#        data = read.load()
#        for file in data:
#            file.printPaths()