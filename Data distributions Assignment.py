#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
from numpy.random import MT19937
from numpy.random import RandomState


# In[6]:


sdgamma=np.random.standard_gamma(2,100000)


# In[7]:


sdgamma.sort()


# In[8]:


dfgamma=pd.DataFrame({"rand":sdgamma})


# In[10]:


dfgamma.hist()
plt.show()


# In[12]:


mean_sdgamma=sum(sdgamma)/len(sdgamma)
print(mean_sdgamma)


# In[13]:


std_sdgamma=sdgamma.std()
print(std_sdgamma)


# In[14]:


mean_sdgamma=sdgamma.mean()
print(mean_sdgamma)


# In[22]:


plt.hist(dfgamma, color='c')
plt.axvline(sdgamma.mean(), color='b', linestyle='solid', linewidth=2)
plt.axvline(sdgamma.mean()+sdgamma.std(),color='b', linestyle='dashed', linewidth=2 )
plt.axvline(sdgamma.mean()-sdgamma.std(),color='b', linestyle='dashed', linewidth=2 )
plt.show


# In[23]:


rand1=np.random.normal(5,0.5,100)
rand2=np.random.normal(10,1,100)
rand3=rand1+rand2


# In[24]:


print(rand3)


# In[31]:


rand3_df=pd.DataFrame({'rand':rand3})
print(rand3_df)


# In[33]:


rand3_df.hist()
plt.show()


# In[34]:


rand3_df.mean()
print(rand3_df.mean())


# In[35]:


rand3_df.std()
print(rand3_df.std())


# In[ ]:




