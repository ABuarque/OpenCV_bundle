# OpenCV_bundle

## Installing
+ get instaling script: https://github.com/ABuarque/OpenCV_bundle/blob/master/install-opencv.sh
+ put it into home directory and run ir : ./install-opencv.sh

## Java test (setup on eclipse)
+ Open eclipse
+ Create new project
+ Right click on project -> Build path -> Configure build path -> Add librar -> User library -> Next -> User library -> New -> Name as opencv -> Ok   
+ Click on it -> Add external jar and go to /OpenCV/build/bin and select the jar file -> ok
+ Click on Native library location -> External folder -> /OpenCV/build/lib -> ok
+ Right clik again on the src directory of project -> Build path -> Configure build path -> Edit -> select opencv -> ok
+ Run a simple code to test as shown here http://docs.opencv.org/2.4/doc/tutorials/introduction/java_eclipse/java_eclipse.html

## C++ test (setup on netbeans)
+ Open netbeans
+ Create new c++ project project
+ Open properties -> build -> C++
+ At Include Directories add the folder /usr/local/include/opencv2
+ Go to linker
+ At Aditional Libraries Directories add the folder /usr/local/lib
+ And at Libraries add all the so files inside the lib folder

