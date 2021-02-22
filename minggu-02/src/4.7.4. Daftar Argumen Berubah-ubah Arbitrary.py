#!/usr/bin/env python
# coding: utf-8

# In[1]:


def concat(*args, sep="/"):
    return sep.join(args)


# In[2]:


concat("earth", "mars", "venus")


# In[3]:


concat("earth", "mars", "venus", sep=".")


# In[ ]:




