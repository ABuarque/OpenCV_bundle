#include "Cam.h"
#include <opencv2/opencv.hpp>
#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <iostream>

using namespace std;
using namespace cv;

Cam::Cam() {}

Cam::Cam(int cameraIndex) {
    this->windowName = windowName;
    this->windowName = "My Window";
    this->cam = VideoCapture(cameraIndex);
    if(!cam.isOpened()) 
        throw "Error on opening cam";
    this->picCounter = 0;
    this->videoCounter = 0;
}

Cam::~Cam() {}

void Cam::takePicture() {
    Mat frame;
    try {
        cam >> frame;
    } catch(exception& e) {
        cerr << e.what() << endl;    }
    
    imwrite("pic_" + to_string(picCounter++) + ".png", frame);
}

void Cam::fullOperation() {
    //video name with extension
    const string VIDEO_NAME = "video_";
    
    //foucc 
    const int FOURCC = CV_FOURCC('M', 'J', 'P', 'G');
    
    //fps
    const int FPS = 20;
    
    //frame size
    const Size FRAME_SIZE = Size(cam.get(CV_CAP_PROP_FRAME_WIDTH), 
            cam.get(CV_CAP_PROP_FRAME_HEIGHT));
    namedWindow(windowName, CV_WINDOW_AUTOSIZE);
    bool appOn = true;
    while(appOn) {
        Mat frame;
        cam >> frame;
         if(isRecording) {
            writer.write(frame);
            putText(frame, "REC", Point(0, 60), 2, 2, Scalar(0, 0, 255), 2);
        }     
        imshow(windowName, frame);
        switch(waitKey(10)) {
            case 112: // take picture
                imwrite("pic_" + to_string(picCounter++) + ".png", frame);
                cout << "Picture shot" << endl;
                break;
            case 114: //startVideo / pause video
                if(isAvailableForVideo) {
                    writer = VideoWriter(VIDEO_NAME + to_string(videoCounter) + ".avi", 
                                         FOURCC, FPS, FRAME_SIZE);
                    cout << "Started rec" << endl;
                    isAvailableForVideo = false;
                } else {
                    if(isRecording) {
                        isRecording = false; //pause
                        cout << "Rec paused" << endl;
                    } else {
                        isRecording = true; //resume rec
                        cout << "Rec resumed" << endl;
                    }
                }
                break;
            case 115: //stop video
                cout << "Stopped video" << endl;
                isAvailableForVideo = true;
                isRecording = false;
                videoCounter++;
                break;
            case 27: //finish
                appOn = false;
                break;
        }
    } 
}
