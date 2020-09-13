#!/usr/bin/env python
# coding: utf-8

# # Question1

# In[4]:


get_ipython().system(' pip install unittest2')


# In[49]:


def prime(n):
        if(n>1):
            for i in range(2,n+1):
                if(n%i==0):
                    return n
                else:
                    return "not"
print(prime(2))


# In[50]:


get_ipython().run_cell_magic('writefile', 'prime_check.py', 'import unittest\nclass prime_num(unittest.TestCase):\n    def test(self):\n        result=(prime(2))\n        self.assertEquals(result,2)\n\n        ')


# In[51]:


get_ipython().system(' python prime_check.py')


# ## Question2

# In[60]:


lst=list(range(1,1000))


# In[61]:


def armstrongGen(lst):
    for i in lst:
        sum=0
        t=i
        while(t>0):
            num=t%10
            sum=sum+num**3
            t=t//10
        if(i==sum):
            yield i


# In[62]:


print(list(armstrongGen(lst)))

