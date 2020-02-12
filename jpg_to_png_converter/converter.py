import sys
import os
from PIL import Image

path1 = sys.argv[1]
path2 = sys.argv[2]

if not os.path.exists(path2):
    os.makedirs(path2)

for filename in os.listdir(path1):
    if filename.endswith(".jpg"):
        # print(filename.split(".")[0])
        im = Image.open(f"{path1}{filename}")
        # print(Image.open(f"{path1}{filename}"))
        im.save(f"{path2}/{filename.split('.')[0]}.png", "png")
        print("Lets go")
