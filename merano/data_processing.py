#!/usr/bin/python
#-*- coding: utf-8 -*-


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