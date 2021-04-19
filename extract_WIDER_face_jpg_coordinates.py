import os
import cv2
import glob


# Reading text files..
def readTxtFile():
    with open("C:\\Users\\berkg\\OneDrive\\Desktop\\wider_face_split\\wider_face_train_bbx_gt.txt", 'r') as f:
        lines = f.readlines()
    return lines


# Extracting coordinates and jpg names...
def parseNames(lines, finalPts, jpeg_list):
    #finalPts = []
    #jpeg_list = []
    for j in range(len(lines)):
        if "--" in lines[j]:
            jpeg_list.append(lines[j].strip())
        elif len(lines[j]) <= 5:
            currentNumber = int(lines[j])
            currentPointList = []
            for t in range(1, currentNumber + 1):
                currentPointList.append('1 ' + lines[j + t])
            finalPts.append(currentPointList)


# Changing jpeg names..
def getTextNames(jpeg_list):
    text_names = []
    for i in jpeg_list:
        text_names.append(i[i.index('/') + 1:])
    return text_names


# Taking height and width from images..
def get_image_size(text_names):
    imgSizeList = []
    for names in text_names:
        os.chdir("C:\\Users\\berkg\\OneDrive\\Desktop\\txt_files")
        image = glob.glob(f"{names}", recursive=True)
        for j in image:
            img = cv2.imread(j)
            h, w, _ = img.shape
            imgSizeList.append([h, w])
    return imgSizeList


# Scaling coordinates according to image shape..
def scale_point_values(finalPts, imgSizeList):
    scaled_points = []
    counter = 0
    h = imgSizeList[counter][0]
    w = imgSizeList[counter][1]

    for i in finalPts:
        tmp_scaled_points = []
        for j in i:
            columns = j.split()
            tmp_scaled_points.append([((int(columns[1]) + (int(columns[3])/2))/w), ((int(columns[2]) + (int(columns[4])/2))/h), int(columns[3])/w, int(columns[4])/h])

        scaled_points.append(tmp_scaled_points)
        counter += 1
    return scaled_points


# Changing text names, and writing coordinates to text files...
def create_text_file(jpeg_list, points_parsed):

    os.chdir("C:\\Users\\berkg\\OneDrive\\Desktop\\txt_files")
    txt_names = []
    for i in jpeg_list:
        txt_names.append(i[i.index('/')+1:i.index('.')])

    for names, points in zip(txt_names, points_parsed):
        f = open(names + ".txt", "w")
        for singlePnt in points:
            f.write('1 ')
            for coord in singlePnt:
                f.write(str( format(coord, '.8f') ))
                f.write(' ')
            f.write('\n')
        f.close()


lines = readTxtFile()
finalPts = []
jpeg_list = []
parseNames(lines, finalPts, jpeg_list)
text_names = getTextNames(jpeg_list)
imgSizeList = get_image_size(text_names)
points_parsed = scale_point_values(finalPts, imgSizeList)
create_text_file(jpeg_list, points_parsed)