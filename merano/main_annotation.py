#!/usr/bin/python
#-*- coding: utf-8 -*-

from data_processing import *
from request_database import make_dict
from diagrams import*
from createPDF import create_pdf

import json

import os


### Put in file "main.py"



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



