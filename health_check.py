#!/usr/bin/env python3
import os
import Emails
import shutil
import psutil
import socket
import sched, time

schedule = sched.scheduler(time.time, time.sleep)
def do_every1min(sc):
    print("monitoring system every 1 minutes")
    #doing something here
    sys_monitor()

    schedule.enter(60,1,do_every1min,(sc,))


def sys_monitor():
    subject_statment =""
    #cpu usage >80%
    usg_CPU=psutil.cpu_percent(interval=1)
    if usg_CPU > 80:
        subject_statment = "Error - CPU usage is over 80%"

    #disk space <20%
    disk_usage = shutil.disk_usage('/')
    if disk_usage[2]/disk_usage[0]*100 <20:
        subject_statment = "Error - Available disk space is less than 20%"

    #available memory <500MB
    THRESHOLD = 500*1024*1024 #500MB
    mem_usage = psutil.virtual_memory()
    if mem_usage.available < THRESHOLD:
        subject_statment = "Error - Available memory is less than 500MB"


    #localhost == 127.0.0.1
    hostIP = socket.gethostbyname("localhost")
    if hostIP != "127.0.0.1":
        subject_statment = "Error - localhost cannot be resolved to 127.0.0.1"

    if subject_statment!="":
        """
        print("subject_statment is {}".format(subject_statment))
        print("CPU usage {}".format(usg_CPU))
        print(disk_usage[2]/disk_usage[0]*100)
        print(mem_usage.available >> 20 )
        print(socket.gethostbyname("localhost"))
        """

        sender =  "automation@example.com"
        recipient = "student-01-3030eddf5177@example.com"  #userID = username
        subject_line = subject_statment
        body = "Please check your system and resolve the issue as soon as possible."
        path_att = "" #file path #no attachment

        msg = Emails.generate_email(sender,recipient,subject_line,body,path_att)
        Emails.send_email(msg)



#schedule.enter(60,1,do_every1min, (schedule,))
#schedule.run()
sys_monitor()
