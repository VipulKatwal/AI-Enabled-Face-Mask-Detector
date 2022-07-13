# AI-Enabled-Face-Mask-Detector
This project is recognizes human face who wear face mask or not.


Using this project, human faces can be recognized whether or not they are wearing face masks.

//////////////// PLEASE NOTE: JUPITER NOTEBOOK IS RECOMEMNDED FOR THIS PROJECT ////////////////////******

LANGUAGE AND INSTALLATION PACKAGES:

Language: Python

Packages: TensorFlow, OpenCV, NumPy, Keras.

HARDARE REQUIREMENTS (Minimum Requirements):

Minimum RAM: 4GB

Hard Disk: 128GB

Processor: Intel Pentium (2.0 GHz) or above

SOFTWARE REQUIREMENTS:

Operating System: Windows 7 or later,

Python: 3.5 or later

GPU Support: NVIDIA® GPU drivers —CUDA®

11.0 requires 450.x or higher.

Pip: 19.0 or later

OVERVIEW OF THE PROJECT:

The goal of face detection is to determine if there are any faces in the image or video. If multiple faces are present, each face is enclosed by a bounding box and thus we know the location of the faces. Human faces are difficult to model as there are many variables that can change for example facial expression, orientation, lighting conditions and partial occlusions such as sunglasses, scarf, mask etc. The result of the detection gives the face location parameters and it could be required in various forms, for instance, a rectangle covering the central part of the face, eye centers or landmarks including eyes, nose and mouth corners, eyebrows, nostrils, etc.

Face Detection Methods:

There are two main approaches for Face Detection:

Feature Base Approach

Image Base Approach

Feature Base Approach: Objects are usually recognized by their unique features. There are many features in a human face, which can be recognized between a face and many other objects. It locates faces by extracting structural features like eyes, nose, mouth etc. and then uses them to detect a face. Typically, some sort of statistical classifier qualified then helpful to separate between facial and non-facial regions. In addition, human faces have particular textures which can be used to differentiate between a face and other objects. Moreover, the edge of features can help to detect the objects from the face. In the coming section, we will implement a feature-based approach by using OpenCV.

Image Base Approach: In general, Image-based methods rely on techniques from statistical analysis and machine learning to find the relevant characteristics of face and non-face images. The learned characteristics are in the form of distribution models or discriminant functions that is consequently used for face detection.

////////************ I HAVE ONLY PROVIDED A SMALL AMOUNT OF DETAIL HERE. *********//////////
