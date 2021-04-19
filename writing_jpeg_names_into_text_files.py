import os
import glob

os.chdir(input("Enter a file directory: "))
prefix = input("Enter a prefix: ")
file_name = input("Enter a text file name: ")

all_files = os.listdir()  # Importing all files to a list
txt_files = glob.glob('*.txt', recursive=True)  # Taking only txt files from the directory into a list


jpeg_list = []
txt_list = []
# Checking if there is a txt file for each jpeg file in return.
for i in range(len(all_files) - 1):
    if all_files[i].split('.')[0] == all_files[i + 1].split('.')[0]:
        # If there is, appending to files into separate lists
        txt_list.append(all_files[i + 1])
        jpeg_list.append(all_files[i])


# Separating empty txt files from full txt files..
empty_txt_files = []
full_txt_files = []
for i in txt_list:
    if os.stat(i).st_size != 0:
        full_txt_files.append(i)
    else:
        empty_txt_files.append(i)


final_list = []
# There is a txt file for every jpeg file but in case of the txt file is empty,
# creating new list called final_list, and adding files into the list which contain texts inside of .txt files..
for i in jpeg_list:
    for j in full_txt_files:
        if i.split('.')[0] == j.split('.')[0]:
            final_list.append(i)


# Before writing a file, adding a prefix..
new_file = []
for file in final_list:
    new_file.append(prefix + file)


# Writing a names of jpeg files into txt file with prefixes..
with open(file_name + ".txt", "w") as f:
    f.writelines('%s\n' % jpg for jpg in new_file)
