#!/usr/bin/python
#-*- coding: utf-8 -*-

from request_database import list_modules

def get_name_org(f):
    """
    get name of each organism with filename

    :param f: name of one file "path/name.fa.emapper.annotation"
    :type f: str

    :return: organism's name
    :rtype: str
    """
    name = f.split(".")
    name = name[0]
    name = name.split("/")
    name = name[-1]
    return name



### Step 2 :  clean data

def clean_data(data):
    """
    processes data

    :param data: dictionnary with organism's name, modules and values
    :type data: dict

    :return: list [modules,label,values]
    :rtype: list
    """
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

def get_data_org(data):
    """
    processes data to get values for one organism

    :param data: dictionnary with organism's name, modules and values
    :type data: dict

    :return: list [modules,values]
    :rtype: list
    """
    modules=[]
    values=[]
    for key in data.keys():
        modules.append(key)
        values.append(data[key])
    return [modules,values]

def info_data(files,label,value):
    """
    
    percentage of loss and total of modules

    :param files: annotation files
    :type files: list 

    :param label: name of organism
    :type label: list

    :param value: total for each module
    :type value: list

    :return: list [label, percentage, total]
    :rtype: list
    """
    tab=[]
    percentage = []
    total=[]
    name=[]
    print(len(label))
    for o in range(len(label)):
        print(o)
        print(label[o])
        l=label[o]
        l=l.split('_')
        l=(l[0] + " "+ l[1])
        
        t=sum(value[o])

        len_id_modules = len(list_modules(files[o]))
            
        pct = t / len_id_modules * 100
        pct = 100 - pct
        name.append(l)
        total.append(t)
        percentage.append(pct)

    tab=[name, percentage, total]

    return tab