# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 21:34:53 2015

@author: pi
"""
import matplotlib.pyplot as plt
from astropy.table import Table
t=Table.read('/Volumes/PI/formula/py27/sn2011jh216_20120103.txt',format='ascii')
print t.colnames
plt.plot(t['col1'],t['col2'])