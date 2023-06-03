# install pip install moviepy package

import moviepy.editor as mp
import os

path = input("Enter the path of the video : \n")

videoclip = mp.VideoFileClip(path)
audioclip = videoclip.audio
audioclip.write_audiofile("audio.mp3")
