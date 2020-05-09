class Lsedata(object):

    def __init__(self, video, subtitles, poses):
        self.video = video
        self.subtitles = subtitles
        self.poses = poses

    def printPaths (self):
        print('Video:')
        print(self.video)
        print('Subtitles:')
        print(self.subtitles)
        if (self.poses != []):
            print('Poses:')
        for file in self.poses:
            print(file)

    def printName(self):
        video = self.video.split("/")
        videoName = video[len(video)-1].replace(".mp4", "")
        print(videoName)
