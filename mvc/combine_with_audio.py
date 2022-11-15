"""
this function will combine audio and video files to file named Output_Video.MP4
in output folder created in the same directory you are running this function from
"""
### for more information for advance use check moviepy documentation ###
### https://zulko.github.io/moviepy/getting_started/getting_started.html ###

from moviepy.editor import *
import os
def combine_audio_video(audiofile,videofile,output_file_name_with_extension):
  download_path = os.getcwd()
  videoclip = VideoFileClip(videofile)
  audioclip = AudioFileClip(audiofile)
  video = videoclip.set_audio(audioclip)
  if not os.path.exists(f'{download_path}\\output'): # if directory output dosen't
      os.makedirs(f'{download_path}\\output')        # exist create it
  video.write_videofile(f'{download_path}\\output\\{output_file_name_with_extension}')
  while True: ### check if audio and video files are closed to delete them
      try:
          myfile = open(f'{download_path}\\{files[1]}', "r+")
          myfile.close()
          os.remove(f'{download_path}\\{audiofile}')
          os.remove(f'{download_path}\\{videofile}')
          break                             
      except IOError:
          pass