import numpy as np
from PIL import Image

target_image = Image.open("course_4_Using_Databases_with_Python/img.png")
target_image_array = np.array(target_image)
pixels = target_image_array.reshape(-1, 3)

skip_indices = np.arange(101_600, 254_000)

indices_to_grey_out = np.delete(pixels, skip_indices, 0)

pixels_greyed_out = pixels.copy()
pixels_greyed_out[indices_to_grey_out, [0, 1, 2]] = 0

pixels_greyed_out = pixels_greyed_out.reshape(target_image_array.shape)
modified_img = Image.fromarray(pixels_greyed_out)
modified_img.show()