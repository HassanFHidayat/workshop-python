#!/usr/bin/env python
# coding: utf-8

# In[1]:


year = 2016


# In[2]:


event = 'Referendum'


# In[3]:


f'Results of the {year} {event}'


# In[4]:


yes_votes = 42_572_654


# In[5]:


no_votes = 43_132_495


# In[6]:


percentage = yes_votes / (yes_votes + no_votes)


# In[7]:


'{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage)


# In[8]:


s = 'Hello, world.'


# In[9]:


str(s)


# In[10]:


repr(s)import math


# In[11]:


str(1/7)


# In[12]:


x = 10 * 3.25


# In[13]:


y = 200 * 200


# In[14]:


s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'


# In[15]:


print(s)


# In[16]:


# The repr() of a string adds string quotes and backslashes:
hello = 'hello, world\n'


# In[17]:


hellos = repr(hello)


# In[18]:


print(hellos)


# In[19]:


# The argument to repr() may be any Python object:
repr((x, y, ('spam', 'eggs')))


# In[20]:


import math


# In[21]:


print(f'The value of pi is approximately {math.pi:.3f}.')


# In[22]:


table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}


# In[23]:


for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')


# In[24]:


animals = 'eels'


# In[25]:


print(f'My hovercraft is full of {animals}.')


# In[26]:


print(f'My hovercraft is full of {animals!r}.')


# In[27]:


print('We are the {} who say "{}!"'.format('knights', 'Ni'))


# In[28]:


print('{0} and {1}'.format('spam', 'eggs'))


# In[29]:


print('{1} and {0}'.format('spam', 'eggs'))


# In[30]:


print('This {food} is {adjective}.'.format(
      food='spam', adjective='absolutely horrible'))


# In[31]:


print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred', other='Georg'))


# In[32]:


table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}


# In[33]:


print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
      'Dcab: {0[Dcab]:d}'.format(table))


# In[34]:


table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}


# In[35]:


print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))


# In[36]:


for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))


# In[37]:


for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    # Note use of 'end' on previous line
    print(repr(x*x*x).rjust(4))


# In[38]:


'12'.zfill(5)


# In[39]:


'-3.14'.zfill(7)


# In[40]:


'3.14159265359'.zfill(5)


# In[41]:


import math


# In[42]:


print('The value of pi is approximately %5.3f.' % math.pi)


# In[43]:


f = open('workfile', 'w')


# In[44]:


with open('workfile') as f:
    read_data = f.read()


# In[45]:


# We can check that the file has been automatically closed.


# In[46]:


f.closed


# In[47]:


f.read()


# In[48]:


import json


# In[49]:


json.dumps([1, 'simple', 'list'])


# In[ ]:




