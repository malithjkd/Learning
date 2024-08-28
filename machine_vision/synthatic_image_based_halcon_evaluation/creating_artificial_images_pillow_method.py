# create sinthatic image using python and calculate radius and x and y position.
# method works up to this image size. Now the memory is not enough to cualtate the imageing. 




import halcon as ha
import os
import numpy as np
from PIL import Image
from PIL import Image, ImageDraw


# Create a new image
# image =Image.nre('RGB', (column, rows),)
image2 = Image.new('RGB', (12312, 9728), (255, 255, 255))  # White background

# Create a drawing context
draw = ImageDraw.Draw(image2)

# Draw a black circle
#draw.ellipse(center1 + center2, fill='black', outline='black', width=1)
draw.ellipse([3656,2364,8656,7364], fill=(0,0,0), outline=(20,20,20), width=0)

# Convert to grayscale (black and white)
image2 = image2.convert('L')

# Resize the image to 260x200 pixels
new_image = image2.resize((2592, 2048), Image.LANCZOS)      # compress the image 

# save image
new_image.show()
new_image.save('circle_image.bmp')



class method5:
    def __init__(self,image_path):
        self.image_path = image_path # dummy variable
        #self.image = ha.read_image(r"C:\Users\mj.j\OneDrive - PBA Systems Pte. Ltd\GitHub\Github\2D_optical_vision_mapping\assets\logos\PBA_logo.png")
        #self.image = ha.read_image(r"C:\Users\mj.j\OneDrive - PBA Systems Pte. Ltd\Malith - R&D\dot_center_calcualtion\images\Pic_2024_07_30_092609_53")
        #self.image = ha.read_image("Pic_2024_07_30_092609_53.bmp")
        self.image = ha.read_image(self.image_path)

    def calculate_reagens(self):
        region = ha.threshold(self.image_path, 0, 122)
        num_regions = ha.count_obj(ha.connection(region))
        print(f'Number of Regions: {num_regions}')

    def calculate_center(self):
        self.width,self.height=ha.get_image_size_s(self.image)
        #print(self.width,self.height)

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

    # Get the current directory
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











