import os
import re
import glob

input_path = "./"
files = []
glob_path = re.sub("([\[\]])", "[\g<1>]", input_path)
for file in glob.glob(glob_path + "*" + '.txt'):
    files.append(file)
    for file in files:
        root, extension = os.path.splitext(file)
        j=-1
        root2=root
        for idx, char in enumerate(reversed(root)):
            if(char == "\\" or char =="/"):
                j = len(root)-1 - idx
                break
        root=root0[j+1:]
        root0=root2[:j+1]
        print(root)

