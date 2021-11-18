#!/usr/bin/env python
# coding: utf-8

# # Removing duplicates using python

# This can be done using the following methods:
# * Naive method - In naive method, we simply traverse the list and append the first occurrence of the element in new list and ignore all the other occurrences of that particular element.
# 
# * Using list comprehension - This method has working similar to the above method, but this is just a one-liner shorthand of longer method done with the help of list comprehension.
# 
# * Using set() - This is the most popular way by which the duplicated are removed from the list. But the main and notable drawback of this approach is that the ordering of the element is lost in this particular method.
# 
# * Using list comprehension + enumerate() - list comprehension coupled with enumerate function can also achieve this task. It basically looks for already occurred elements and skips adding them. It preserves the list ordering.
# 
# * Using collections.OrderedDict.fromkeys() - This is fastest method to achieve the particular task. It first removes the duplicates and returns a dictionary which has to be converted to list. This works well in case of strings also.

# In[3]:


demo_list = [1, 3, 7, 2, 7, 5, 3, 8, 1, 4, 8, 6]
print("Original list: ", demo_list)

# now using the naive method to remove duplicates
new_list = []
for n in demo_list:
    if n not in new_list:
        new_list.append(n)
# printing new list
print("New list without duplicates: ", new_list)


# In[1]:


demo_list = [1, 3, 7, 2, 7, 5, 3, 8, 1, 4, 8, 6]
print("Original list: ", demo_list)

# now using the list comprehension method to remove duplicates
new_list = []
[new_list.append(n) for n in demo_list if n not in new_list]

print("New list without duplicates: ", new_list)


# In[1]:


demo_list = [1, 3, 7, 2, 7, 5, 3, 8, 1, 4, 8, 6]
print("Original list: ", demo_list)

# now using the set() method to remove duplicates
# converting the original list into a set which doesn't store duplicate records and then converting the set back to a list 
new_list = list(set(demo_list))

print("New list without duplicates: ", new_list)


# >> To make it more clearer

# In[2]:


demo_list = [1, 3, 7, 2, 7, 5, 3, 8, 1, 4, 8, 6]
print("Original list: ", demo_list)

# converting list to a set first which doesn't allow duplicate records & printing
new_set_list = set(demo_list)
print("The set after converting the list: ", new_set_list)

# converting set back into a list and printing
new_list = list(new_set_list)

print("New list without duplicates: ", new_list)


# In[3]:


demo_list = [1, 3, 7, 2, 7, 5, 3, 8, 1, 4, 8, 6]
print("Original list: ", demo_list)

new_list = [i for n, i in enumerate(demo_list) if i not in demo_list[:n]]
print("New list without duplicates: ", new_list)


# In[4]:


from collections import OrderedDict

demo_list = [1, 3, 7, 2, 7, 5, 3, 8, 1, 4, 8, 6]
print("Original list: ", demo_list)

# using collections.OrderedDict.fromkeys()
new_list = list(OrderedDict.fromkeys(demo_list))
print("New list without duplicates: ", new_list)


# >> more simpler for the above method

# In[8]:


from collections import OrderedDict

demo_list = [1, 3, 7, 2, 7, 5, 3, 8, 1, 4, 8, 6]
print("Original list: ", demo_list)

# using collections.OrderedDict.fromkeys() to convert list into a dictionary first and printing
new_dict = OrderedDict.fromkeys(demo_list)
print("The dictionary: ", new_dict)

# converting the dictionary
new_list = list(new_dict)
print("New list without duplicates: ", new_list)


# In[ ]:




