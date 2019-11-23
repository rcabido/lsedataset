import crawler
from sys import argv
import os
from subprocess import call


script, fileName = argv

#crawl= crawler.Crawler(fileName)
#crawl.crawl()


os.chdir("..")
os.chdir("..")
os.chdir("openpose")
cwd = os.getcwd()
print(cwd+"JEJE")
files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(cwd):
    for file in f:
        if ('.mp4' in file)|('.webm' in file):
            files.append(os.path.join(r, file))
for f in files:
    print(f)
    os.rename(f, f.replace(" ", ""))
    path= f.replace(" ", "").split("tfg\\openpose\\")[1]
    print(path)
    params= " --video "+ path +" --face --hand --write_json " + path +".json"
    print("build\\x64\\Release\\OpenPoseDemo.exe"+params)
    #os.system(params)
    call("build/x64/Release/OpenPoseDemo.exe"+params, shell=False)
