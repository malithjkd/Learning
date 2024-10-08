import halcon as ha
import os

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
        Define_Circle_Row = 1090  
        Define_Circle_Column = 1320
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
    #img = ha.read_image('pcb')
    #img = "test"
    #calculator = method5(img)
    #calculator.calculate_reagens() 
    #CircleParameter = calculator.calculate_center()

    # Get the current directory
    current_directory = os.getcwd()

    # List all .bmp files in the current directory
    bmp_files = list_bmp_files(current_directory)

    for bmp_file in bmp_files:

        calculator = method5(bmp_file)
        CircleParameter = calculator.calculate_center()

        print(bmp_file,",   " , CircleParameter[0], ", " , CircleParameter[1], ",  " , CircleParameter[2] )

