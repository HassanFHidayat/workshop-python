#!/usr/bin/env python
# coding: utf-8

# In[1]:


def fib(n):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()


# In[2]:


# Now call the function we just defined:
fib(2000)


# In[3]:


fib


# In[4]:


f = fib


# In[5]:


f(100)


# In[6]:


def fib2(n):  # return Fibonacci series up to n
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)    # see below
        a, b = b, a+b
    return result


# In[7]:


f100 = fib2(100)    # call it


# In[8]:


f100                # write the result


# In[ ]:




