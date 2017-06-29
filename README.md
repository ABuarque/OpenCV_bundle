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
+ Grab a script test on scripts_test directory

## C++ test (setup on netbeans)
+ Open netbeans
+ Create new c++ project project
+ Open properties -> build -> C++
+ At Include Directories add the folder /usr/local/include/opencv2
+ Go to linker
+ At Aditional Libraries Directories add the folder /usr/local/lib
+ And at Libraries add all the so files inside the lib folder
+ Grab a script test on scripts_test director

## Python test (using sublime)
+ If installation process was ok just do a simple test
+ Grab a script test on scripts_test director
