#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


data=pd.read_csv("/GlobalLandTemperaturesByMajorCity.csv")


# In[3]:


data.head()


# In[4]:


data.dtypes


# In[5]:


data.shape


# In[6]:


data.isna().sum()


# In[7]:


data.isna().sum() / data.shape[0] * 100


# In[8]:


data_prepared = data.dropna(axis=0, how="any")


# In[9]:


data_prepared.shape


# In[10]:


data_prepared["City"].value_counts()


# In[11]:


data_prepared[data_prepared["Country"] == "Turkey"]


# In[12]:


data_selected=data_prepared[data_prepared["Country"].isin(["Turkey","Brazil","United States"])]


# In[13]:


data_selected["Country"].value_counts()


# In[14]:


data_selected.groupby(by="Country").mean()


# In[15]:


data_selected.groupby(by="Country").agg(["min","mean","max"])


# In[16]:


tr_avg_temps=data_selected[data_selected["Country"]=="Turkey"]["AverageTemperature"]
br_avg_temps=data_selected[data_selected["Country"]=="Brazil"]["AverageTemperature"]
usa_avg_temps=data_selected[data_selected["Country"]=="United States"]["AverageTemperature"]


# In[ ]:





# In[ ]:





# In[17]:


sns.distplot(tr_avg_temps)
sns.distplot(br_avg_temps)
sns.distplot(usa_avg_temps)


# In[22]:


ulkeler=data_selected["Country"].unique()
for ulke in ulkeler:
    sns.distplot(data_selected[data_selected["Country"]==ulke]["AverageTemperature"])
    plt.legend(ulkeler)
    


# In[ ]:





# In[ ]:





# In[ ]:




