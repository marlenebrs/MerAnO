 
#!/usr/bin/python
#-*- coding: utf-8 -*-

import subprocess
import unittest

from merano import main_SBML, get_SBMLdoc_from_folder
from merano import main_analysis
from merano import make_dict
from merano import get_name_org

def test_filetype(filename, filetype):
  filename = filename.split('.')
  assert filename[-1] == filetype

def test_main_SBML():
    filetype = 'xml'
    results = main_SBML(get_SBMLdoc_from_folder())
    test_filetype(results, filetype)

def test_get_SBMLdoc_from_folder():
    filetype = 'xml'
    results = get_SBMLdoc_from_folder()
    for filename in filelist:
        test_filetype(filename, filetype)
      
def test_annotation():
    dict = {'Bacteroides_fragilis_YCH46': {'Carbohydrate metabolism': 8, 'Metabolism of cofactors and vitamins': 4, 'Energy metabolism': 2, 'Amino acid metabolism': 5}, 'Enterococcus_faecalis_V583': {'Nucleotide metabolism': 2, 'Gene set': 1, 'Amino acid metabolism': 5, 'Metabolism of cofactors and vitamins': 2, 'Biosynthesis of terpenoids and polyketides': 2}, 'Lactobacillus_plantarum_WCFS1': {'Amino acid metabolism': 2, 'Carbohydrate metabolism': 6, 'Metabolism of cofactors and vitamins': 5, 'Energy metabolism': 2, 'Lipid metabolism': 1, 'Nucleotide metabolism': 1, 'Gene set': 1}}
    files=(['../merano/Samples/Annotation_files/Bacteroides_fragilis_YCH46.annotations', '../merano/Samples/Annotation_files/Enterococcus_faecalis_V583.annotations','../merano/Samples/Annotation_files/Lactobacillus_plantarum_WCFS1.annotations'])
    data={}
    for f in files :
        data[get_name_org(f)] = make_dict(f)
    print (data)
    assert data == dict

test_annotation()
print('Done testing.')
