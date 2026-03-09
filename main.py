import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1. Load image in grayscale
img = cv2.imread('input_image.png', 0)

if img is not None:
    # 2. Calculate Histogram and CDF
    hist, bins = np.histogram(img.flatten(), 256, [0, 256])
    cdf = hist.cumsum()

    # 3. Normalization (Scaling to 0-255)
    cdf_m = np.ma.masked_equal(cdf, 0)
    cdf_m = (cdf_m - cdf_m.min()) * 255 / (cdf_m.max() - cdf_m.min())
    cdf = np.ma.filled(cdf_m, 0).astype('uint8')

    # 4. Map original pixels to new values
    result_img = cdf[img]

    # 5. Visualization
    plt.figure(figsize=(12, 6))
    plt.subplot(121), plt.imshow(img, cmap='gray'), plt.title('Original')
    plt.axis('off')
    plt.subplot(122), plt.imshow(result_img, cmap='gray'), plt.title('Equalized')
    plt.axis('off')
    
    # Save the result before showing
    plt.savefig('output_result.png')
    plt.show(block=True)
    plt.show()
else:
    print("Error: Image not found!")