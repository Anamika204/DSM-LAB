#!/usr/bin/env python
# coding: utf-8

# In[1]:


a = int(input["enter a number"])
b = int(input["enter a number"])
ch = int(input["enter your choice 
               1.addition\n,2.substraction\n,3.multiplication\n,4.division"])
               if choice = 1
               sum = a+b
               print(sum)
               elif
               choice = 2
               sub = a-b
               print(sub)
               elif
               choice = 3
               mul = a*b
               print(mul)
               else
               choice = 4
               div = a%b
               print(div)


# In[2]:


a = int(input("enter a number"))
b = int(input("enter a number"))
ch = int(input("enter your choice 
               1.addition\n,2.substraction\n,3.multiplication\n,4.division"))
               if choice = 1:
               sum = a+b
               print(sum)
               elif
               choice = 2:
               sub = a-b
               print(sub)
               elif
               choice = 3:
               mul = a*b
               print(mul)
               else
               choice = 4:
               div = a%b
               print(div)


# In[4]:


a = int(input("enter a number"))
b = int(input("enter a number"))
ch = int(input("enter your choice"))
               if 
               choice = 1
               sum = a+b
               print(sum):
               elif
               choice = 2:
               sub = a-b
               print(sub)
               elif
               choice = 3:
               mul = a*b
               print(mul)
               else
               choice = 4:
               div = a%b
               print(div)


# In[5]:


a = int(input("enter a number"))
b = int(input("enter a number"))
ch = int(input("enter your choice 1.addition/n,2.substraction/n,3.multiplication/n,4.division/n,5.invalid/n"))
if ch == 1:
    print("sum=",a+b)
elif ch == 2:
    print("sub=",a-b)
elif ch == 3:
    print("mul=",a*b)
elif ch == 4:
    print("div=",a%b)
else ch == 5:
    print("invalid")


# In[6]:


a = int(input("enter a number"))
b = int(input("enter a number"))
ch = int(input("enter your choice 1.addition/n,2.substraction/n,3.multiplication/n,4.division/n"))
if ch == 1:
    print("sum=",a+b)
elif ch == 2:
    print("sub=",a-b)
elif ch == 3:
    print("mul=",a*b)
elif ch == 4:
    print("div=",a%b)
else:
    print("invalid")


# In[7]:


a = int(input("enter a number"))
b = int(input("enter a number"))
ch = int(input("enter your choice 1.addition/n,2.substraction/n,3.multiplication/n,4.division/n"))
if ch == 1:
    print("sum=",a+b)
elif ch == 2:
    print("sub=",a-b)
elif ch == 3:
    print("mul=",a*b)
elif ch == 4:
    print("div=",a%b)
else:
    print("invalid")


# In[1]:


a = int(input("Enter a number"))
b = int(input("enter a number"))
print("and=",a and b)
print("or=",a or b)
print("not=",a not b)


# In[1]:


a = int(input("Enter a number"))
b = int(input("enter a number"))
print("and=",a and b)
print("or=",a or b)
print(a>=b)
print(a<=b)
print(a==b)
print(a!=b)


# In[4]:


a = int(input("Enter a number"))
b = int(input("enter a number"))
print(a and b == 10)
print(a == 10 or b == 10 )
print(not b)
print(a>=b)
print(a<=b)
print(a==b)
print(a!=b)


# In[7]:


dict1 = {"roll":1,"name" : "anamika","age" : 21}
dict2 = {"phno": 97654321, "place" : "calicut"} 
print(dict1 | dict2)


# In[8]:


dict1 = {6,"anamika",21}
dict2 = {864356788,"calicut"}
dict1. update dict2


# In[9]:


dict1 = {"roll":1,"name" : "anamika","age" : 21}
dict2 = {"phno": 97654321, "place" : "calicut"} 
dict1.update(dict2)


# In[12]:


dict1 = {"roll":1,"name" : "anamika","age" : 21}
dict2 = {"phno": 97654321, "place" : "calicut","name":"devu"} 
dict1.update(dict2)


# In[13]:


print(dict1)


# In[4]:



import numpy as np

X=np.array([[1,2,3],[4,5,6],[7,8,9]])


U,S,VT=np.linalg.svd(X)


n_components=2


X_reconstructed=np.dot(U[:,:n_components],np.dot(np.diag(S[:n_components]),VT[:n_components,:]))
print("Original matrix:")
print(X)
print("\nReconsructed Matrix(with reduced dimensions):")
print(X_reconstructed)


# In[11]:


import matplotlib.pyplot as plt
x = [3,7,6,8,9]
y = [3,4,5,6,9]
plt.plot(x,y)
plt.title("graph")
plt.ylabel("length")
plt.xlabel("width")


# In[15]:


import matplotlib.pyplot as plt
subject = ["ads","ase","dbms","ai"]
mark = [32,32,38,36]
plt.bar(subject,mark)
plt.xlabel("mark")
plt.ylabel("subject")
plt.title("semester1")


# In[18]:


import matplotlib.pyplot as plt
subject = ["ads","ase","dbms","ai"]
mark = [32,32,38,36]
plt.scatter(subject,mark)
plt.xlabel("mark")
plt.ylabel("subject")
plt.title("semester1")


# In[20]:


import matplotlib.pyplot as plt
subject = ["ads","ase","dbms","ai"]
mark = [32,32,38,36]
plt.hist(subject)
plt.xlabel("mark")
plt.ylabel("subject")
plt.title("semester1")


# In[23]:





# In[27]:


import matplotlib.pyplot as plt
subject = ["ads","ase","dbms","ai"]
mark = [35,32,38,36]
plt.plot(mark)
plt.legend(mark)
plt.xlabel("mark")
plt.ylabel("subject")
plt.title("semester1")


# In[28]:


import matplotlib.pyplot as plt
x = [1,2,6,18]
y = [3,10,12,20]
plt.title("line diagram")
plt.xlabel("x axis")
plt.ylabel("y axis)
           


# In[ ]:




