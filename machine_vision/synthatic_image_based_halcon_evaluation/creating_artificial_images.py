import numpy as np
from PIL import Image
from PIL import Image, ImageDraw

# Create a sample NumPy array
# data = np.random.randint(0, 255, (100, 100, 3))  # color images
data = np.random.randint(0, 255, (100, 100))  # Black and white image

# Convert data type to uint8 (optional, if needed)
data = data.astype(np.uint8)  

print(data.shape)
# Convert to PIL Image
image = Image.fromarray(data)

# Save as BMP
image.save('output.bmp')



# Create a new image
image2 = Image.new('RGB', (2000, 2000), (255, 255, 255))  # White background

# Create a drawing context
draw = ImageDraw.Draw(image2)

# Define the center and radius of the circle
center1 = (500,500)  # Center coordinates
center2 = (1000,1000)
radius = 50  # Radius

# Draw a black circle
#draw.ellipse(center1 + center2, fill='black', outline='black', width=1)
draw.ellipse([800,800,1200,1200], fill=(0,0,0), outline=(20,20,20), width=10)

#draw.circle(center, radius, fill='black')

# save image
image2.show()
image2.save('circle_image.bmp')


