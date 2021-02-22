#!/usr/bin/env python
# coding: utf-8

# In[1]:


def make_incrementor(n):
    return lambda x: x + n


# In[2]:


f = make_incrementor(42)


# In[3]:


f(0)


# In[4]:


f(1)


# In[5]:


pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]


# In[6]:


pairs.sort(key=lambda pair: pair[1])


# In[7]:


pairs


# In[ ]:




