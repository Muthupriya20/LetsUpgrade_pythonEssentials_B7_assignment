#!/usr/bin/env python
# coding: utf-8

# # List Functions 

# In[1]:


list1=[["a","b","c"],30,"apple",145.75]
print(list1)


# In[2]:


#length of a list
print(len(list1))


# In[4]:


#maximum and minimum in a list
list2=[10,30,65,23]
print(max(list2))
print(min(list2))


# In[5]:


#range
print(list(range(20)))
print(list(range(20,200,5)))


# # Dictionary Functions

# In[19]:


dict={'name':'jack', 'age':20, 'gender':'M', 'dept':'CSE', 'reg.no':1234 }
print(dict)


# In[20]:


print(dict['name'])


# In[21]:


#all-print true for non-zero entry
squares={0:0,1:1,3:9,2:4,5:25}
cubes={0:0,1:1,3:27,2:8,5:125,10:1000,7:123}
print(all(cubes))


# In[23]:


#any-print true if any one entry is true
print(any(squares))

#length of dictionary
print(len(cubes))

#produce printable string
print(str(dict))

#print type of variable
print(type(dict['age']))

#to sort
print(sorted(squares))
print(sorted(cubes))


# # Sets Functions

# In[24]:


set1={'apple','orange','banana'}
set2={0,1,2,3}
print(set1)
print(set2)


# In[25]:


#length of set
print(len(set1))
print(len(set2))

#maximum and minimum in a set
print(max(set1))
print(min(set2))


# In[26]:


#to sort
print(sorted(set1))
print(sorted(set2))

#print sum of all term in a set
print(sum(set2))

#all-true for non-zero entry
print(all(set1))
print(all(set2))


# In[31]:


#any-print true if any one entry is true
print(any(set2))

#returns enumerate object
e_set1=enumerate(set1,1)
print(type(set1))
print(type(e_set1))
print(list(e_set1))


# # Tuples Methods

# In[34]:


tup=(1,2,4,8,5,3,8)
print(tup)


# In[35]:


#count
print(tup.count(8))

#index
print(tup.index(5))


# # Functions

# In[36]:


#length of a tuple
print(len(tup))

#maximum and minimum in a tuple
print(max(tup))
print(min(tup))

#to sort
print(sorted(tup))


# # String Methods

# In[39]:


string="i loVe pYthon"
print(string)


# In[44]:


#to convert first letter into capital
print(string.capitalize())

#to convert string in lower case
print(string.casefold())

#count
print(string.count("o"))

#find
print(string.find("V"))

#replace
print(string.replace("loVe","Like"))


# In[ ]:




