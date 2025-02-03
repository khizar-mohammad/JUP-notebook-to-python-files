#!/usr/bin/env python
# coding: utf-8

# In[24]:


import nbformat
from nbconvert import PythonExporter


with open('./drive/MyDrive/Colab Notebooks/Randomcodes.ipynb') as f:
        nb = nbformat.read(f, as_version=4)

exporter = PythonExporter()
(body, resources) = exporter.from_notebook_node(nb)

with open('exported_code.py', 'w') as f:
        f.write(body)

