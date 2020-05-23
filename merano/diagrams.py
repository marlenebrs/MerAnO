#coding:utf8

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Image as im
from reportlab.platypus import PageBreak

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont


import requests
import pandas as pd
import numpy as np
# To install pandas: conda install pandas
import pylab as plt
import json
import os


# Excel file
myFiles=['Samples/Annotation_files/Bacteroides_fragilis_YCH46.fa.emapper.annotations', 'Samples/Annotation_files/Enterococcus_faecalis_V583.fa.emapper.annotations','Samples/Annotation_files/Lactobacillus_plantarum_WCFS1.fa.emapper.annotations']
#myFiles=['Samples/Annotation_files/query_seqs.fa.emapper.annotations']
if not os.path.exists('Results'):
    os.makedirs('Results')
if not os.path.isfile('modules.json'):
    with open("modules.json", mode='w') as f:
        f.write(json.dumps([], indent=4))

def main_analyses(files):
    
    data={}
    for f in files:
        data[get_name_org(f)] = make_dict(f)
    

#    data= {'Bacteroides_fragilis_YCH46': {'Carbohydrate metabolism': 221, 'Metabolism of cofactors and vitamins': 129, 'Energy metabolism': 164, 'Amino acid metabolism': 178, 'Nucleotide metabolism': 55, 'Glycan metabolism': 39, 'Gene set': 29, 'Lipid metabolism': 32, 'Biosynthesis of terpenoids and polyketides': 54, 'Biosynthesis of other secondary metabolites': 3, 'Xenobiotics biodegradation': 1}, 'Enterococcus_faecalis_V583': {'Nucleotide metabolism': 53, 'Gene set': 16, 'Amino acid metabolism': 115, 'Metabolism of cofactors and vitamins': 82, 'Biosynthesis of terpenoids and polyketides': 29, 'Glycan metabolism': 5, 'Carbohydrate metabolism': 190, 'Energy metabolism': 90, 'Lipid metabolism': 24, 'Xenobiotics biodegradation': 3, 'Biosynthesis of other secondary metabolites': 4}, 'Lactobacillus_plantarum_WCFS1': {'Amino acid metabolism': 179, 'Carbohydrate metabolism': 205, 'Metabolism of cofactors and vitamins': 86, 'Energy metabolism': 112, 'Lipid metabolism': 32, 'Nucleotide metabolism': 50, 'Gene set': 21, 'Biosynthesis of terpenoids and polyketides': 24, 'Biosynthesis of other secondary metabolites': 1, 'Glycan metabolism': 7, 'Xenobiotics biodegradation': 4, 'Module set': 2}}
    data=clean_data(data)
    modules=data[0]
    label=data[1]
    value=data[2]
    info=[]
    for i in range(len(label)):
        tmp=make_barplot(modules,label[i],value[i])
        info.append(tmp)
        tmp=make_pie(modules,label[i],value[i])
        info.append(tmp)
        
    tmp=make_multiple_barplot(modules,label,value)
    info.append(tmp)
    create_pdf(info)

 #   create_pdf(plot)

def get_name_org(f):
    name = f.split(".")
    name = name[0]
    name = name.split("/")
    name = name[-1]
    return name


############################# 1 - Generates the modules list present within the annotation file #############################
def list_modules(annotation_files):
    csv = pd.read_csv(annotation_files, sep="\t", header=3, usecols=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])


    id_modules = []
    for i in range(len(csv)):
        temp = csv['KEGG_Module'][i]                          # stores each cell content of the 'KEGG_Module' column into a temporary variable
        if not pd.isnull(temp):                               # If the value is different of "NaN"
            value = str(csv['KEGG_Module'][i]).split(",")     # For the cells composed of different modules id -> split at the comma and stores them in a list
            for word in value:
                id_modules.append(word)

    return id_modules

############################# 2 - Check if the modules are in the JSON file : check_json(module)#############################

def check_json(id):
    new=open('modules.json')
    load=json.load(new)
    for entry in load:
        if id == entry ['ID']:
            return entry ['medium']

############################# 3 - Creation of the update JSON function : update_json(dict_module) #############################
def write_json(data):
    f= open("modules.json",'w')
    json.dump(data, f, indent=4)
    f.close()

def update_json(liste):
    dico_modules = {}
    dico_modules['ID'] = liste[4]
    dico_modules['name'] = liste[3]
    dico_modules['little'] = liste[2]
    dico_modules['medium'] = liste[1]
    dico_modules['bigger'] = liste[0]

    with open("modules.json") as f:
        data = json.load(f)
        data.append(dico_modules)

    write_json(data)



############################# 4 - If not in JSON file, requests KEGG : request_kegg(module) & read_text(text) #############################

def request_kegg(module):         # Returns the information page about the module
    r = requests.get('http://rest.kegg.jp/get/%s' % module)
    description = r.text
    return description

def read_text(module,text):           # Returns the hierarchy Pathway Modules list for one particular module present in the CLASS section
    t = text.split("\n")
    value = str
    name = str
    for i in range(len(t)):
        if "NAME" in t[i]:
            name = t[i]
        if "CLASS" in t[i]:
            value = t[i]

    name = name.strip("NAME")
    name = name.strip()

    value = value.strip("CLASS")
    value = value.strip()
    value = value.split("; ")

    value.append(name)
    value.append(module)

    return value


############################# 5 - Creates a general list "data" containing all the "medium" pathway modules #############################


def list_medium_module(f):
    modules_list = list_modules(f)

    medium_module = []

#    with open("modules.json", mode='w') as f:
#        f.write(json.dumps([], indent=4))

    for i in modules_list:
        check = check_json(i)

        if check == None :
            description = request_kegg(i)
            if len(description) > 4:
                list_hierarchy = read_text(i,description)
                update_json(list_hierarchy)
                medium_module.append(list_hierarchy[1])

        else :
            medium_module.append(check)

    return medium_module




############################# 6 - Creates a dictionary containing as keys the name of each pathway module and as values the occurence of each module in the "data" list #############################

def make_dict(f):
    l=list_medium_module(f)
    data={}.fromkeys(l,0) #l is for the list and 0 initiate all the keys values
    for valeur in l:
        data[valeur]+=1
    return data

def clean_data(data):
    all_org=list(data.items())
    modules=list(all_org[0][1].keys())
    i=1
    while i < (len(all_org)):
        tmp=list(all_org[i][1].keys())
        for m in tmp:
            for j in modules:
                if m not in modules:
                    modules.append(m)
        i=i+1
    
    value=[]
    label=[]
    for org in all_org:
        value_org=[]
        label.append(org[0])
        o=list(org[1].items())
        for m in range(len(modules)):
            is_mod=0
            for mod in o:
                if modules[m] == mod[0]:
                    value_org.append(mod[1])
                    is_mod=1
            if is_mod==0:
                value_org.append(0)

        
        value.append(value_org)
    return [modules, label, value]
    

############################# 7 - Creating the plots from the collected data #############################

def make_multiple_barplot(modules,label,value):
    x=np.arange(len(modules))
    width=0.8
    #fig, ax = plt.subplots()
    n=len(value)
    for i in range(n):
        plt.bar(x - width/2. + i/float(n)*width, value[i], 
                width=width/float(n), align="edge", label=label[i])

    
    plt.xticks(x,modules,rotation=45,horizontalalignment='right',fontweight='light')
    plt.title('Division of metabolisms within the bacteria')
    plt.tight_layout()
    plt.legend()
    name='multiple_barplot'
    plt.savefig('./Results/'+name, format='png')
    plt.close()
    description='Comparaison of presence of modules in each organismes'
    return [name,description]

def make_barplot(modules,label,value):
    x=np.arange(len(modules))
    width=0.8
    #fig, ax = plt.subplots()
    
    plt.bar(x , value,width, align="edge", label=label)

    
    plt.xticks(x,modules,rotation=45,horizontalalignment='right',fontweight='light')
    plt.title('Division of metabolisms within ' + label)
    plt.tight_layout()
    plt.legend()
    name=('barplot_'+label)
    plt.savefig('./Results/'+name, format='png')
    plt.close()
    description=('Barplot illustrating the size of each module present in '+label)
    return [name,description]
''' 
def make_pie(modules, label,values):
    modules=np.array(modules)
    values=np.array(values)
    fig, ax=plt.subplots(subplot_kw=dict(aspect='equal')) # Equal aspect ratio ensures the pie chart is circular.
    #plt.pie(values)
    explode = (0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05)
    percent = 100.*values/sum(values)
    plt.pie(values,labels=percent, autopct='%1.1f%%', startangle=90, pctdistance=0.85, explode = explode)
    legende = ['{0} - {1:1.2f} %'.format(v,n) for v,n in zip(modules, percent)]
    ax.set_title('Division of metabolisms within '+ label)
#    plt.legend(legende, bbox_to_anchor=(1,0), loc="lower right", bbox_transform=plt.gcf().transFigure)
    name=('pie_'+label)
    plt.savefig('./Results/'+ name, format='png')
    plt.close()
    description=('Pie chart illustrating the percent of each module present in '+label)
    return [name,description]
'''
def make_pie(module,label,value):
    modules=np.array(module)
    values=np.array(value)
    fig, ax=plt.subplots(subplot_kw=dict(aspect='equal')) # Equal aspect ratio ensures the pie chart is circular.
    #plt.pie(values)
    bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
    wedges, texts = ax.pie(values, wedgeprops=dict(width=1), startangle=+40)
    kw = dict(arrowprops=dict(arrowstyle="-"),bbox=bbox_props, zorder=0, va="center")
    for i, p in enumerate(wedges):
        percent = 100.*values/sum(values)
        ang = (p.theta2 - p.theta1)/2. + p.theta1
        y = np.sin(np.deg2rad(ang))
        x = np.cos(np.deg2rad(ang))
        horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
        connectionstyle = "angle,angleA=0,angleB={}".format(ang)
        kw["arrowprops"].update({"connectionstyle": connectionstyle})
        ax.annotate(['{1:1.2f} %'.format(v,n) for v,n in zip(modules, percent)][i], xy=(x, y), xytext=(1.35*np.sign(x), 1.4*y),horizontalalignment=horizontalalignment, **kw)
    #labels = ['{0} - {1:1.2f} %'.format(v,n) for v,n in zip(modules, percent)]
    ax.set_title('Division of metabolisms within '+label)
    plt.legend(modules, bbox_to_anchor=(2,0), loc="lower left", bbox_transform=plt.gcf().transFigure)
    name=('pie_'+label)
    plt.savefig('./Results/'+ name, format='png')
    plt.close()
    description=('Pie chart illustrating the percent of each module present in '+label)
    return [name,description]
    

###################################### 8- create pdf #########################################

def create_pdf(images):
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
    for i in range(len(images)):
        title=images[i][0]
        title=title.split('_')
#        print(title)
        if i%2==0 and len(title)>2:
            text.append(Paragraph(title[1]+' ' +title[2], stylesH))
            text.append(Spacer(0*cm,0.5*cm))
            text.append(Paragraph('Description : ' + images[i][1], stylesN))
            text.append(Spacer(0*cm,0.5*cm))
        elif i%2!=0 and len(title)>2:
            text.append(Paragraph('Description : ' + images[i][1], stylesN))
            text.append(Spacer(0*cm,0.5*cm))

        else:
            if comparison==0:
                text.append(Paragraph('Comparison', stylesH))
                comparison=1
            text.append(Paragraph(images[i][1], stylesN))
            text.append(Spacer(0*cm,0.5*cm))
        path=('./Results/'+images[i][0])
        
        text.append(im(path, width=500))
        text.append(PageBreak())




    doc.build(text)

main_analyses(myFiles)
