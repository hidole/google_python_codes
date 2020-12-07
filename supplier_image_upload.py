#!/usr/bin/env python3
import requests
import os
# This example shows how a file can be uploaded using
# The Python Requests module

url = "http://35.232.86.7/upload/"
path =os.getcwd()
#print(path)
detail = "/supplier-data/images/"
path = path + detail
for subdir,dirs,files in os.walk(path):
  for file in files:
     if (".jpeg")in file:
        filename = path+file
        with open(filename, 'rb') as opened:
             r = requests.post(url, files={'file': opened})
