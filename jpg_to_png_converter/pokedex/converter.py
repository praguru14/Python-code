import sys
import os
import glob
from PIL import Image

path1 = sys.argv[1]
path2 = sys.argv[2]
print(path1)

if not os.path.exists(path2):
    os.makedirs(path2)

for file in os.listdir(path1):
    print("hello")
