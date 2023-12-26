import os

path = '../myFile'

# os.listdir() method
all_files = os.listdir(path)
print(all_files)
for file in all_files:
    if os.path.isfile(os.path.join(path, file)):
        print("{} is a file".format(file))


# os.scandir() method
print("------------------------")
all_files = os.scandir(path)

for file in all_files:
    if file.is_file():
        print("{} is a file".format(file))



# using pathlib module
print("-------------------")
import pathlib

path_object = pathlib.Path(path)      # path object constructor
for file in path_object.iterdir():
    if file.is_file():
        print(file.name)
