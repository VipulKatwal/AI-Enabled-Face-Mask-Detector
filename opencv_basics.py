#!/usr/bin/env python
# coding: utf-8

# ## **OpenCV Github Link** https://github.com/opencv

# In[1]:


import cv2 #Import the OpenCV Library
import numpy as np

print(cv2.__version__)


# ## CHAPTER 1
# 
# ### How to read, write, and display Images
# 
# 

# In[2]:


#Reading & Displaying an Image

img = cv2.imread('dog.jpg')
#imread enables us to read an Image
#The 2nd argumnet is a flag which specifies the way image should be read

cv2.imshow("Output", img) #Displaying the Image

cv2.waitKey(0) #Delay. No. of Milliseconds for which we want to show our image window
cv2.destroyAllWindows()


# In[6]:


cv2.imwrite('copy_dog.jpg', img)


# ### How to read, write, and display Videos
# 

# In[8]:


#Reading & Displaying a Video

cap = cv2.VideoCapture(0) #If you want to display the Video File, just give the name of it inplace of 0

# is a 4-byte identifier which specifies the format of a video stream

fourcc = cv2.VideoWriter_fourcc('X','V','I','D') 

out = cv2.VideoWriter('Name of Output File.avi', fourcc, 20.0, (640,480)) #No. of frames/s, Frame Size

#Videos are just a sequence of Images
#So, we will add a while loop to capture the frame continuously

while True:
    success, frame = cap.read() #frame variable will capture the Video & success variable will tell us whether it was captured successfully or not
    
    if success == True:
        
        out.write(frame)
        
        cv2.imshow("Video", frame)
    
        if cv2.waitKey(1) == ord('q'): #This adds a Delay and looks for the key press inorder to break the loop
            break
            
    else:
        break
        
        
cap.release() #Release the resources after recording
out.release()
cv2.destroyAllWindows()


# In[27]:


#Reading & Displaying a Video

cap = cv2.VideoCapture(0)

cap.set(3, 640)#Width
cap.set(4, 480)#Height
cap.set(10, 100)#brightness

#Videos are just a sequence of Images
#So, we will add a while loop to go through each frame

while True:
    success, img = cap.read() #img variable will capture the Video & success variable will tell us whether it was captured successfully or not
    cv2.imshow("Video", img)
      
   
    if cv2.waitKey(1) & 0xFF == ord('q'): #This adds a Delay and looks for the key press inorder to break the loop
        break
        
cap.release() #Release the resources after recording
cv2.destroyAllWindows()


# ## CHAPTER 2
# 
# ### Basic Functions
# 
# 

# In[27]:


#Converting the Image into Gray Scale

#Reading an Image

img = cv2.imread('dog.jpg') 

imgGray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)#Converting the Image into Gray Scale

cv2.imshow('GrayScale Image',imgGray)

cv2.imwrite('copy_lena.png', imgGray)



#imgGray1 = cv2.cvtColor(imgGray, cv2.COLOR_GRAY2RGB)#Converting the Image into Gray Scale

#cv2.imshow('GrayScale Image1',imgGray1)


cv2.waitKey(0) #Delay. No. of Milliseconds for which we want to show our image window
cv2.destroyAllWindows()


# In[16]:


#Blur Function to Blur the Image

#Reading an Image

img = cv2.imread('dog.jpg') 

imgBlur = cv2.GaussianBlur(img, (21,21), 0)
#(7,7) is the Kernel Size (Amount of Blur) which is always odd. So, (3,3), (5,5), etc.
# 0 is Sig function (Standard Deviation along X-Direction) 

cv2.imshow('Blurred Image',imgBlur)

cv2.waitKey(0) #Delay. No. of Milliseconds for which we want to show our image window
cv2.destroyAllWindows()


# In[21]:


#Edge Detector - Canny 

img = cv2.imread('dog.jpg') #Reading an Image

imgCanny = cv2.Canny(img, 150, 200)#Threshold Values

kernel = np.ones((5,5), np.uint8)
#Type of the object which is unsigned integer of 8 bits which means the values can range from 0 to 255

imgDilation = cv2.dilate(imgCanny, kernel, iterations = 1)#dilate function is used when the Edges are not properly connected

imgErosion = cv2.erode(imgDilation, kernel, iterations = 1)#Erosion function is used when we want to thin (Erode) the Image


#iterations - How much thickness do we actually need?

cv2.imshow('Canny Image',imgCanny)
cv2.imshow('Dilation Image',imgDilation)
cv2.imshow('Erosion Image',imgErosion)


cv2.waitKey(0) #Delay. 0 Means Infinite Delay. No. of Milliseconds for which we want to show our image window
cv2.destroyAllWindows()


# In[3]:


#Resizing the Image

#Reading & Displaying an Image
import cv2
import numpy as np

img = cv2.imread('dog.jpg') 
#Reading an Image

cv2.imshow("Output", img) #Displaying the Image

print(img.shape) #Shape of the Image (Height, Width, No.of Channels(RGB))

cv2.waitKey(0) #Delay. 0 Means Infinite Delay. No. of Milliseconds for which we want to show our image window
cv2.destroyAllWindows()


# In[5]:


img_resize = cv2.resize(img, (200, 400)) # (Width, Height)

cv2.imshow("Original Image", img)
cv2.imshow("Re-sized Image", img_resize) #Displaying the Image

cv2.waitKey(0) #Delay. 0 Means Infinite Delay. If specified 1, it means 1 milliseconds
cv2.destroyAllWindows()


# In[12]:


#Cropping the Image

img = cv2.imread('dog.jpg') #Reading an Image

cv2.imshow("Output", img) #Displaying the Image

imgCropped = img[0:200, 200:500] #(Height, Width)

cv2.imshow("Cropped Image", imgCropped) #Displaying the Image

print(img.shape) #Shape of the Image (Height, Width, No.of Channels(BGR))

cv2.waitKey(0) #Delay. 0 Means Infinite Delay. If specified 1, it means 1 milliseconds
cv2.destroyAllWindows()


# ## CHAPTER 3
# 
# ### Shapes and Texts
# 

# In[8]:


#0 means Black

img = np.zeros((512, 512))#Print a Black Image. It is a GrayScale Image

cv2.imshow("O", img)

print(img.shape)

cv2.waitKey(0)
cv2.destroyAllWindows()


# In[18]:


#0 means Black

img = np.zeros((512, 512, 3),np.uint8 )#Print a Black Image with 3 Channles RGB.

#img[:] = 255, 0 , 0

cv2.line(img, (0,0), (300,300), (0,255,255),3) #Staring Pt., Ending Pt., Color, Thickness

cv2.imshow("O", img)

#print(img.shape)

cv2.waitKey(0)
cv2.destroyAllWindows()


# In[19]:


cv2.rectangle(img, (0,0), (250,350), (0, 255, 255), cv2.FILLED) #cv2.FILLED is used to Fill the Rectangles

cv2.imshow("O", img)

#print(img.shape)

cv2.waitKey(0)
cv2.destroyAllWindows()


# In[20]:


cv2.circle(img, (400,50), 30 , (0, 255, 255), cv2.FILLED) #Center, Radius , Color

cv2.imshow("O", img)

#print(img.shape)

cv2.waitKey(0)
cv2.destroyAllWindows()


# In[22]:


cv2.putText(img, "OpenCV", (300, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 150,0), 1) #Staring Pt., Font, Scale, Color, Thickness

cv2.imshow("O", img)

#print(img.shape)

cv2.waitKey(0)
cv2.destroyAllWindows()


# ## CHAPTER 4
# 
# ### Joining Images
# 

# In[13]:


#How to Join Image Together

img = cv2.imread('dog.jpg') #Reading an Image

imgHor = np.hstack((img, img))#Images stacked in Horizonatl Direction

cv2.imshow("Horizontal", imgHor) #Displaying the Image


cv2.waitKey(0)
cv2.destroyAllWindows()


# In[14]:


#How to Join Image Together

img = cv2.imread('dog.jpg') #Reading an Image

imgVer = np.vstack((img, img))#Images stacked in Horizonatl Direction

cv2.imshow("Vertical", imgVer) #Displaying the Image


#Both the Images must have same Channels because they have a matrix and we cannot resize the Images

cv2.waitKey(0)
cv2.destroyAllWindows()


# ## CHAPTER 5
# 
# ### Face Detection on an Image
# 

# In[14]:


faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img = cv2.imread('face.jpg') #Reading an Image

img = cv2.resize(img, (1240,640))
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x,y),(x+w,y+h),(0,0,255),2)

cv2.imshow("Output", img) #Displaying the Image

cv2.waitKey(0)
cv2.destroyAllWindows()


# ### Face Detection in Videos
# 

# In[15]:


import cv2
cap = cv2.VideoCapture('vid.mp4')

#Videos are just a sequence of Images
#So, we will add a while loop to capture the frame continuously

faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")


while True:
    success, frame = cap.read() #frame variable will capture the Video & success variable will tell us whether it was captured successfully or not
            
        
    imgGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
    
    cv2.imshow("Video", frame)
    
    if cv2.waitKey(1) == ord('q'): #This adds a Delay and looks for the key press inorder to break the loop
        break
            
        
cap.release() #Release the resources after recording
cv2.destroyAllWindows()


# ### Face Detection in Real-Time
# 

# In[1]:


import cv2
cap = cv2.VideoCapture(0) #If you want to display the Video File, just give the name of it inplace of 0

#Videos are just a sequence of Images
#So, we will add a while loop to capture the frame continuously

faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")


while True:
    success, frame = cap.read() #frame variable will capture the Video & success variable will tell us whether it was captured successfully or not
            
        
    imgGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),3)
    
    cv2.imshow("Video", frame)
    
    if cv2.waitKey(1) == ord('q'): #This adds a Delay and looks for the key press inorder to break the loop
        break
            
        
cap.release() #Release the resources after recording
cv2.destroyAllWindows()


# ### Face & Eyes Detection in Real-time

# In[10]:


#Face and Eyes Detection in Real-Time
cap = cv2.VideoCapture(0)

#Videos are just a sequence of Images
#So, we will add a while loop to capture the frame continuously

faceCascade = cv2.CascadeClassifier("haarcascade_eye.xml")
faceCascade1 = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")


while True:
    success, frame = cap.read() #frame variable will capture the Video & success variable will tell us whether it was captured successfully or not
            
        
    imgGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    eyes = faceCascade.detectMultiScale(imgGray, 1.1, 4)
    faces = faceCascade1.detectMultiScale(imgGray, 1.1, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,0),2)
    
    for (x, y, w, h) in eyes:
        cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,0),2)
    
    cv2.imshow("Video", frame)
    
    if cv2.waitKey(1) == ord('q'): #This adds a Delay and looks for the key press inorder to break the loop
        break
            
        
cap.release() #Release the resources after recording
cv2.destroyAllWindows()


# ### Pedestrians Detection

# In[11]:


cap = cv2.VideoCapture('vtest.avi') #note - insert a video link here

#Videos are just a sequence of Images
#So, we will add a while loop to capture the frame continuously

faceCascade = cv2.CascadeClassifier("haarcascade_fullbody.xml")


while True:
    success, frame = cap.read() #frame variable will capture the Video & success variable will tell us whether it was captured successfully or not
            
        
    imgGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,0),2)
    
    cv2.imshow("Video", frame)
    
    if cv2.waitKey(1) == ord('q'): #This adds a Delay and looks for the key press inorder to break the loop
        break
            
        
cap.release() #Release the resources after recording
cv2.destroyAllWindows()


# In[ ]:




