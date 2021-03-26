#!/usr/bin/env python
# coding: utf-8

# In[1]:


def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)


# In[2]:


class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart


# In[45]:


x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)
del x.counter


# In[3]:


x = Complex(3.0, -4.5)


# In[4]:


x.r, x.i


# In[5]:


class Dog:

    kind = 'canine'         # class variable shared by all instances

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance


# In[6]:


d = Dog('Fido')


# In[7]:


e = Dog('Buddy')


# In[8]:


d.kind


# In[9]:


e.kind


# In[10]:


d.name


# In[11]:


e.name


# In[12]:


class Dog:

    tricks = []             # mistaken use of a class variable

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)


# In[13]:


d = Dog('Fido')


# In[14]:


e = Dog('Buddy')


# In[15]:


d.add_trick('roll over')


# In[16]:


e.add_trick('play dead')


# In[17]:


d.tricks                # unexpectedly shared by all dogs


# In[18]:


class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []    # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)


# In[19]:


d = Dog('Fido')


# In[20]:


e = Dog('Buddy')


# In[21]:


d.add_trick('roll over')


# In[22]:


e.add_trick('play dead')


# In[23]:


d.tricks


# In[24]:


e.tricks


# In[25]:


class Warehouse:
    purpose = 'storage'
    region = 'west'


# In[26]:


w1 = Warehouse()


# In[27]:


print(w1.purpose, w1.region)


# In[28]:


w2 = Warehouse()


# In[29]:


w2.region = 'east'


# In[30]:


print(w2.purpose, w2.region)


# In[31]:


class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]


# In[32]:


rev = Reverse('spam')


# In[33]:


iter(rev)


# In[34]:


for char in rev:
    print(char)


# In[35]:


def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]


# In[36]:


for char in reverse('golf'):
    print(char)


# In[37]:


sum(i*i for i in range(10))                 # sum of squares


# In[38]:


xvec = [10, 20, 30]


# In[39]:


yvec = [7, 5, 3]


# In[40]:


sum(x*y for x,y in zip(xvec, yvec))         # dot product


# In[41]:


unique_words = set(word for line in page  for word in line.split())


# In[42]:


valedictorian = max((student.gpa, student.name) for student in graduates)


# In[43]:


data = 'golf'


# In[44]:


list(data[i] for i in range(len(data)-1, -1, -1))


# In[ ]:




