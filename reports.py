#!/usr/bin/env python3
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
import os

def get_filedata(detail):   #returing a path and list
    path = os.getcwd()
    path = path+detail
    print(path)
    listdata = os.listdir(path)
    print(listdata)
    return path , listdata

def generate_report(filename,title,data):
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(filename)
    pdf_body =[]
    #report.build(pdf_body)

    report_title = Paragraph(title, styles["h1"])
    #paragraph_1 = Paragraph("Some normal body text", styles["BodyText"])
    paragraph_1 = Paragraph(data, styles["BodyText"])
    pdf_body.append(report_title)
    pdf_body.append(paragraph_1)
    report.build(pdf_body)
