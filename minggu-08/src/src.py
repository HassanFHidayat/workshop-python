#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os


# In[2]:


os.getcwd()      # Return the current working directory


# In[3]:


os.chdir('/server/accesslogs')   # Change current working directory


# In[4]:


dir(os)


# In[5]:


help(os)


# In[6]:


import shutil


# In[7]:


shutil.copyfile('data.db', 'archive.db')


# In[8]:


shutil.move('/build/executables', 'installdir')


# In[9]:


import glob


# In[10]:


glob.glob('*.py')


# In[11]:


import sys


# In[12]:


print(sys.argv)


# In[13]:


sys.stderr.write('Warning, log file not found starting a new one\n')


# In[14]:


import argparse

parser = argparse.ArgumentParser(prog = 'top',
    description = 'Show top lines from each file')
parser.add_argument('filenames', nargs='+')
parser.add_argument('-l', '--lines', type=int, default=10)
args = parser.parse_args()
print(args)


# In[15]:


import re


# In[16]:


re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')


# In[17]:


re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')


# In[18]:


'tea for too'.replace('too', 'two')


# In[19]:


import math


# In[20]:


math.cos(math.pi / 4)


# In[21]:


math.log(1024, 2)


# In[22]:


import random


# In[23]:


random.choice(['apple', 'pear', 'banana'])


# In[24]:


random.sample(range(100), 10)   # sampling without replacement


# In[25]:


random.random()    # random float


# In[26]:


random.randrange(6)    # random integer chosen from range(6)


# In[27]:


import statistics


# In[28]:


data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]


# In[29]:


statistics.mean(data)


# In[30]:


statistics.median(data)


# In[31]:


statistics.variance(data)


# In[32]:


# dates are easily constructed and formatted


# In[33]:


from datetime import date


# In[34]:


now = date.today()


# In[35]:


now


# In[36]:


now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")


# In[37]:


# dates support calendar arithmetic


# In[38]:


birthday = date(1964, 7, 31)


# In[39]:


age = now - birthday


# In[40]:


age.days


# In[41]:


import zlib


# In[42]:


s = b'witch which has which witches wrist watch'


# In[43]:


len(s)


# In[44]:


t = zlib.compress(s)


# In[45]:


len(t)


# In[46]:


zlib.decompress(t)


# In[47]:


zlib.crc32(s)


# In[48]:


from timeit import Timer


# In[49]:


Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()


# In[50]:


Timer('a,b = b,a', 'a=1; b=2').timeit()


# In[51]:


import reprlib


# In[52]:


reprlib.repr(set('supercalifragilisticexpialidocious'))


# In[53]:


import pprint


# In[54]:


t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta', 'yellow'], 'blue']]]


# In[55]:


pprint.pprint(t, width=30)


# In[56]:


import textwrap


# In[57]:


doc = """The wrap() method is just like fill() except that it returns a list of strings instead of one big string with newlines to separate the wrapped lines."""


# In[58]:


print(textwrap.fill(doc, width=40))


# In[59]:


import locale


# In[60]:


locale.setlocale(locale.LC_ALL, 'English_United States.1252')


# In[61]:


conv = locale.localeconv()          # get a mapping of conventions


# In[62]:


x = 1234567.8


# In[63]:


locale.format("%d", x, grouping=True)


# In[64]:


locale.format_string("%s%.*f", (conv['currency_symbol'],
                     conv['frac_digits'], x), grouping=True)


# In[65]:


from string import Template


# In[66]:


t = Template('${village}folk send $$10 to $cause.')


# In[67]:


t.substitute(village='Nottingham', cause='the ditch fund')


# In[68]:


import logging


# In[69]:


logging.debug('Debugging information')


# In[70]:


logging.info('Informational message')


# In[72]:



logging.error('Error occurred')


# In[71]:


logging.warning('Warning:config file %s not found', 'server.conf')


# In[73]:


logging.critical('Critical error -- shutting down')


# In[74]:


import weakref, gc


# In[75]:


class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)


# In[76]:


a = A(10)                   # create a reference


# In[77]:


d = weakref.WeakValueDictionary()


# In[78]:


d['primary'] = a            # does not create a reference


# In[79]:


d['primary']                # fetch the object if it is still alive


# In[80]:


del a                       # remove the one reference


# In[81]:


gc.collect()                # run garbage collection right away


# In[82]:


d['primary']                # entry was automatically removed


# In[83]:


from array import array


# In[84]:


a = array('H', [4000, 10, 700, 22222])


# In[85]:


sum(a)


# In[86]:


a[1:3]


# In[87]:


from collections import deque


# In[88]:


d = deque(["task1", "task2", "task3"])


# In[89]:


d.append("task4")


# In[90]:


print("Handling", d.popleft())


# In[91]:


import bisect


# In[92]:


scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]


# In[93]:


bisect.insort(scores, (300, 'ruby'))


# In[94]:


scores


# In[95]:


from heapq import heapify, heappop, heappush


# In[96]:


data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]


# In[97]:


heapify(data)                      # rearrange the list into heap order


# In[98]:


heappush(data, -5)                 # add a new entry


# In[99]:


[heappop(data) for i in range(3)]  # fetch the three smallest entries


# In[100]:


from decimal import *


# In[101]:


round(Decimal('0.70') * Decimal('1.05'), 2)


# In[102]:


round(.70 * 1.05, 2)


# In[103]:


getcontext().prec = 36


# In[104]:


Decimal(1) / Decimal(7)


# In[ ]:




