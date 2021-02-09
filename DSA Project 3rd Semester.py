#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Resizeable Array Class Initialization
class ResizeableArray:
    def __init__(self):    #class constructor
        self.n = 0         #this variable represent the Size/number of elements stored in the Array
        self.capacity = 5  #it is the initialized storage capacity of the Array
        self.A = ["-" for i in range(self.capacity)]  #Creating Array of storage capacity self.capacity by appending "-" which shows that the space is empty
     
    #function to get Array's length or Size of the Array
    def len_array(self):
        return self.n       #returns the size/No. of elements stored in the array
    
    #funtion to print the Array
    def print_array(self):
        if self.n!=0:                           #checking that Array is not empty
            for i in range(self.n):             #iterate through the elements of Array
                if i != "-":                    #Checking whether Array is ended or not 
                    print(self.A[i],end=(" "))  #printing ith element from the Array
        else:
            return "Empty Array"                #prints when the Array is empty

    #function to get ith element from Array
    def getitem(self, i):                      #variable 'i' is the index of the required element
        if self.n==0:                          #checking that Array is empty or not
            raise Exception("Empty Array!")    #raise error when array is empty
        if 0 <= i < self.n:                    #checking that the given index is greater than/equal to 0 and less than size of Array
            return self.A[i]                   #returns the required ith element
        else:
            raise IndexError("Invalid index!") #raise error when the index is not valid

    #funtion to append element in the Array
    def append(self, e):                  #parameter 'e' is the element to append
        if self.n == self.capacity:       #checks that the Array is full by comparing Array's length to it's capacity
            self.resize(10+self.capacity) #if Array is full than calls resize funtion to increase the size by 10
        self.A[self.n] = e                #appending the element 'e'
        self.n += 1                       #increasing/updating the size of Array

    #funtion to increase the size of fully loaded Array
    def resize(self, c):             #taking input 'c', the capacity by increasing Array's capacity
        B = ["-" for i in range(c)]  #creating new Array of capacity 'c'
        for k in range(self.n):      #iterate through all the elements stored in the previous(fully loaded) Array 
            B[k] = self.A[k]         #inserting previous Array's elements in the new one
        self.A = B                   #replacing fully loaded Array by resized Array
        self.capacity = c            #updating capacity of the Array


# In[2]:


obj = ResizeableArray()


# In[3]:


obj.len_array()


# In[4]:


obj.print_array()


# In[10]:


obj.append(1)
obj.append(2)
obj.append(3)
obj.append(4)


# In[11]:


obj.len_array()


# In[13]:


obj.print_array()


# In[14]:


obj.append(5)


# In[15]:


obj.len_array()


# In[16]:


obj.print_array()


# In[17]:


obj.append(6)


# In[19]:


obj.print_array()


# In[20]:


obj.getitem(5)

