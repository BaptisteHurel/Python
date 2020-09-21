#!/usr/bin/env python
# coding: utf-8

# ## 1) NumPy

# In[5]:


pip install numpy


# In[6]:


get_ipython().system('which python3')


# In[7]:


import numpy as np


# In[3]:


l = [i for i in range{}]


# In[9]:


ar = np.array{l}


# In[ ]:


ar


# In[ ]:


ar.min()


# In[ ]:


ar.max()


# In[ ]:


ar.mean() #moyenne


# In[ ]:


ar.std() #ecart type


# In[10]:


ar.dtype() #datatype


# In[11]:


ex = list{[1,2,3,'s']}


# In[12]:


np.array(ex)


# In[1]:


m = np.array([[1,2],[3,4]])


# In[14]:


m[0][1] = 9


# In[15]:


m.shape 


# In[22]:


m2 = np.array([1,2,3,4,5], ndmin=2); m2


# In[23]:


m2.shape


# In[25]:


m2.shape(5,1)


# In[28]:


m2.reshape(1,5)


# In[33]:


b = np.linspace(0, 2, 4) # 0--> nb depart , 2 --> nb arrivée , 4--> nb de valeurs


# In[34]:


b**2 # chaque element est mis au carré / 0 et 2


# In[35]:


np.arrange(24)


# In[36]:


c = np.arrange(24).reshape(2,3,4); c


# In[37]:


c.shape


# In[38]:


c.ndim


# In[41]:


ar = np.array([[1,2,3],[4,5,6],[7,8,9]])


# ### Exercices  /Cours

# In[42]:


#lignes 2 et 3 et colonnes 1 et 2
ar[1:2,0:2]


# In[43]:


#juste la 2eme ligne et un tableau à 1 dimension
ar[1,:]


# In[44]:


#la derniere colonne
ar[:,-1]


# In[45]:


s = "personne ecoute ce que je raconte"


# In[46]:


s[0:9]


# In[48]:


ar==2


# In[49]:


A = np.array([[1,1],[0,1]])
B = np.array([[2,0],[3,4]])
1,B


# In[51]:


A+B #surcharge d'opérateur


# In[ ]:


a = np.array([[1,2],[3,4]])


# In[ ]:


a.argmax() #position avec l'argument maximum


# In[52]:


b = np.array([1,7,2,8,3]


# In[53]:


sum(b) #fonction python


# In[54]:


b.sum(axis=0) #colonne


# In[55]:


b.sum(axis=1) #ligne


# In[ ]:


np.array([1,2,3,4]).cumsum()


# In[56]:


np.arrange(10) #numpy array


# In[57]:


np.title(3,8);


# In[ ]:


z = npzeros((2,4)); z


# In[4]:


z.dtype


# In[63]:


6*z


# In[62]:


np.ones((2,4), dtype='int8')


# In[61]:


np.diag(np.array([1,4]))


# In[ ]:




