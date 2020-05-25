 
#!/usr/bin/python
#-*- coding: utf-8 -*-

def test_filetype(filename, filetype):
  filename = filename.split('.')
  assert filename[-1] == filetype