#include <opencv2/opencv.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <iostream>

using namespace cv;
using namespace std;

//*****************TO CLOSE PRESS ESC*************************

int main(int argc, char* argv[]) {
    VideoCapture cap(0);
    if (!cap.isOpened()) {
        cout << "ERROR INITIALIZING VIDEO CAPTURE" << endl;
	return -1;
    }
    
    string windowName = "Webcam feed";
    namedWindow(windowName, CV_WINDOW_AUTOSIZE);
    
    while(true) {
        Mat frame;
        bool success = cap.read(frame);
        if(!success) {
            cout << "error" << endl;
            break;
        }
        imshow(windowName, frame);
        switch(waitKey(10)) {
            case 27:
                return 0;
        }
    }
    return 0;
}