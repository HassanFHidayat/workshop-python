#!/usr/bin/env python
# coding: utf-8

# In[1]:


def standard_arg(arg):
    print(arg)


# In[2]:


def pos_only_arg(arg, /):
    print(arg)


# In[3]:


def kwd_only_arg(*, arg):
    print(arg)


# In[4]:


def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)


# In[5]:


standard_arg(2)


# In[6]:


standard_arg(arg=2)


# In[7]:


pos_only_arg(1)


# In[8]:


pos_only_arg(arg=1)


# In[9]:


kwd_only_arg(3)


# In[10]:


kwd_only_arg(arg=3)


# In[11]:


combined_example(1, 2, 3)


# In[12]:


combined_example(1, 2, kwd_only=3)


# In[13]:


combined_example(1, standard=2, kwd_only=3)


# In[14]:


combined_example(pos_only=1, standard=2, kwd_only=3)


# In[15]:


def foo(name, **kwds):
    return 'name' in kwds


# In[ ]:




