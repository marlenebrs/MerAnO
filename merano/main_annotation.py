#!/usr/bin/python
#-*- coding: utf-8 -*-

from merano.data_processing import*
from merano.request_database import make_dict
from merano.diagrams import*
from merano.createPDF import create_pdf

import json

import os


### Put in file "main.py"



def main_analysis(files):

    """
    run analyses part

    :param files: files to process
    :type files: list
    """
    print("Execution in progress...Can take more than 10 minutes")
    data={}
    for f in files:                         # get dic with key=org's name 
        data[get_name_org(f)] = make_dict(f)         # value = nb of modules for each medium class
        

    info=[]         # list with path and description for each file containing chart
    mod_data=clean_data(data)
    modules=mod_data[0]
    label=mod_data[1]
    value=mod_data[2] 
    info=[]         # list with path and description for each file containing chart
    for i in range(len(label)):  # create chart for each organism 
        md=get_data_org(data[label[i]])   
        mod=md[0]
        val=md[1]
        tmp=make_barplot(mod,label[i],val)
        info.append(tmp)
        tmp=make_pie(mod,label[i],val)
        info.append(tmp)
        

    tmp=make_multiple_barplot(modules,label,value)  # create multiple chart
    info.append(tmp)
    tab=info_data(files,label,value)
    
    create_pdf(info,tab)        # create pdf
    print("Execution ok ... output files are in directory named \"Results\"")



