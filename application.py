import os
import glob
import cv2
import numpy as np


os.chdir(input('Enter a file directory: '))
txt_files = glob.glob('*.txt', recursive=True)   # Taking only txt files from the directory into a list


# creating function to read .txt files
def map_lines(file_list):
    for file in file_list:
        with open(file, 'r') as fd:
            yield fd.readlines()


x_points = []
y_points = []
# Extracting x and y points from txt files..
for line in map_lines(txt_files):
    for items in line:
        columns = items.split()
        lookup_val_x = columns[1:2]
        lookup_val_y = columns[2:3]
        # Adding extracted points into new lists called x_points and y_points
        x_points.extend(lookup_val_x)
        y_points.extend(lookup_val_y)


# Scaling images..
img_width = 2464
img_height = 2056

x_points = [float(i) for i in x_points]
scaled_x_points = [i * img_width for i in x_points]
y_points = [float(i) for i in y_points]
scaled_y_points = [i * img_height for i in y_points]
# The x, y coordinates must be integers so that they can be drawn on the image..
rounded_x_points = [round(i) for i in scaled_x_points]
rounded_y_points = [round(i) for i in scaled_y_points]


# Drawing points on black image based on coordinate values x, y
image = np.zeros((img_height, img_width, 3), np.uint8)
for x, y in zip(rounded_x_points, rounded_y_points):
    cv2.circle(image, (x, y), 3, (0, 0, 255), -1)
    # cv2.imshow("Test", image)
    # cv2.waitKey(0)

cv2.imwrite("test.jpg", image)
