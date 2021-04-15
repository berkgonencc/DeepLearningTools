"""

"""
import os
import numpy as np


with open("C:\\Users\\berkg\\OneDrive\\Desktop\\debugData_1.txt", 'r') as f:
    lines = f.readlines()

numbers = []
finalPts = []
jpeg_list = []
for j in range(len(lines)):
    coordinates = []
    test = []
    if "--" in lines[j]:
        jpeg_list.append(lines[j])
    elif len(lines[j]) <= 5:
        currentNumber = int(lines[j])
        currentPointList = []
        for t in range(1, currentNumber+1):
            currentPointList.append(lines[j+t])
        finalPts.append(currentPointList)

print(jpeg_list)
print(finalPts)



#range([start], stop[, step])

"""
# print(numbers)
new_list = []
for i in range(len(numbers)):
    n = int(numbers[i].strip())
    new_list.append(n)

print(new_list)

"""
