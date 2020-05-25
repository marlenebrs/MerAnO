 
#!/usr/bin/python
#-*- coding: utf-8 -*-

import subprocess
import unittest

from merano import main_analysis

def test_filetype(filename, filetype):
  filename = filename.split('.')
  assert filename[-1] == filetype
