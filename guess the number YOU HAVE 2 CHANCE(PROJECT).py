#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
a=random.randint(0,99)



j=3
for i in range(0,3):
    
    j=j-1
    b=int(input("guess any number (0,99)"))
    print("chance left:",j)
    if (a>b):
        print("your number is too low")
        print("try again")
    elif(a<b):
        print("ypur number is too high")
        print("try again")
    else:
        print("your number is correct")
        break
        
        
        
print("random value is:",a)
    
            
    


# In[4]:


import multiprocessing
print("multiprocsiing.cpu_count")


# In[ ]:




