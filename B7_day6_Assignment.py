#!/usr/bin/env python
# coding: utf-8

# # Question 1

# In[12]:


class bank_account():
   def __init__(self,ownerName,Balance):
       self.ownerName=ownerName
       self.Balance=Balance
   def deposit(self,a):
       return (self.Balance+a)
   def withdrawals(self,y):
       if(y<self.Balance):
           return(self.Balance-y)
       else:
           return "insufficient balance"
obj=bank_account("suresh",100000)
print(obj.deposit(5000))
print(obj.withdrawals(5000))


# # Question 2 

# In[16]:


class cone():
    def __init__(self,R,h):
        self.R=R
        self.h=h
    def Volume(self):
        return self.R**2*(self.h/3)*3.14
    def surface_area(self):
        return 3.14*self.R*(self.R+((self.h)**2+(self.R)**2)**0.5)
obj1=cone(2,3)
print(obj1.Volume())
print(obj1.surface_area())

