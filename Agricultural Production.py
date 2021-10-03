#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from ipywidgets import interact


# In[11]:


data = pd.read_csv("C:/Users/jghantt/Desktop/New folder/Data Science/Agri Project/data.csv")


# In[12]:


data.shape


# In[13]:


data.head()


# In[14]:


data.isnull().sum()


# In[15]:


data['label'].value_counts()


# In[21]:


print("Average Ratio of Nitrogen in the soil : {0:.2f}".format(data['N'].mean()))
print("Average Ratio of Phosphorous in the soil : {0:.2f}".format(data['P'].mean()))
print("Average Ratio of Potassium in the soil : {0:.2f}".format(data['K'].mean()))
print("Average Temperature in Celsius : {0:.2f}".format(data['temperature'].mean()))
print("Average Relative humidity in % : {0:.2f}".format(data['humidity'].mean()))
print("Average PH Value of the soil : {0:.2f}".format(data['ph'].mean()))
print("Average Rainfall in mm : {0:.2f}".format(data['rainfall'].mean()))


# In[ ]:





# In[ ]:




