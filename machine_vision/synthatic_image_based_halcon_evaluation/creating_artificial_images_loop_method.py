# create sinthatic image using python and calculate radius and x and y position.
# method works up to this image size. Now the memory is not enough to cualtate the imageing. 

import halcon as ha
import os
import numpy as np
from PIL import Image
from PIL import Image, ImageDraw
import math


image_size_in_pix_column    = 2592 
image_size_in_pix_row       = 2048
physical_size_of_pixel      = 475         # value is written in nm (nano meaters) 


# Create a sample NumPy array
# data = np.random.randint(0, 255, (100, 100, 3))  # color images
synthetic_image_np = np.zeros((image_size_in_pix_row, image_size_in_pix_column))    # Creating Black image
synthetic_image_np[:][:] = 255                                                # converting it to Creating white image

# Consider one pixel size is 0.475um or 475 nm
field_of_view_column = physical_size_of_pixel*image_size_in_pix_column
field_of_view_row = physical_size_of_pixel* image_size_in_pix_row

# Get the field of view (FOV)
print("field of view x (column): " + str(field_of_view_column/1000000) + " mm")
print("field of view Y (row): " + str(field_of_view_row/1000000) + " mm")

# get the center location
image_center_row = synthetic_image_np.shape[0] /2
image_center_column = synthetic_image_np.shape[1] /2


for x in range (0,image_size_in_pix_column,1):
    dx = x - image_center_row
    for y in range (0,image_size_in_pix_row,1):
        dy = y - image_center_column
        distance = math.sqrt(dy*dy + dx*dx)
        if distance < 526.3:
            synthetic_image_np[x][y] = 0
            #print (x,y)

#synthetic_image_np[image_center_row][image_center_column] = 0 


print(image_center_column, image_center_row)

# Convert data type to uint8 (optional, if needed)
image_array = synthetic_image_np.astype(np.uint8)  

# Convert to PIL Image
image = Image.fromarray(image_array)

# Save as BMP
image.save('output.bmp')



class method5:
    def __init__(self,image_path):
        self.image_path = image_path # dummy variable
        self.image = ha.read_image(self.image_path)

    def calculate_center(self):
        self.width,self.height=ha.get_image_size_s(self.image)
        print(self.width,self.height)

        # define the dot location
        Define_Circle_Row = 1024  
        Define_Circle_Column = 1295
        ha.gen_cross_contour_xld ( Define_Circle_Row, Define_Circle_Column, 30, 0.785398)
        CircleInitRadius = 525
        CircleRadiusTolerance = 50

        MetrologyHandle = ha.create_metrology_model()
        ha.set_metrology_model_image_size (MetrologyHandle, self.width, self.height)
        # MetrologyCircleIndices = ha.add_metrology_object_circle_measure (MetrologyHandle, Define_Circle_Row , Define_Circle_Column, CircleInitRadius, CircleRadiusTolerance, Thichness_of_the_box, sigma, measure_threshold, ['measure_distance'], [50] )
        MetrologyCircleIndices = ha.add_metrology_object_circle_measure (MetrologyHandle, Define_Circle_Row , Define_Circle_Column, CircleInitRadius, CircleRadiusTolerance, 20, 0.4, 1.8, ['measure_distance'], [40] )
        ha.set_metrology_object_param (MetrologyHandle, MetrologyCircleIndices, 'measure_transition', 'uniform')
        ha.apply_metrology_model (self.image, MetrologyHandle)
        CircleParameter = ha.get_metrology_object_result(MetrologyHandle, MetrologyCircleIndices, 'all', 'result_type', 'all_param')
        return CircleParameter

def list_bmp_files(directory='.'):
    # List to store .bmp file names
    bmp_files = []

    # Iterate through all files in the folder
    for filename in os.listdir(directory):
        if filename.lower().endswith('.bmp'):
            bmp_files.append(filename)

    return bmp_files


if __name__ == '__main__':

    calculator = method5("circle_image.bmp")
    CircleParameter = calculator.calculate_center()
    print(CircleParameter)

#   Get the current directory
#    current_directory = os.getcwd()
#
#    # List all .bmp files in the current directory
#    bmp_files = list_bmp_files(current_directory)
#
#    for bmp_file in bmp_files:
#
#        calculator = method5(bmp_file)
#        CircleParameter = calculator.calculate_center()
#
#        print(bmp_file,",   " , CircleParameter[0], ", " , CircleParameter[1], ",  " , CircleParameter[2] )











