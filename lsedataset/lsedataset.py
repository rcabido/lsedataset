import lsedatasetBuild
import lsedatasetRead
import lsedata
import dataset
from sys import argv
import os
import videoStruct

script = argv

def menu():
    print ("Choose an option")
    print ("\t1 - Build Dataset")
    print ("\t2 - Build Poses")
    print ("\t3 - Build Dataset since a key-word-search")
    print ("\t4 - List Dataset")
    print ("\t5 - Search File")
    print ("\t6 - Insert")
    print ("\t7 - Get")
    print ("\t8 - Load Chapters")
    print ("\t9 - Exit")

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

def readTriplet():
    valid=False
    name=""
    while(not valid):
        try:
            name = input("Enter the name of the file: ")
            urlsFile = open(name + '.txt', 'r').readlines()
            valid=True
        except FileNotFoundError:
            print("Wrong file name, try again")
    return name
 
exit = False
option = 0
os.chdir("../openpose/VideosTFG")
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
            build.downloadFile()
            #build.buildAllPoses()
            exit = True
    elif option == 2:
        build.buildAllPoses()
        exit = True
    elif option == 3:
        search = input("Enter the name to the search: ")
        build = lsedatasetBuild.lsedatasetBuild(search)
        build.downloadSearch()
        exit = True
    elif option == 4:
        print ("Loading dataset...")
        ######################
        #To loadPaths DataSet#
        ######################

        cwd = os.getcwd()
        read = lsedatasetRead.lsedatasetRead(cwd)
        data = read.load()
        for file in data:
            file.printPaths()
    elif option == 5:
        cwd = os.getcwd()
        read = lsedatasetRead.lsedatasetRead(cwd)
        data = read.load()
        element = read.getElement()
        if (element != None):
            element.printPaths()
    elif option == 6:
        save = dataset.DataSet()
        name = input("Enter the name of the field: ")
        value = input("Enter the value of the field: ")
        save.insert(name,value)
    elif option == 7:
        save = dataset.DataSet()
        name = input("Enter the name of the field: ")
        save.getValue(name)
    elif option == 8:
        fileName = readTriplet()
        videoStructure = videoStruct.VideoStruct(fileName)
        listWords = videoStructure.convertChapters()
        listWords = videoStructure.addVideoClips(listWords)
        print(videoStructure.addPoses(listWords)[0])
        #videoStructure.addPoses(listWords)
    elif option == 9:
        print("Exiting...")
        exit = True
    else:
        print ("Choose a correct option, try again")
 
print ("Terminated")

