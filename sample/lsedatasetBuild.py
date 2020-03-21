import crawler
import os
from subprocess import call

class lsedatasetBuild:

    def __init__(self, fileNameUrls):
        self.fileNameUrls = fileNameUrls

    def download(self):
        crawl= crawler.Crawler(self.fileNameUrls)
        crawl.crawl()

    def buildPoses(self):
        cwd = os.getcwd()
        if ('VideosTFG' not in cwd):
            os.chdir("VideosTFG")
        files = []
        # r=root, d=directories, f = files
        for r, d, f in os.walk(os.getcwd()):
            for file in f:
                if ('.mp4' in file)|('.webm' in file):
                    files.append(os.path.join(r, file))
        os.chdir("..")
        for f in files:
            print("Pose detection: " + f)
            os.rename(f, f.replace(" ", ""))
            path= f.replace(" ", "").split("openpose/")[1]
            params= " --video "+ path +" --display 0 --render_pose 0 --face --hand --write_json " + path +".json"
            os.chdir("..")
            os.chdir("openpose")
            call("./build/examples/openpose/openpose.bin"+params, shell=True)
