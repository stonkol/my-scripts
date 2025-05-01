 ################################
# `pip install opencv-python`    #
# `brew install opencv` (macOS)  #
 ################################

# import cv2

# # Load the image
# img = cv2.imread('image.png')

# # Split the image into 9 equal parts
# for r in range(0, img.shape[0], img.shape[0]//3):
#     for c in range(0, img.shape[1], img.shape[1]//3):
#         # Save each part as a separate file
#         cv2.imwrite(f'part_{r}_{c}.png', img[r:r+img.shape[0]//3, c:c+img.shape[1]//3])
