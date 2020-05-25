 
#!/usr/bin/python
#-*- coding: utf-8 -*-

import subprocess
import unittest

from merano import main_SBML, get_SBMLdoc_from_folder
from merano import main_analysis

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

