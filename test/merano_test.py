 
#!/usr/bin/python
#-*- coding: utf-8 -*-

import subprocess
import unittest
import libsbml

from merano import main_sbml, read_sbml
#from merano import main_analysis
from merano import read_text,request_kegg
from merano import get_name_org
"""
def test_filetype(filename, filetype):
  filename = filename.split('.')
  assert filename[-1] == filetype
"""
"""
def test_main_SBML():
    filetype = 'xml'
    files = (['Samples/SBML_files/Bacteroides_fragilis_YCH46.xml', 'Samples/SBML_files/Enterococcus_faecalis_V583.xml','Samples/SBML_files/Lactobacillus_plantarum_WCFS1.xml'])
    results = main_sbml(files)
    test_filetype(results, filetype)
"""
"""
def test_read_sbml():
    #filetype = 'libsbml.SBMLDocument'
    filename = 'Samples/SBML_files/bacteroides_fragilis_YCH46.xml'
    results = read_sbml(filename)
    assert isinstance(results, libsbml.SBMLDocument)
"""    
"""  
def test_annotation():
    dict = {'Bacteroides_fragilis_YCH46': {'Carbohydrate metabolism': 8, 'Metabolism of cofactors and vitamins': 4, 'Energy metabolism': 2, 'Amino acid metabolism': 5}, 'Enterococcus_faecalis_V583': {'Nucleotide metabolism': 2, 'Gene set': 1, 'Amino acid metabolism': 5, 'Metabolism of cofactors and vitamins': 2, 'Biosynthesis of terpenoids and polyketides': 2}, 'Lactobacillus_plantarum_WCFS1': {'Amino acid metabolism': 2, 'Carbohydrate metabolism': 6, 'Metabolism of cofactors and vitamins': 5, 'Energy metabolism': 2, 'Lipid metabolism': 1, 'Nucleotide metabolism': 1, 'Gene set': 1}}
    files=(['Samples/Annotation_files/Bacteroides_fragilis_YCH46.fa.emapper.annotations', 'Samples/Annotation_files/Enterococcus_faecalis_V583.fa.emapper.annotations','Samples/Annotation_files/Lactobacillus_plantarum_WCFS1.fa.emapper.annotations'])
    data={}
    for f in files :
        data[get_name_org(f)] = make_dict(f)
    print (data)
    assert data == dict
"""
def test_get_name_org():
    filename='MerAnO/test/Samples/Annotation_files/Bacteroides_fragilis_YCH46.fa.emapper.annotations'
    name=filename.split(".")[0]
    name=name.split("/")[-1]
    results=get_name_org(filename)
    assert results == name

def test_read_text():
    module='M00088'
    text=request_kegg(module)
    list=['Pathway modules', 'Lipid metabolism', 'Lipid metabolism', 'Ketone body biosynthesis, acetyl-CoA => acetoacetate/3-hydroxybutyrate/acetone', 'M00088']
    results=read_text(module,text)
    assert results == list
    

#test_read_sbml()
#test_main_SBML()
#test_annotation()
test_get_name_org()
test_read_text()
print('Done testing.')
