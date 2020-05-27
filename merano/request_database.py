#!/usr/bin/python
#-*- coding: utf-8 -*-

import pandas as pd
import requests
import json

### Step 1 :  get data

    ## 1.1 Get the modules list 

def list_medium_module(f):
    """
    get "medium" modules

    :param f: filename
    :type f: str

    :return: list of medium modules which be request
    :rtype: list
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
    
    :param f: filename
    :type f: str

    :return: list of modules' id
    :rtype: list
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
    
    :param id: module identifiant
    :type id: str

    :return: name of medium class if id in json file
    :rtype: str
    """
    new=open('Storage/modules.json')
    load=json.load(new)
    for entry in load:
        if id == entry ['ID']:
            return entry ['medium']

        
        ## 1.4 If not in JSON file, requests KEGG 
    


def request_kegg(module):         
    """
    request kegg (database)
    
    :param module: module identifiant
    :type module: str

    :return: text from url page (str)
    :rtype: str
    """

    r = requests.get('http://rest.kegg.jp/get/%s' % module) # Returns informations on this url page 
    description = r.text
    return description

def read_text(module,text):  
    """  
    processing of the variable obtained with the request
    
    :param module: module identifiant
    :type module: str
    
    :param text: return of request_kegg()
    :type text: str

    :return: list of str: [Class (3), module's name, id]
    :rtype: list
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
    """
    write json file

    :param data: text to put in json file
    :type data: str
    """
    f= open("Storage/modules.json",'w')
    json.dump(data, f, indent=4)
    f.close()

def update_json(liste):
    """
    update (add arg in) json file
    
    :param liste: liste (str): [pathways, name, id]
    :type liste: list
    """
    dico_modules = {}
    dico_modules['ID'] = liste[4]
    dico_modules['name'] = liste[3]
    dico_modules['little'] = liste[2]
    dico_modules['medium'] = liste[1]
    dico_modules['bigger'] = liste[0]

    with open("Storage/modules.json") as f:
        data = json.load(f)
        data.append(dico_modules)

    write_json(data)



    ## 1.6 - Create dictionary containing data to make charts

def make_dict(f):
    """
    sort data in a dictionnary
    
    :param f: filename
    :type f: str

    :return: dict of modules and occurrences {module: nb}
    :rtype: dict
    """
    l=list_medium_module(f)
    data={}.fromkeys(l,0) #l is for the list and 0 initiate all the keys values
    for valeur in l:
        data[valeur]+=1
    return data
