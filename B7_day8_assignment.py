#!/usr/bin/env python
# coding: utf-8

# # Question 1

# In[5]:


def getinput(arg_func):
    def wrap_function():
        x=int(input("enter:"))
        arg_func(x)
    return wrap_function


# In[ ]:


@getinput
def fibo(n):
    if n<=1:
        return n
    else:
        return(fibo(n-1)+fibo(n-2))
nterms=int(input())
if(nterms<=0):
    print("invalid")
else:
    for i in range (nterms):
        print(fibo(i))
fibo()
        


# ##Question 2 

# In[ ]:


get_ipython().run_cell_magic('writefile', 'test.txt', 'Hi....This is Muthupriya')


# In[ ]:


try:
    file=open("test.txt","r")
    file.write("i am kaviya")
    print("it is in read mode")
except Exception as e:
    print("Error")
    print("Error message is:",e)


# In[ ]:




