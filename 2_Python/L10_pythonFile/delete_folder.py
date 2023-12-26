import os
path = '../myFile/A'

if os.path.exists(path):
    print("The directory exists")
    # remove directory
    #os.removedirs(path)