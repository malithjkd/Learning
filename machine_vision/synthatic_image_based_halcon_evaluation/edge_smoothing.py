import numpy as np
from PIL import Image
import math 

# Load the BMP image into a PIL Image object
image = Image.open('output_100.bmp')

# Convert the PIL Image object to a NumPy array
image_array = np.array(image)


#x = 85
#y = 59
#sum = int(image_array[x-1][y-1]) + int(image_array[x-1][y]) + int(image_array[x-1][y+1]) + int(image_array[x][y-1]) + int(image_array[x][y]) + int(image_array[x][y+1]) + int(image_array[x+1][y-1]) + int(image_array[x+1][y]) + int(image_array[x+1][y+1])
#print(int(image_array[x-1][y-1]), int(image_array[x-1][y]), int(image_array[x-1][y+1]))
#print(int(image_array[x][y-1]), int(image_array[x][y]), int(image_array[x][y+1]))
#print(int(image_array[x+1][y-1]), int(image_array[x+1][y]), int(image_array[x+1][y+1]))


# Print the shape of the NumPy array
print(image_array.shape)
image_size_in_pix_column = image_array.shape[0]
image_size_in_pix_row = image_array.shape[1]

hd_image = np.zeros((image_size_in_pix_row, image_size_in_pix_column))

image_center_column = image_size_in_pix_column / 2
image_center_row = image_size_in_pix_row / 2

count = 0

for x in range (1,image_size_in_pix_column-1,1):
    #dx = x - image_center_row
    for y in range (1,image_size_in_pix_row-1,1):
        sum = int(image_array[x-1][y-1]) + int(image_array[x-1][y]) + int(image_array[x-1][y+1]) + int(image_array[x][y-1]) + int(image_array[x][y]) + int(image_array[x][y+1]) + int(image_array[x+1][y-1]) + int(image_array[x+1][y]) + int(image_array[x+1][y+1])
        
        if image_array[x][y] == 255:
            if sum < 2041:
                count = 0
                for i in range (0,100,1):
                    dx = (x + i/100) - image_center_row
                    for j in range (0,100,1):
                        dy = (y + j/100) - image_center_column
                        distance = math.sqrt(dy*dy + dx*dx)
                        if distance < 350.00:
                            count = count + 1
                
                print(x, y, sum, count)
                hd_image[x][y] =255*(1 - count/10000)
            else:
                hd_image[x][y] = 255           
        else :
            hd_image[x,y] = 0


# Convert data type to uint8 (optional, if needed)
image_array_uint8 = hd_image.astype(np.uint8)  

# Convert to PIL Image
image = Image.fromarray(image_array_uint8)

# Save as BMP
image.save('output_100_hd.bmp')

