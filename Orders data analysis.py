#!/usr/bin/env python
# coding: utf-8

# In[5]:


#!pip install kaggle
import kaggle


# In[6]:


get_ipython().system('kaggle datasets download ankitbansal06/retail-orders -f orders.csv')


# In[7]:


import zipfile
zip_ref = zipfile.ZipFile('orders.csv.zip')
zip_ref.extractall()
zip_ref.close()


# In[2]:


import pandas as pd


# In[3]:


df = pd.read_csv('orders.csv',na_values =['Not Available', 'unknown'])
df.head(20)
df['Ship Mode'].unique()


# In[4]:


df.rename(columns={'Order Id':'order_id' ,'City':'city', 'Ship Mode':'ship_mode'})


# In[5]:


df.columns=df.columns.str.lower()


# In[6]:


df.columns=df.columns.str.replace(' ','_')


# In[7]:


df.head(5)


# In[8]:


#derive new columns , disscount , sale_price and profit
df['disscount']=df['list_price']*df['discount_percent']*.01


# In[10]:


df['sale_price']=df['list_price']-df['disscount']


# In[12]:


df['profit']=df['sale_price']-df['cost_price']


# In[16]:


df.dtypes


# In[15]:


df['order_date']=pd.to_datetime(df['order_date'],format="%Y-%m-%d")


# In[18]:


df.drop(columns=['list_price','cost_price','discount_percent'],inplace=True)


# In[20]:


import sqlalchemy as sal
engine = sal.create_engine('mssql://Amit\SQLEXPRESS01/master?driver=ODBC+DRIVER+17+FOR+SQL+SERVER')
conn=engine.connect()


# In[22]:


df.to_sql('df_orders',con=conn, index=False , if_exists = 'append')


# In[ ]:




