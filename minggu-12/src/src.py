#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


a = np.array([0, 1, 2, 3])


# In[3]:


a


# In[4]:


a.ndim


# In[5]:


a.shape


# In[6]:


len(a)


# In[7]:


b = np.array([[0, 1, 2], [3, 4, 5]])    # 2 x 3 array


# In[8]:


b


# In[9]:


b.ndim


# In[10]:


b.shape


# In[11]:


len(b)     # returns the size of the first dimension


# In[12]:


c = np.array([[[1], [2]], [[3], [4]]])


# In[13]:


c


# In[14]:


c.shape


# In[15]:


a = np.arange(10) # 0 .. n-1  (!)


# In[16]:


a


# In[17]:


b = np.arange(1, 9, 2) # start, end (exclusive), step


# In[18]:


b


# In[19]:


c = np.linspace(0, 1, 6)   # start, end, num-points


# In[20]:


c


# In[21]:


d = np.linspace(0, 1, 5, endpoint=False)


# In[22]:


d


# In[23]:


a = np.random.rand(4)       # uniform in [0, 1]


# In[24]:


a


# In[25]:


b = np.random.randn(4)      # Gaussian


# In[26]:


b


# In[27]:


np.random.seed(1234)        # Setting the random seed


# In[28]:


a = np.array([1, 2, 3])


# In[29]:


a.dtype


# In[30]:


b = np.array([1., 2., 3.])


# In[31]:


b.dtype


# In[32]:


c = np.array([1, 2, 3], dtype=float)


# In[33]:


c.dtype


# In[34]:


x = np.linspace(0, 3, 20)
y = np.linspace(0, 9, 20)
plt.plot(x, y)       # line plot    

plt.plot(x, y, 'o')  # dot plot


# In[35]:


image = np.random.rand(30, 30)
plt.imshow(image, cmap=plt.cm.hot)    

plt.colorbar()


# In[36]:


X = np.linspace(-np.pi, np.pi, 256)
C, S = np.cos(X), np.sin(X)

plt.plot(X, C)
plt.plot(X, S)

plt.show()


# In[37]:


# Create a figure of size 8x6 inches, 80 dots per inch
plt.figure(figsize=(8, 6), dpi=80)

# Create a new subplot from a grid of 1x1
plt.subplot(1, 1, 1)

X = np.linspace(-np.pi, np.pi, 256)
C, S = np.cos(X), np.sin(X)

# Plot cosine with a blue continuous line of width 1 (pixels)
plt.plot(X, C, color="blue", linewidth=1.0, linestyle="-")

# Plot sine with a green continuous line of width 1 (pixels)
plt.plot(X, S, color="green", linewidth=1.0, linestyle="-")

# Set x limits
plt.xlim(-4.0, 4.0)

# Set x ticks
plt.xticks(np.linspace(-4, 4, 9))

# Set y limits
plt.ylim(-1.0, 1.0)

# Set y ticks
plt.yticks(np.linspace(-1, 1, 5))

# Save figure using 72 dots per inch
# plt.savefig("exercise_2.png", dpi=72)

# Show result on screen
plt.show()


# In[38]:


#Set Limits
plt.figure(figsize=(10, 6), dpi=80)
plt.plot(X, C, color="blue", linewidth=2.5, linestyle="-")
plt.plot(X, S, color="red",  linewidth=2.5, linestyle="-")

# Set Ticks
plt.xlim(X.min() * 1.1, X.max() * 1.1)
plt.ylim(C.min() * 1.1, C.max() * 1.1)

# Set ticks labels
plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi])
plt.yticks([-1, 0, +1])
plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
          [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
plt.yticks([-1, 0, +1],
          [r'$-1$', r'$0$', r'$+1$'])

#moving spines
ax = plt.gca()  # gca stands for 'get current axis'
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))

#Add a Legend
plt.plot(X, C, color="blue", linewidth=2.5, linestyle="-", label="cosine")
plt.plot(X, S, color="red",  linewidth=2.5, linestyle="-", label="sine")
plt.legend(loc='upper left')

#Annotate some points
t = 2 * np.pi / 3
plt.plot([t, t], [0, np.cos(t)], color='blue', linewidth=2.5, linestyle="--")
plt.scatter([t, ], [np.cos(t), ], 50, color='blue')

plt.annotate(r'$cos(\frac{2\pi}{3})=-\frac{1}{2}$',
             xy=(t, np.cos(t)), xycoords='data',
             xytext=(-90, -50), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

plt.plot([t, t],[0, np.sin(t)], color='red', linewidth=2.5, linestyle="--")
plt.scatter([t, ],[np.sin(t), ], 50, color='red')

plt.annotate(r'$sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$',
             xy=(t, np.sin(t)), xycoords='data',
             xytext=(+10, +30), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(16)
    label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.65))


# Show result on screen
plt.show()


# In[ ]:




