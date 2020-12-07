#!/usr/bin/env python3
from PIL import Image
import os

path = os.getcwd()
dest = "/opt/icons/"
#print(path)
detail = "/supplier-data/images/"
path =path+detail
print(path)


for subdir,dirs,files in os.walk(path):
  for file in files:
     if (".tiff")in file:
        filename = path+file
        print(filename)
        im = Image.open(filename)
        im = im.convert('RGB')
        imcov = im.rotate(90).resize((600,400))
        file_nodot = file.replace(".tiff",'')
        imcov.convert("RGB").save(path+file_nodot+".jpeg")
