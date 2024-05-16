#!/usr/bin/env python
# coding: utf-8

# In[1]:


import  numpy as np
a=[1,2,3,44]
b=np.array(a)
b


# 
# 
# for i in range(0,5):
#     ele=int(input("enter"))
#     a.append(ele)
#     print(a)
# b=np.array(a)    
# 

# import numpy as np
# a=[]
# for i in range(0,5):
#     ele=int(input("enter"))
#     a.append(ele) 
#     print(a) 
# b=np.array(a)

# In[4]:


#shape =n(rows),n(columns)


a=[[1,2,3,4],[5,6,7,8],[9,7,6,4]]
b=np.array(a)
b


# In[6]:


print("total shape",b.shape)
print("total size" ,b.size)


# In[11]:


b=np.zeros((4,3))
b


# In[12]:


b=np.ones((2,3))
b


# In[14]:


a=np.eye(3,3)
a


# # 

# In[4]:


#random number

import numpy as np
a=np.random.rand(5)
print(a)
b=np.random.randint(1,10,5)
print(b)
c=np.random.randn(5)
print(c)


# In[9]:


#reshapping data

b=np.random.randint(1,10,12)
print(b)

b.shape

b=b.reshape(2,6)
print("shape :2,6",b)


b=b.reshape(3,4)
print("shape :3,4",b)

b=b.reshape(6,2)
print("shape :6,2",b)



# In[17]:


rangen=np.random.randint(1,100,64)
print(rangen)

rangen=rangen.reshape(8,8)

print(rangen)



# In[18]:


# principle of -1!
rangen=rangen.reshape(-1,4)
a



# In[25]:


import numpy as np 
np.random.seed(5)
a=np.random.randint(1,100,10)
a


# In[32]:


#copy

a=np.array([10,20,30,40,50,60])
b=a[3:6]
b[:]=0
a


# In[33]:


a=np.array([10,20,30,40,50,60])
b=a[3:6].copy()
b[:]=0
a


# In[35]:


# conditional selection


import numpy as np
a=np.arange(1,16)
a


# In[37]:


a<10


# In[38]:


b=a>10
a[b]


# In[42]:


a[a % 10==2]


# In[43]:


import numpy as np
a=np.arange(1,5)
a


# In[44]:


a**2


# In[45]:


a+2


# In[46]:


import numpy as np

a=np.array([10,20,30,40,50])
np.min(a)


# In[47]:


np.max(a)


# In[ ]:


np.argmax(a)  #it will return undexing of max value


# In[ ]:


np.argmin(a)  #it will return undexing of min value


# In[48]:


#linspace()
import numpy as np

a=np.linspace(1,2,5)

a



# In[49]:


a=np.array([10,20,30,40,50,60])
np.unique(a,return_index=True ,return_counts=True)


# In[ ]:



    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




