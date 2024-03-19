from PIL import Image
import IPython.display as display
import numpy as np
import webbrowser
# image1 = Image.open('sunset-1373171_1280.jpg')

# webbrowser.open('sunset-1373171_1280.jpg')

# image1.show()

''''
img = Image.new('RGB', (100, 100), color = (0,0,255))

img.save('pil_red.png')

webbrowser.open('pil_red.png')
'''

''''

img = Image.open('sunset-1373171_1280.jpg')

img.rotate(angle=60, fillcolor='white',expand=True,center = (100,100)).save('sunset-1373171_1280_rotated.jpg')

webbrowser.open('sunset-1373171_1280_rotated.jpg')
'''


image = Image.open('sunset-1373171_1280.jpg')
numpy_array = np.array(image)


