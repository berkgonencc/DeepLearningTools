import os
import glob
import cv2
from shutil import copyfile


# creating function to read .txt files
def map_lines(file_list):
    for file in file_list:
        with open(file, 'r') as fd:
            yield fd.readlines()


os.chdir("C:\\Users\\berkg\\OneDrive\\Desktop\\all_files")  # Changing directory..
txt_files = glob.glob('*.txt', recursive=True)  # Taking only txt files...


# Converting coordinates to YoloV4 format and adding them to the list called yolo_points..
def convert_yolo_format(txt_files):
    yolo_points = []
    for line in map_lines(txt_files):
        points = []
        for items in line:
            columns = items.split()
            if len(columns) > 1 and columns[0] == '1':
                points.append([int(columns[1]) + (int(columns[3]) - int(columns[1])) / 2,
                               int(columns[2]) + (int(columns[4]) - int(columns[2])) / 2,
                               int(columns[3]) - int(columns[1]),
                               int(columns[4]) - int(columns[2])])

        yolo_points.append(points)
    return yolo_points


os.chdir("C:\\Users\\berkg\\OneDrive\\Desktop\\all_files")
all_files = os.listdir()  # Importing all files to a list


# Checking if there is a txt file for each jpeg file in return..
def separate_existing_txt_lists(all_files, jpg_list, txt_list):
    # jpg_list = []
    # txt_list = []
    for i in range(len(all_files) - 1):
        if all_files[i].split('.')[0] == all_files[i + 1].split('.')[0]:
            # If there is, appending to files into separate lists
            txt_list.append(all_files[i + 1])
            jpg_list.append(all_files[i])


# Taking height and width from images..
def get_image_size(jpg_list):
    img_size_list = []
    for names in jpg_list:
        img = cv2.imread(names)
        h, w, _ = img.shape
        img_size_list.append([h, w])
    return img_size_list


# Scaling coordinates according to image shape..
def scale_point_values(yolo_points, img_size_list):
    scaled_points = []
    counter = 0
    h = img_size_list[counter][0]
    w = img_size_list[counter][1]

    for i in yolo_points:
        tmp_scaled_points = []
        for columns in i:
            tmp_scaled_points.append([int(columns[0]) / w, int(columns[1]) / h, int(columns[2]) / w, int(columns[3]) / h])

        scaled_points.append(tmp_scaled_points)
        counter += 1

        if counter < len(img_size_list):
            h = img_size_list[counter][0]
            w = img_size_list[counter][1]

    return scaled_points


def create_text_file(jpg_list, points_parsed):

    os.chdir("C:\\Users\\berkg\\OneDrive\\Desktop\\txt_files")
    txt_names = []
    for i in jpg_list:
        txt_names.append(i[:i.index('.')])

    for names, points in zip(txt_names, points_parsed):
        src = "C:\\Users\\berkg\\OneDrive\\Desktop\\all_files\\" + names + ".jpg"
        dst = "C:\\Users\\berkg\\OneDrive\\Desktop\\Images\\" + names + ".jpg"
        copyfile(src, dst)  # Copying images which have full text files from source to another file..
        f = open(names + ".txt", "w")
        for singlePnt in points:
            f.write('1 ')
            for coord in singlePnt:
                f.write(str( format(coord, '.8f') ))
                f.write(' ')
            f.write('\n')
        f.close()


yolo_points = convert_yolo_format(txt_files)
jpg_list = []
txt_list = []
separate_existing_txt_lists(all_files, jpg_list, txt_list)
img_size_list = get_image_size(jpg_list)
points_parsed = scale_point_values(yolo_points, img_size_list)
create_text_file(jpg_list, points_parsed)
