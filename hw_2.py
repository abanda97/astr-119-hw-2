#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import matplotlib.pyplot as plt


# In[ ]:


x = np.linspace(0, 2*np.pi, 1000)


# In[ ]:


y = 5.5 * np.cos(2*x) + 5.5
z = 0.02 * np.exp(x)
w = 0.25 * x**2 + 0.1* np.sin(10*x)

fig = plt.figure(figsize=(6,6))

#The functions that each line on the graph represents
plt.plot(x, y, label=r'$y(x) = \5.5cos(2*x) + 5.5$')
plt.plot(x, z, label=r'$y(x) = \0.02 * exp(x)$')
plt.plot(x, w, label=r'$y(x) = \0.25 * x^2 + 0.1sin(10*x)$')


#X and Y axes labels
plt.xlabel('Time Spent in ASTR-119')
plt.ylabel('Measure of Pure Awesomeness')

#X and Y ranges
plt.xlim([0,2*np.pi])
plt.ylim([-1,10.])


# In[ ]:




