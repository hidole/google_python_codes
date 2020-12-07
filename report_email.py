#!/usr/bin/env python3

import email.message
import mimetypes
import os.path
import smtplib
import reports
import Emails
from datetime import date
def main():
    src = "/supplier-data/descriptions/"
    path, listdata = reports.get_filedata(src)
    dataDic={}#[]
    strSum = ""
    for a in listdata:
        filepath = os.path.join(path, a)
        with open(filepath) as filedata:
            line = filedata.readlines()
            strSum = strSum + "<br/>"
            strSum = strSum + "name: "+line[0]+"<br/>"
            strSum = strSum + "weight: "+line[1] +"<br/>"
            #dataDic["name"]=line[0]
            #dataDic["weight"]= int(line[1].replace("lbs",''))
            #dataDic.append(["</br>"])
            #dataDic.append(["image: ",line[0]])
            #dataDic.append(["weight: ",line[1]])

            #print(strSum)
    today = date.today()
    _today = today.strftime("%B %d, %Y")
    print("Today's date:",_today)
    title_input = "Processed Update on " + str(_today)
    reports.generate_report("/tmp/processed.pdf",title_input,strSum)


    sender =  "automation@example.com"
    recipient = "student-01-3030eddf5177@example.com"  #userID = username
    subject_line = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    path_att = "/tmp/processed.pdf" #file path

    msg = Emails.generate_email(sender,recipient,subject_line,body,path_att)
    Emails.send_email(msg)

if __name__ == "__main__":
    main()

