import lsedatasetBuild
import lsedatasetRead
import lsedata
import dataset
from sys import argv
import os

script = argv

def menu():
    print ("Choose an option")
    print ("\t1 - Build Dataset")
    print ("\t2 - Build Poses")
    print ("\t3 - List Dataset")
    print ("\t4 - Search File")
    print ("\t7 - Data Set")
    print ("\t5 - Insert")
    print ("\t6 - Get")
    print ("\t8 - Exit")

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
        os.chdir("..")
        os.chdir("openpose")
        if(not os.path.isdir("VideosTFG")):
            print("No hay videos descargados.")
            exit = True
        else:
            os.chdir("VideosTFG")
            build.buildPoses()
            exit = True
    elif option == 3:
        print ("Loading dataset...")
        ######################
        #To loadPaths DataSet#
        ######################

        cwd = os.getcwd()
        if ('lsedataset' in cwd):
            os.chdir("..")
            os.chdir("openpose/VideosTFG")
            cwd = os.getcwd()
        read = lsedatasetRead.lsedatasetRead(cwd)
        data = read.load()
        for file in data:
            file.printPaths()
    elif option == 4:
        cwd = os.getcwd()
        if ('lsedataset' in cwd):
            os.chdir("..")
            os.chdir("openpose/VideosTFG")
            cwd = os.getcwd()
        read = lsedatasetRead.lsedatasetRead(cwd)
        data = read.load()
        element = read.getElement()
        if (element != None):
            element.printPaths()
    elif option == 5:
        save = dataset.DataSet()
        name = input("Enter the name of the field: ")
        value = input("Enter the value of the field: ")
        save.insert(name,value)
    elif option == 6:
        save = dataset.DataSet()
        name = input("Enter the name of the field: ")
        save.getValue(name)
    elif option == 7:
        save = dataset.DataSet()
        save.hello()
        exit = True
    elif option == 8:
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
