import os
path = 'testfile.txt'
# check if the file exist
if os.path.isfile(path):
    print("The file is exist")
else:
    print("The file doesn't exist")


# delete file
if os.path.isfile(path):
    os.remove(path)
else:
    print("The file doesn't exist")

