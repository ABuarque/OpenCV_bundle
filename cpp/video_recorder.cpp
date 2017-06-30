#include <iostream>
#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>

using namespace std;
using namespace cv;

int main() {
    VideoCapture cap(0);
    if(!cap.isOpened()) {
        cout << "Error on creating video capture" << endl;
        return -1;
    }
    
    //video name with extension
    const string videoName = "myVideo.avi";
    
    //fps
    const int fps = 20;
    
    //fourcc
    const int fourcc = CV_FOURCC('M', 'J', 'P', 'G');
    
    //frame size object
    const Size frameSize = Size(cap.get(CV_CAP_PROP_FRAME_WIDTH), 
            cap.get(CV_CAP_PROP_FRAME_HEIGHT));

    VideoWriter writer = VideoWriter(videoName, fourcc, fps, frameSize);
    if(!writer.isOpened()) {
        cout << "Error opening writer" << endl;
        return -1;
    }
    const string windowName = "My window";
    namedWindow(windowName, CV_WINDOW_AUTOSIZE);
    while(true) {
        Mat frame;
        bool readOk = cap.read(frame);
        if(!readOk) {
            cout << "ERror on getting frame" << endl;
            return -1;
        }
        writer.write(frame);
        imshow(windowName, frame);
        if(waitKey(10) == 27) 
            break;
    }
    return 0;
}
