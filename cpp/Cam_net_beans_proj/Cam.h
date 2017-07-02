#ifndef CAM_H
#define CAM_H

#include <opencv2/opencv.hpp>
#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <string>

class Cam {
private:
    cv::VideoCapture cam;
    cv::VideoWriter writer;
    
    std::string windowName;
    int picCounter;
    int videoCounter;
    
    bool isRecording = false;
    bool isAvailableForVideo = true;
    
public:
    
    Cam(int cameraIndex);
    Cam();
    ~Cam();
    
    void takePicture();
    
    /**
     * 
     * Press p to take a picture
     * Press r to start recording / pause / resume recording
     * Press s to stop recording
     * Press esc to finish 
     */
    void fullOperation();
};

#endif
