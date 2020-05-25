#!/usr/bin/python
#-*- coding: utf-8 -*-

### Importations
    ## Reportlab - To create pdf
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Image
from reportlab.platypus import PageBreak

    ## Import

import requests
import pandas as pd
import numpy as np
import pylab as plt
import json
import os


### Put in file "main.py"

if not os.path.exists('Results'):
    os.makedirs('Results')          # Create directory to put all results in 
if not os.path.isfile('modules.json'):
    with open("modules.json", mode='w') as f:
        f.write(json.dumps([], indent=4))   # Create json file


### Main for the analysis part

def main_analysis(files):

    """
    run analyses part

    Args:
        files (list) : files to process
    """
    print("Execution in progress...")
    data={}
    for f in files:                         # get dic with key=org's name 
        data[get_name_org(f)] = make_dict(f)         # value = nb of modules for each medium class
        
    data=clean_data(data) # prepare data to make charts
    modules=data[0]
    label=data[1]
    value=data[2]
    info=[]         # list with path and description for each file containing chart
    for i in range(len(label)):         # create chart for each organism
        tmp=make_barplot(modules,label[i],value[i])
        info.append(tmp)
        tmp=make_pie(modules,label[i],value[i])
        info.append(tmp)
        
    tmp=make_multiple_barplot(modules,label,value)  # create multiple chart
    info.append(tmp)
    create_pdf(info)        # create pdf




def get_name_org(f):
    """
    get name of each organism with filename

    args: 
        f (str): name of one file "path/name.fa.emapper.annotation"
    
    return:
        organism's name
    """
    name = f.split(".")
    name = name[0]
    name = name.split("/")
    name = name[-1]
    return name

### Step 1 :  get data

    ## 1.1 Get the modules list 

def list_medium_module(f):
    """
    get "medium" modules

    args:
        f (str): filename

    return:
        list of medium modules which  be request
    """
    modules_list = list_modules(f)

    medium_module = []

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


    ## 1.2 Get modules' id present within  annotation file

def list_modules(f):
    """
    get list of id module in annotation's file

    args:
        f (str): filename
    
    return:
        list of modules' id
    """

    csv = pd.read_csv(f, sep="\t", header=3, usecols=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])


    id_modules = []
    for i in range(len(csv)):
        temp = csv['KEGG_Module'][i]                          # stores each cell content of the 'KEGG_Module' column into a temporary variable
        if not pd.isnull(temp):                               # If the value is different of "NaN"
            value = str(csv['KEGG_Module'][i]).split(",")     # For the cells composed of different modules id -> split at the comma and stores them in a list
            for word in value:
                id_modules.append(word)

    return id_modules


       ## 1.3 Check if the modules are in JSON file 

def check_json(id):
    """
    find id in Json file

    args:
        id (str)

    return:
        name of medium class if id in json file
    """
    new=open('modules.json')
    load=json.load(new)
    for entry in load:
        if id == entry ['ID']:
            return entry ['medium']

        
        ## 1.4 If not in JSON file, requests KEGG 
    


def request_kegg(module):         
    """
    request kegg (database)

    args:
        module (str) : id of a module

    return:
        text from url page (str)
    """

    r = requests.get('http://rest.kegg.jp/get/%s' % module) # Returns informations on this url page 
    description = r.text
    return description

def read_text(module,text):  
    """  
    processing of the variable obtained with the request

    args:
        module (str) : id
        text (str) : return of request_kegg()
    return:
        list of str: [Class (3), module's name, id]
    """        
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


      ## 1.5 Update JSON function when id not in json file

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



    ## 1.6 - Create dictionary containing data to make charts

def make_dict(f):
    """
    sort data in a dictionnary

    args:
        f (str): filename
    
    return 
        {module: nb}
    """
    l=list_medium_module(f)
    data={}.fromkeys(l,0) #l is for the list and 0 initiate all the keys values
    for valeur in l:
        data[valeur]+=1
    return data


### Step 2 :  clean data

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
    

### Step 3 Making charts

    ## 3.1 Barplot to compare organism

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

    ## 3.2 Barplot for one organism

def make_barplot(modules,label,value):
    x=np.arange(len(modules))
    width=0.8

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

    ## 3.3 Pie chart represente proportion of modules in a organism

def make_pie(module,label,value):
    modules=np.array(module)
    values=np.array(value)
    fig, ax=plt.subplots(subplot_kw=dict(aspect='equal')) # Equal aspect ratio ensures the pie chart is circular.

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

    ax.set_title('Division of metabolisms within '+label)
    plt.legend(modules, bbox_to_anchor=(2,0), loc="lower left", bbox_transform=plt.gcf().transFigure)
    name=('pie_'+label)
    plt.savefig('./Results/'+ name, format='png')
    plt.close()
    description=('Pie chart illustrating the percent of each module present in '+label)
    return [name,description]
    

### Step 4 create pdf 

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

### run 

myFiles=['Samples/Annotation_files/Bacteroides_fragilis_YCH46.fa.emapper.annotations', 'Samples/Annotation_files/Enterococcus_faecalis_V583.fa.emapper.annotations','Samples/Annotation_files/Lactobacillus_plantarum_WCFS1.fa.emapper.annotations']

main_analysis(myFiles)
