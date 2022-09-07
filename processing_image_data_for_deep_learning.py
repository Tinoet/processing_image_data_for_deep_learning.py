
"""Processing image data for Deep Learning.ipynb
**Topics:**

*   Reading an image file and converting it to a numpy array
*   Resizing an image
*   RGB to Grayscale conversion
"""

# getting an image using web get

!wget 'https://tractive.com/blog/wp-content/uploads/2016/04/puppy-care-guide-for-new-parents.jpg'

"""**Libraries that can be used for image processing:**

1. matplotlib.image

2. Pillow

3. OpenCV (cv2)
"""

# importing the image module from matplotlib library

import matplotlib.image as mpimg
import matplotlib.pyplot as plt

# loading an image through matplotlib.image module

img = mpimg.imread('/content/dog.jpg')

type(img)

print(img.shape)

print(img)

# displaying the image from numpy array

img_plot = plt.imshow(img)
plt.show()

"""Resizing the image using Pillow library"""

from PIL import Image

img = Image.open('/content/dog.jpg')
img_resized = img.resize((200, 200))

img_resized.save('dog_image_resized.jpg')

# displaying the image from numpy array

img_res = mpimg.imread('/content/dog_image_resized.jpg')
img_res_plot = plt.imshow(img_res)
plt.show()

print(img_res.shape)

"""**Converting RGB images to Grayscale image using OpenCV**"""

# importing OpenCV library
import cv2

img = cv2.imread('/content/dog.jpg')

type(img)

img.shape

grayscale_image = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

type(grayscale_image)

grayscale_image.shape

"""cv2.imshow() will display the image. But this will not be allowed in Google Colab.

**from google.colab.patches import cv2_imshow**
"""

from google.colab.patches import cv2_imshow

# displaying the image
cv2_imshow(grayscale_image)

# saving the grayscale image
cv2.imwrite('dog_grayscale_image.jpg', grayscale_image)

