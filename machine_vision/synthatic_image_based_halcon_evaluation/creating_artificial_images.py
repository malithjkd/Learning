import numpy as np
from PIL import Image
from PIL import Image, ImageDraw



# Create a sample NumPy array
# data = np.random.randint(0, 255, (100, 100, 3))  # color images
# data = np.random.randint(0, 255, (100, 100))  # Black and white image

# Convert data type to uint8 (optional, if needed)
# data = data.astype(np.uint8)  

# print(data.shape)
# Convert to PIL Image
# image = Image.fromarray(data)

# Save as BMP
#image.save('output.bmp')

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


