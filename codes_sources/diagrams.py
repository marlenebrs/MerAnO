import requests
import pandas as pd
import numpy as np
# To install pandas: conda install pandas
import pylab as plt
import json


# Excel file
#myFile = '/Users/marlenebarus/Master1/Semestre8/PdP/eggnog/Lactobacillus/query_seqs.fa.emapper.annotations'

############################# 1 - Generates the modules list present within the annotation file #############################
def list_modules(fichier_annotations):
    csv = pd.read_csv(fichier_annotations, sep="\t", header=3, usecols=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])

    modules = []
    for i in range(len(csv)):
        temp = csv['KEGG_Module'][i]                          # stores each cell content of the 'KEGG_Module' column into a temporary variable
        if not pd.isnull(temp):                               # If the value is different of "NaN"
            value = str(csv['KEGG_Module'][i]).split(",")     # For the cells composed of different modules id -> split at the comma and stores them in a list
            for word in value:
                modules.append(word)

    return modules

############################# 2 - Verifies if the modules are in the JSON file : check_json(module)#############################

def check_json(id):
    new=open('modules.json')
    load=json.load(new)
    for l in range (len(load)) :
        name=load[l]
        name=name.get('ID')
        if id in name:
            path=load[l].get('medium')
            return (path)

############################# 3 - Creation of the update JSON function : update_json(dict_module) #############################
def write_json(data):
    with open("modules.json", mode='w') as f:
        json.dump(data, f, indent=4)

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


############################# 4 - If not in JSON file, requests KEGG : request_kegg(module) et read_text(text) #############################

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


def list_medium_module():
    with open("modules.json", mode='w') as f:
        f.write(json.dumps([], indent=4))

    myFile = '/Users/marlenebarus/Master1/Semestre8/PdP/eggnog/Lactobacillus/query_seqs.fa.emapper.annotations'
    modules_list = list_modules(myFile)
    print(modules_list)

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
        print(medium_module)

    return medium_module

list_medium_module()


############################# 6 - Creates a dictionary containing as keys the name of each pathway module and as values the occurence of each module in the "data" list #############################

def make_dict():
    l=list_medium_module()
    compte={}.fromkeys(l,0) #l is for the list and 0 initiate all the keys values
    for valeur in l:
        compte[valeur]+=1
    print (compte)

make_dict()
