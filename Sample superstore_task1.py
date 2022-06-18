#!/usr/bin/env python
# coding: utf-8

# # SAMPLE SUPERSTORE EXPLORATORY DATA ANALYSIS

# # MUNAVATH PRASHANTH

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt


# In[2]:


Superstore=pd.read_csv("C:/Users/munavathprashanth24/OneDrive/Documents/Superstore.csv")


# In[3]:


Superstore.head()


# In[4]:


Superstore.tail()


# In[5]:


Superstore.shape


# In[6]:


Superstore.describe()


# In[7]:


Superstore.info()


# In[8]:


Superstore.columns


# In[9]:


Superstore.isnull().sum()


# In[10]:


Superstore.nunique()


# # Correlation Matrix

# In[11]:


from matplotlib import style
style.use("dark_background")


# In[12]:


sns.heatmap(Superstore.corr(),annot=True)


# # Pair-plot

# In[13]:


sns.pairplot(Superstore,hue="Ship Mode")


# In[14]:


Superstore['Ship Mode'].value_counts()


# In[15]:


sns.countplot(x=Superstore['Ship Mode'])


# In[16]:


sns.pairplot(Superstore,hue="Segment")


# In[17]:


sns.countplot(x="Segment",data=Superstore)


# In[18]:


sns.pairplot(Superstore,hue="Category")


# In[19]:


Superstore["Category"].value_counts()


# In[20]:


sns.countplot(x="Category",data=Superstore)


# In[21]:


Superstore["Sub-Category"].value_counts()


# In[22]:


plt.figure(figsize=(12,10))
Superstore["Sub-Category"].value_counts().plot.pie()
plt.show()


# In[23]:


Superstore["State"].value_counts()


# In[24]:


plt.figure(figsize=(15,12))
sns.countplot(x="State",data=Superstore,palette="rocket",order=Superstore['State'].value_counts().index)
plt.xticks(rotation=90)
plt.show()


# In[25]:


Superstore.hist(figsize=(10,10),bins=40)
plt.show()


# In[26]:


plt.figure(figsize=(10,10))
Superstore['Region'].value_counts().plot.pie()
plt.show()


# In[27]:


plt.figure(figsize=(10,6))
plt.scatter(x='Sales',y='Profit',data=Superstore)
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.show()


# In[28]:


sns.lineplot(x='Discount',y='Profit',label='Profit',data=Superstore)
plt.legend()
plt.show()


# In[29]:


sns.lineplot(x='Quantity',y='Profit',label='Profit',data=Superstore)
plt.legend()
plt.show()


# # profit/loss and sales in segment

# In[30]:


Superstore.groupby("Segment")[['Profit','Sales']].sum().plot.bar(color=["red","blue"],figsize=(8,5),ylabel="profit/loss vs sales")


# # segment wise sales in each region

# In[31]:


plt.figure(figsize=(8,10))
plt.title("segment wise sales in each region")
sns.barplot(x="Region",y="Sales",hue="Segment",data=Superstore,order=Superstore['Region'].value_counts().index,palette='rocket')
plt.xlabel("Region",fontsize=10)
plt.show()


# # profit/loss and sales in region

# In[32]:


Superstore.groupby('Region')[["Profit","Sales"]].sum().plot.bar(color=["red","blue"],figsize=(8,5))
plt.ylabel("profit/loss and sales")
plt.show()


# # profit/loss and sales across states

# In[33]:


Superstore.groupby('State')[["Profit","Sales"]].sum().sort_values(by="Sales",ascending=False).plot.bar(color=["red","blue"],figsize=(8,5))
plt.ylabel("profit/loss and sales")
plt.xlabel("states")
plt.ylabel("profit/loss and sales")
plt.title
plt.show()


# # profit/loss and sales by category

# In[34]:


Superstore.groupby('Category')[["Profit","Sales"]].sum().plot.bar(color=["red","blue"],figsize=(8,5))
plt.ylabel("profit/loss and sales")
plt.show()


# In[35]:


Superstore.groupby('Sub-Category')[["Profit","Sales"]].sum().sort_values(by="Sales",ascending=False).plot.bar(color=["red","blue"],figsize=(8,5))
plt.ylabel("profit/loss and sales")
plt.show()


# In[41]:


from matplotlib import style
style.use("dark_background")
Superstore.boxplot()


# In[ ]:




