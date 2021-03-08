#!/usr/bin/env python
# coding: utf-8

# In[1]:


import fibo


# In[2]:


fibo.fib(1000)


# In[3]:


fibo.fib2(100)


# In[4]:


fibo.__name__


# In[5]:


fib = fibo.fib


# In[6]:


fib(500)


# In[7]:


from fibo import fib, fib2


# In[8]:


fib(500)


# In[9]:


from fibo import *


# In[10]:


fib(500)


# In[11]:


import sys


# In[12]:


sys.ps1


# In[13]:


sys.ps2


# In[14]:


sys.ps1 = 'C> '


# In[15]:


print('Yuck!')


# In[16]:


import fibo, sys


# In[17]:


dir(fibo)


# In[18]:


dir(sys)


# In[19]:


a = [1, 2, 3, 4, 5]


# In[20]:


import fibo


# In[21]:


fib = fibo.fib


# In[22]:


dir()


# In[23]:


import builtins


# In[24]:


dir(builtins)


# In[25]:


import sound.effects.echo


# In[ ]:




