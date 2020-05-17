from moviepy.editor import *
import base64
import os, sys

class VideoStruct(object):
    def __init__(self,filename):
        self.fileName=filename

    def convertChapters(self):
        if((self.fileName!=None)|(self.fileName=="")):
            f=open(self.fileName + '.txt','r')
            mesage=f.readlines()
            f.close()
            list=[]
            for linea in mesage:
                l=linea.rstrip('\n')
                if (l != ""):
                    try:
                        int(l)
                    except Exception as e:
                        if (l.find("-->") != -1):
                            time = l.split(" --> ")
                            triplet = {'start': time[0][:-1], 'end': time[1][:-1]}
                        else:
                            triplet['word'] = l
                            list.append(triplet)
            return list
        else:
            raise Exception('The file name is wrong')

    def addVideoClips(self, wordsList):
        try:
            if (len(wordsList) > 0):
                devnull = open(os.devnull, "w")
                old_stdout = sys.stdout
                sys.stdout = devnull
                for item in wordsList:
                    #print(item['word'] + item['start'])
                    video = VideoFileClip(self.fileName + ".mp4").subclip(item['start'],item['end'])
                    video.write_videofile(self.fileName + item['word'] + ".mp4",fps=25)
                    s = open(self.fileName + item['word'] + ".mp4", "rb")
                    e = base64.b64encode(s.read())
                    s.close()
                    item['video'] = e.decode('utf-8')
                    os.remove(self.fileName + item['word'] + ".mp4")
                sys.stdout = old_stdout
                devnull.close()  
            return wordsList
        except Exception as e:
             print(e)

    def addPoses(self, wordsList):
        try:
            if (len(wordsList) > 0):
                os.chdir(self.fileName + ".mp4.json")
                suPath = "_keypoints.json"
                for item in wordsList:
                    h, m, s = item['start'].split(":")
                    s = s.split(",")
                    start = int(h)*3600 + int(m)*60 + int(s[0])
                    he, me, se = item['end'].split(":")
                    se = se.split(",")
                    end = int(he)*3600 + int(me)*60 + int(se[0])
                    i = (start*25) + int(int(s[1])*0.25)
                    j = (end*25) + int(int(se[1])*0.25)
                    aux = len(str(i))
                    pathBase = self.fileName + "_"
                    while aux < 12:
                        pathBase = pathBase + "0"
                        aux = aux + 1
                    poseWord = ""
                    while i < j:
                        if len(str(i))> len(str(i-1)):
                            pathBase = pathBase[:-1]
                        path = pathBase + str(i) + suPath
                        try:
                            s = open(path, "r")
                            poseFile = s.read()
                            s.close()
                            poseWord = poseWord + poseFile + " \n"
                        except Exception as exc:
                            print(exc)
                        i = i + 1
                    item['poses'] = poseWord
            os.chdir("..")
            return wordsList
        except Exception as e:
             print(e)
