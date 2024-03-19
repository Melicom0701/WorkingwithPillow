from PIL import Image
import IPython.display as display
import numpy as np
import webbrowser

def open_image(image_path):
    image = Image.open(image_path)
    return image
def display_image(image):
    image.save('temp.jpg')
    webbrowser.open('temp.jpg')

def imageToNumpy(image):
    numpy_array = np.array(image)
    return numpy_array
def convertRGBtoBWUsingNumpy(image):
    rgb_image = np.array(image)
    r,g,b = rgb_image[:,:,0], rgb_image[:,:,1], rgb_image[:,:,2]
    gamma = 1.04
    r_const, g_const, b_const = 0.2126, 0.7152, 0.0722
    black_white_image = (r_const * r**gamma + g_const * g**gamma + b_const * b**gamma)**(1/gamma)
    black_white_image = black_white_image.astype(np.uint8)
    return convertNumpyToImage(black_white_image)


def convertNumpyToImage(numpy_array):
    image = Image.fromarray(numpy_array)
    return image
def saveImage(image, name):
    image.save(name)

def assignment(directory):
    image = open_image(directory)
    numpy_array = imageToNumpy(image)
    black_white = convertRGBtoBWUsingNumpy(image)
    return black_white

dir = 'sunset-1373171_1280.jpg'
obj = assignment(dir)
display_image(obj)