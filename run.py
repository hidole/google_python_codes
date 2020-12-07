#!/usr/bin/env python3
import os
import requests
import json


#detail="/supplier-data/descriptions/"
#detail="/descriptions/"

def get_filedata(detail):   #returing a path and list
    path = os.getcwd()
    path = path+detail
    print(path)
    listdata = os.listdir(path)
    print(listdata)
    return path , listdata

def process_post_data(src_detail,destURL):
    path, listdata = get_filedata(src_detail)
    dataDic={}
    list_column = ["name","weight","description", "image_name"]
    index_column=0

    total_data =[]

    for a in listdata:
        filepath = os.path.join(path, a)
        with open(filepath) as filedata:
            line = filedata.readlines()
            dataDic["name"]=line[0]
            dataDic["weight"]= int(line[1].replace("lbs",''))
            dataDic["description"]=line[2]
            dataDic["image_name"]=a.replace("txt","jpeg")

            print(dataDic)
            response = requests.post(destURL, json=dataDic)
            print(response.status_code)
            dataDic.clear()
            filedata.close()

detail="/supplier-data/descriptions/"
#src = "/descriptions/"
destURL = "http://35.232.86.7/fruits/"

process_post_data(detail, destURL)
