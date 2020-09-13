#!/usr/bin/env python
# coding: utf-8

# # question 1

# In[29]:


def matchlist(list=[]):
    sublist=[1,1,5]
    for i in range(len(list)):
        if list[i]==sublist[0]:
            for j in range(i+1,len(list)):
                if list[j]==sublist[1]:
                    for k in range(j+1,len(list)):
                        if list[k]==sublist[2]:
                            return "it's a Match"
    else:
        return "it's Gone"
    


# In[32]:


matchlist([1,5,3,1])


# In[33]:


matchlist([1,2,1,7,5,9])


# # Question 2

# In[50]:


def prime_num(n):
    if n>1:
        for i in range (2,n):
            if n%i==0:
                return False
        return True
lst_prime=list(filter(prime_num,range(1,2500)))
print(len(lst_prime))


# # Question 3 

# In[54]:


list1=[input()]
list1_args=map(lambda x:x.title(),list1)
print(list(list1_args))

