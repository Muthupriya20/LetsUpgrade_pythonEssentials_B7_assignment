#!/usr/bin/env python
# coding: utf-8

# # Question1

# In[5]:


speed=int(input())
if(speed<=1000):
    print("Safe to Land")
elif(1000<speed<5000):
    print("Bring down to 1000")
else:
    print("Turn Around")


# # Question2

# In[10]:


for n in range(1,201):
    if(n>1):
        for i in range(2,n):
            if(n%i==0):
                break
        else:
            print(n)
    


# In[ ]:




