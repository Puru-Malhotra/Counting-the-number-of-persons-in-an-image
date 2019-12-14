#!/usr/bin/env python
# coding: utf-8

# In[2]:


import face_recognition


# In[3]:


image = face_recognition.load_image_file("xyz.png")
face_landmarks_list = face_recognition.face_locations(image)


# In[4]:


print(face_lanmarks_list)


# In[7]:


from Ipython.display import Image
Image(filename = "xyz.png")


# In[6]:


print(f'There are {len(face_landmarks_list)} people in this image')


# In[ ]:




