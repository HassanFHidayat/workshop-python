#!/usr/bin/env python
# coding: utf-8

# In[1]:


def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")


# In[2]:


parrot(1000)                                          # 1 positional argument


# In[3]:


parrot(voltage=1000)                                  # 1 keyword argument


# In[4]:


parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments


# In[5]:


parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments


# In[6]:


parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments


# In[7]:


parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword


# In[8]:


def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])


# In[9]:


cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")


# In[ ]:




