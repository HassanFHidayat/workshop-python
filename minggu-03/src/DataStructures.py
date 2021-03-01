#!/usr/bin/env python
# coding: utf-8

# In[1]:


fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']


# In[2]:


fruits.count('apple')


# In[3]:


fruits.count('tangerine')


# In[4]:


fruits.index('banana')


# In[5]:


fruits.index('banana', 4)  # Find next banana starting a position 4


# In[6]:


fruits.reverse()


# In[7]:


fruits


# In[8]:


fruits.append('grape')


# In[9]:


fruits


# In[10]:


fruits.sort()


# In[11]:


fruits


# In[12]:


fruits.pop()


# In[13]:


stack = [3, 4, 5]


# In[14]:


stack.append(6)


# In[15]:


stack.append(7)


# In[16]:


stack


# In[17]:


stack.pop()


# In[18]:


stack


# In[19]:


stack.pop()


# In[20]:


stack.pop()


# In[21]:


stack


# In[22]:


from collections import deque


# In[23]:


queue = deque(["Eric", "John", "Michael"])


# In[24]:


queue.append("Terry")           # Terry arrives


# In[25]:


queue.append("Graham")          # Graham arrives


# In[26]:


queue.popleft()                 # The first to arrive now leaves


# In[27]:


queue.popleft()                 # The second to arrive now leaves


# In[28]:


queue                           # Remaining queue in order of arrival


# In[29]:


squares = []


# In[30]:


for x in range(10):
    squares.append(x**2)


# In[31]:


squares


# In[32]:


squares = list(map(lambda x: x**2, range(10)))


# In[33]:


squares = [x**2 for x in range(10)]


# In[34]:


[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]


# In[35]:


combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x, y))


# In[36]:


combs


# In[37]:


vec = [-4, -2, 0, 2, 4]


# In[38]:


# create a new list with the values doubled


# In[39]:


[x*2 for x in vec]


# In[40]:


# filter the list to exclude negative numbers


# In[41]:


[x for x in vec if x >= 0]


# In[42]:


# apply a function to all the elements


# In[43]:


[abs(x) for x in vec]


# In[44]:


# call a method on each element


# In[45]:


freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']


# In[46]:


[weapon.strip() for weapon in freshfruit]


# In[47]:


# create a list of 2-tuples like (number, square)


# In[48]:


[(x, x**2) for x in range(6)]


# In[49]:


# the tuple must be parenthesized, otherwise an error is raised


# In[50]:


[x, x**2 for x in range(6)]


# In[51]:


# flatten a list using a listcomp with two 'for'


# In[52]:


vec = [[1,2,3], [4,5,6], [7,8,9]]


# In[53]:


[num for elem in vec for num in elem]


# In[54]:


from math import pi


# In[55]:


[str(round(pi, i)) for i in range(1, 6)]


# In[56]:


matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]


# In[57]:


[[row[i] for row in matrix] for i in range(4)]


# In[58]:


transposed = []


# In[59]:


for i in range(4):
    transposed.append([row[i] for row in matrix])


# In[60]:


transposed


# In[61]:


transposed = []


# In[62]:


for i in range(4):
    # the following 3 lines implement the nested listcomp
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)


# In[63]:


transposed


# In[64]:


list(zip(*matrix))


# In[65]:


a = [-1, 1, 66.25, 333, 333, 1234.5]


# In[66]:


del a[0]


# In[67]:


a


# In[68]:


del a[2:4]


# In[69]:


a


# In[70]:


del a[:]


# In[71]:


a


# In[72]:


del a


# In[73]:


t = 12345, 54321, 'hello!'


# In[74]:


t[0]


# In[75]:


t


# In[76]:


# Tuples may be nested:
u = t, (1, 2, 3, 4, 5)


# In[77]:


u


# In[78]:


# Tuples are immutable:
t[0] = 88888


# In[79]:


# but they can contain mutable objects:
v = ([1, 2, 3], [3, 2, 1])


# In[80]:


v


# In[81]:


empty = ()


# In[82]:


singleton = 'hello',    # <-- note trailing comma


# In[83]:


len(empty)


# In[84]:


len(singleton)


# In[85]:


singleton


# In[86]:


x, y, z = t


# In[87]:


basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}


# In[88]:


print(basket)                      # show that duplicates have been removed


# In[89]:


'orange' in basket                 # fast membership testing


# In[90]:


'crabgrass' in basket


# In[91]:


# Demonstrate set operations on unique letters from two words


# In[92]:


a = set('abracadabra')


# In[93]:


b = set('alacazam')


# In[94]:


a                                  # unique letters in a


# In[95]:


a - b                              # letters in a but not in b


# In[96]:


a | b                              # letters in a or b or both


# In[97]:


a & b                              # letters in both a and b


# In[98]:


a ^ b                              # letters in a or b but not both


# In[99]:


a = {x for x in 'abracadabra' if x not in 'abc'}


# In[100]:


a


# In[101]:


tel = {'jack': 4098, 'sape': 4139}


# In[102]:


tel['guido'] = 4127


# In[103]:


tel


# In[104]:


tel['jack']


# In[105]:


del tel['sape']


# In[106]:


tel['irv'] = 4127


# In[107]:


tel


# In[108]:


list(tel)


# In[109]:


sorted(tel)


# In[110]:


'guido' in tel


# In[111]:


'jack' not in tel


# In[112]:


knights = {'gallahad': 'the pure', 'robin': 'the brave'}


# In[114]:


for k, v in knights.items():
    print(k, v)


# In[115]:


for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)


# In[116]:


questions = ['name', 'quest', 'favorite color']


# In[117]:


answers = ['lancelot', 'the holy grail', 'blue']


# In[118]:


for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))


# In[119]:


basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']


# In[120]:


for i in sorted(basket):
    print(i)


# In[121]:


import math


# In[122]:


raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]


# In[123]:


filtered_data = []


# In[124]:


for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)


# In[125]:


filtered_data


# In[126]:


string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'


# In[127]:


non_null = string1 or string2 or string3


# In[128]:


non_null


# In[ ]:




