import cv2
import numpy as np
import matplotlib.pyplot as plt

# Create a dummy image (a simple gradient image with a square and circle)
dummy_image = np.zeros((200, 200, 3), dtype=np.uint8)
cv2.rectangle(dummy_image, (50, 50), (150, 150), (0, 255, 0), -1)  # Green square
cv2.circle(dummy_image, (100, 100), 40, (255, 0, 0), -1)  # Blue circle
print(cv2.__version__)
print(np.__version__)
# Convert to grayscale
gray_image = cv2.cvtColor(dummy_image, cv2.COLOR_BGR2GRAY)

# Display the images using matplotlib
fig, axes = plt.subplots(1, 2, figsize=(8, 4))
axes[0].imshow(cv2.cvtColor(dummy_image, cv2.COLOR_BGR2RGB))  # Convert BGR to RGB for correct colors
axes[0].set_title("Original Image")
axes[0].axis("off")

axes[1].imshow(gray_image, cmap="gray")
axes[1].set_title("Grayscale Image")
axes[1].axis("off")

plt.show()
