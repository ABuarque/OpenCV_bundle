#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <iostream>

#define DEBUG if(1)

using namespace std;
using namespace cv;

class Cam {
private:
    VideoCapture cap;
    
public:
    Cam();
    Cam(int cameraIndex);
    ~Cam();
    
    void openCam();
};


Cam::Cam() {}

Cam::Cam(int cameraIndex) {
    this->cap = VideoCapture(cameraIndex);
    if(!this->cap.isOpened()) 
        throw "Error on creating video cap";
}

Cam::~Cam() {}

void Cam::openCam() {
    DEBUG cout << "Iside openCam" << endl;
    const string windowName = "My window";
    namedWindow(windowName, CV_WINDOW_AUTOSIZE);
    while(true) {
        Mat frame;
        bool readOK = cap.read(frame);
        if(!readOK) {
            throw "Error on reading frame";
            break;
        }
        imshow(windowName, frame);
        if(waitKey(10) >= 0) break;
    }
}

int main() {
    Cam c;
    try {
        c = Cam(0);
        c.openCam();
    } catch(const char* msg) {
        cout << msg << endl;
    }
    return 0;
}
