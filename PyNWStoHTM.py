# -*- coding: utf-8 -*-
"""
Created on Tue Jul 09 14:35:06 2019

@author: guye0
"""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import requests
import time
import pytemperature

# Import API key
#from config import api_key

# Incorporated citipy to determine city based on latitude and longitude
#from citipy import citipy

Weather = pd.read_csv('cities.csv')
Stud_df = pd.DataFrame(Weather)
Stud_df.to_html('datapage111.html',index=False)