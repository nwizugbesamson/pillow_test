## https://www.tutorialspoint.com/python_pillow/Python_pillow_merging_images.htm

from PIL import Image
#Read the two images
image1 = Image.open('images/elephant.jpg')
image1.show()
image2 = Image.open('images/ladakh.jpg')
image2.show()
#resize, first image
image1 = image1.resize((426, 240))
image1_size = image1.size
image2_size = image2.size
new_image = Image.new('RGB',(2*image1_size[0], image1_size[1]), (250,250,250))
new_image.paste(image1,(0,0))
new_image.paste(image2,(image1_size[0],0))
new_image.save("images/merged_image.jpg","JPEG")
new_image.show()