# OpenCV_bundle

# HOW TO USE THIS REPOSITORY
First, if you don't have opencv installed, install it (see how below). Then, go through the tutorials packages in python, java and c++ (python, java, cpp) to see how to handle common situations with the code. Here you can also see how to setup the IDE for your projects (see below).

## Installing
+ get instaling script: https://github.com/ABuarque/OpenCV_bundle/blob/master/install-opencv.sh
+ put it into home directory and run it : ./install-opencv.sh

## Java test (setup on eclipse)
+ Open eclipse
+ Create new project
+ Right click on project -> Build path -> Configure build path -> Add librar -> User library -> Next -> User library -> New -> Name as opencv -> Ok   
+ Click on it -> Add external jar and go to /OpenCV/build/bin and select the jar file -> ok
+ Click on Native library location -> External folder -> /OpenCV/build/lib -> ok
+ Right clik again on the src directory of project -> Build path -> Configure build path -> Edit -> select opencv -> ok
+ Grab a script test on scripts_test directory

## C++ test (setup on netbeans)
+ Open netbeans
+ Create new c++ project project
+ Open properties -> build -> C++
+ At Include Directories add the folder /usr/local/include/opencv2
+ Go to linker
+ At Aditional Libraries Directories add the folder /usr/local/lib
+ And at Libraries add all the so files inside the lib folder
+ Grab a script test on scripts_test directory

## C++ teste (setup on QT creator)
+ Open the .pro file
+ At the bottom add these lines:
  + INCLUDEPATH += /usr/local/include/opencv2
  + LIBS += -L/usr/local/lib ***(folowed by the sources you need. To find them type it on terminal: pkg-config --libs opencv)**

## Python test (using sublime)
+ If installation process was ok just do a simple test
+ Grab a script test on scripts_test director
