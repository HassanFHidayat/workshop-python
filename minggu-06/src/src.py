#!/usr/bin/env python
# coding: utf-8

# In[1]:


while True print('Hello world')


# In[2]:


10 * (1/0)


# In[3]:


4 + spam*3


# In[4]:


'2' + 2


# In[6]:


while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")


# In[7]:


class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")


# In[8]:


import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise


# In[9]:


for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()


# In[10]:


try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print(type(inst))    # the exception instance
    print(inst.args)     # arguments stored in .args
    print(inst)          # __str__ allows args to be printed directly,
                         # but may be overridden in exception subclasses
    x, y = inst.args     # unpack args
    print('x =', x)
    print('y =', y)


# In[11]:


def this_fails():
    x = 1/0


# In[12]:


try:
    this_fails()
except ZeroDivisionError as err:
    print('Handling run-time error:', err)


# In[13]:


raise NameError('HiThere')


# In[14]:


raise ValueError  # shorthand for 'raise ValueError()'


# In[15]:


try:
    raise NameError('HiThere')
except NameError:
    print('An exception flew by!')
    raise


# In[16]:


class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class InputError(Error):
    """Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

class TransitionError(Error):
    """Raised when an operation attempts a state transition that's not
    allowed.

    Attributes:
        previous -- state at beginning of transition
        next -- attempted new state
        message -- explanation of why the specific transition is not allowed
    """

    def __init__(self, previous, next, message):
        self.previous = previous
        self.next = next
        self.message = message


# In[17]:


try:
    raise KeyboardInterrupt
finally:
    print('Goodbye, world!')


# In[18]:


def bool_return():
    try:
        return True
    finally:
        return False


# In[19]:


bool_return()


# In[20]:


def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")


# In[21]:


divide(2, 1)


# In[22]:


divide(2, 0)


# In[23]:


divide("2", "1")


# In[ ]:




