import numpy as np
from PIL import Image

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