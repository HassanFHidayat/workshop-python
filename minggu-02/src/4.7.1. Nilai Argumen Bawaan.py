#!/usr/bin/env python
# coding: utf-8

# In[1]:


def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)


# In[2]:


i = 5


# In[3]:


def f(arg=i):
    print(arg)


# In[4]:


i = 6


# In[5]:


f()


# In[6]:


def f(a, L=[]):
    L.append(a)
    return L


# In[7]:


print(f(1))


# In[8]:


print(f(2))


# In[9]:


print(f(3))


# In[10]:


def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L


# In[11]:


print(f(1))


# In[12]:


print(f(2))


# In[13]:


print(f(3))


# In[ ]:




