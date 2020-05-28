#!/usr/bin/python
#-*- coding: utf-8 -*-


### Import

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Image
from reportlab.platypus import PageBreak
from reportlab.lib import colors




def create_pdf(charts,tab):
    """
    Create a pdf file with all charts

    :param charts: contain path and description for all charts
    
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

    l1=['organism']
    l2=['lost data (%)']
    l3=['total modules analysed']
    for i in range (len(tab[0])):
        l1.append(tab[0][i])
        l2.append(tab[1][i])
        l3.append(tab[2][i])
    
    data=[]
    data.append(l1)
    data.append(l2)
    data.append(l3)
    table=Table(data)

    style=TableStyle([('ALIGN',(0,0),(-1,-1),'CENTER')])
    ts=TableStyle([('BOX',(0,0),(-1,-1),2,colors.black),('GRID',(0,0),(-1,-1),2,colors.black)])
    table.setStyle(ts)
    table.setStyle(style)

    text = []
    text.append(Paragraph("Analyses of organism's pathways", stylesT))
    text.append(Spacer(0*cm,2*cm))
    text.append(table)
    text.append (PageBreak())
    comparison=0
    for i in range(len(charts)):
        title=charts[i][0]
        title=title.split('_')

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
