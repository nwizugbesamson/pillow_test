#We can import some python libraries before starting to merge videos.
from moviepy.editor import VideoFileClip, concatenate_videoclips

#we use VideoFileClip() class create two video object, then we will merge them.
video_1 = VideoFileClip("VideoExample1.mp4")
video_2 = VideoFileClip("VideoExample2.mp4")

#Merge videos with concatenate_videoclips()
final_video= concatenate_videoclips([video_1, video_2])

final_video.write_videofile("final_video.mp4")