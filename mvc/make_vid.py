import cv2
import os

# # Construct the argument parser and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-ext", "--extension", required=False, default='png', help="extension name. default is 'png'.")
# ap.add_argument("-o", "--output", required=False, default='output.mp4', help="output video file")
# args = vars(ap.parse_args())

# Arguments
dir_path = 'data/Images'
output = 'data/Video/pic_to_img.mp4'

images = []
for f in os.listdir(dir_path):
    print(f)
    for _ in range(100):
        images.append(f) 
print(len(images))

# Determine the width and height from the first image
image_path = os.path.join(dir_path, images[0])
frame = cv2.imread(image_path)
# cv2.imshow('video',frame)
height, width, channels = frame.shape

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v') # Be sure to use lower case
out = cv2.VideoWriter(output, fourcc, 20.0, (width, height))

for image in images:

    image_path = os.path.join(dir_path, image)
    frame = cv2.imread(image_path)
    resized = cv2.resize(frame, (width, height))

    out.write(frame) # Write out frame to video
    print(image_path, resized.shape)

    # cv2.imshow('video',frame)
    if (cv2.waitKey(1) & 0xFF) == ord('q'): # Hit `q` to exit
        break

# Release everything if job is finished
out.release()
cv2.destroyAllWindows()

print("The output video is {}".format(output))