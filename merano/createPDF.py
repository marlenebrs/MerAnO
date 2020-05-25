#!/usr/bin/python
#-*- coding: utf-8 -*-

### Import

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Image
from reportlab.platypus import PageBreak




def create_pdf(charts):
    """
    Create a pdf file with all charts

    Args:
        charts (list) : contain path and description for all charts
    
    """
    styles = getSampleStyleSheet()
    stylesN = styles['Normal']
    stylesH = styles['Heading1']
    stylesT = ParagraphStyle(
    'T',
    parent=styles['Title'],
    fontSize=25,
    leading=8,
    textColor='#3F9ED5 '

    )

    doc = SimpleDocTemplate("./Results/Report.pdf", pagesize=A4)


    text = []
    text.append(Paragraph("Analyses of organism's pathways", stylesT))
    text.append(Spacer(0*cm,2*cm))
    comparison=0
    for i in range(len(charts)):
        title=charts[i][0]
        title=title.split('_')
#        print(title)
        if i%2==0 and len(title)>2:
            text.append(Paragraph(title[1]+' ' +title[2], stylesH))
            text.append(Spacer(0*cm,0.5*cm))
            text.append(Paragraph('Description : ' + charts[i][1], stylesN))
            text.append(Spacer(0*cm,0.5*cm))
        elif i%2!=0 and len(title)>2:
            text.append(Paragraph('Description : ' + charts[i][1], stylesN))
            text.append(Spacer(0*cm,0.5*cm))

        else:
            if comparison==0:
                text.append(Paragraph('Comparison', stylesH))
                comparison=1
            text.append(Paragraph(charts[i][1], stylesN))
            text.append(Spacer(0*cm,0.5*cm))
        path=('./Results/'+charts[i][0])
        
        text.append(Image(path, width=500))
        text.append(PageBreak())




    doc.build(text)