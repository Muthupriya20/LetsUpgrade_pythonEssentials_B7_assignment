#!/usr/bin/env python
# coding: utf-8

# # Armstrong Number

# In[7]:


for n in range(1042000,702648265):
    sum=0
    t=n
    while(t>0):
        num=t%10
        sum=sum+num**7
        t=t//10
    if(n==sum):
        print("The first armstrong number is",n)
        break


# In[ ]:




