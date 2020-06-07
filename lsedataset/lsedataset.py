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
    print ("\t1  - Build dataset since a file text")
    print ("\t2  - Build poses of local videos")
    print ("\t3  - Build dataset since a key-word-search")
    print ("\t4  - List local video dataset")
    print ("\t5  - Search path local video")
    print ("\t6  - List words in Data Base")
    print ("\t7  - Get word info")
    print ("\t8  - Insert video in Data Base")
    print ("\t9  - Delete word in Data Base")
    print ("\t10 - Exit")

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

def readTriplet():
    name=""
    try:
        name = input("Enter the name of the video: ")
        urlsFile = open(name + '.txt', 'r').readlines()
    except FileNotFoundError:
        print("Wrong file name, try again")
        name = ""
    return name

def readUrlsFile():
    name=""
    try:
        name = input("Enter the name of the file: ")
        urlsFile = open(name + '.txt', 'r').readlines()
    except FileNotFoundError:
        name = ""
        print("Wrong file name, try again")
    return name
 
exit = False
option = 0
os.chdir("../openpose/VideosTFG")
while not exit:
 
    menu()
 
    option = chooseOption()
 
    if option == 1:
        ###################################
        #To build the DataSet since a file#
        ###################################

        print ("Building dataset...")
        fileName = readUrlsFile()
        if (fileName != ""):
            build = lsedatasetBuild.lsedatasetBuild(fileName)
            build.downloadFile()

    elif option == 2:
        ###################
        #To capt all poses#
        ###################

        print ("Building poses...")
        build = lsedatasetBuild.lsedatasetBuild("local")
        build.buildAllPoses()
        
    elif option == 3:
        #####################################
        #To build the DataSet since a Search#
        #####################################

        search = input("Enter the name to the search: ")
        build = lsedatasetBuild.lsedatasetBuild(search)
        build.downloadSearch()
        
    elif option == 4:
        ###############################
        #To print local videos DataSet#
        ###############################

        print ("Loading dataset...")
        cwd = os.getcwd()
        read = lsedatasetRead.lsedatasetRead(cwd)
        data = read.load()
        for file in data:
            file.printName()

    elif option == 5:
        ########################
        #To print local DataSet#
        ########################

        cwd = os.getcwd()
        read = lsedatasetRead.lsedatasetRead(cwd)
        data = read.load()
        element = read.getElement()
        if (element != None):
            element.printPaths()

    elif option == 6:
        ########################
        #List words in DataBase#
        ########################

        save = dataset.DataSet()
        save.listWords()

    elif option == 7:
        #########################
        #Search word in DataBase#
        #########################

        save = dataset.DataSet()
        name = input("Enter the name of the field: ")
        save.getWord(name)

    elif option == 8:
        ##########################
        #Insert video in DataBase#
        ##########################

        fileName = readTriplet()
        if (fileName != ""):
            name = input("Do you want to use Stop Words filter? Y/N")
            if (name == 'Y'):
                videoStructure = videoStruct.VideoStruct(fileName, true)
            else:
                videoStructure = videoStruct.VideoStruct(fileName, false)
            listWords = videoStructure.convertChapters()
            listWords = videoStructure.addVideoClips(listWords)
            listWords = videoStructure.addPoses(listWords)
            save = dataset.DataSet()
            save.insertVideo(listWords)

    elif option == 9:
        #########################
        #Delete word in DataBase#
        #########################

        save = dataset.DataSet()
        name = input("Enter the name of the field: ")
        save.deleteWord(name)

    elif option == 10:
        #########
        #Exiting#
        #########

        print("Exiting...")
        exit = True

    else:
        print ("Choose a correct option, try again")
 
print ("Terminated")

