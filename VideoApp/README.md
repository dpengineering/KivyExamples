# Video App

## Overview

Simple Kivy UI which shows you how to playback a video on your main
screen using cv2's VideoCapture. You can play a downloaded video or stream
camera output using this feature.

Take note that there is a `VIDEO_PATH` you can modify to reference a video on your
computer. 

For more information on how to use VideoCapture to stream from a camera, 
[check this out](https://appdividend.com/2022/03/19/python-cv2-videocapture/).

For a few of the webcams in the DPEA, you might need to modify what video encoding you
are using. For example, your code would look similar to the following --
```python
import cv2

cam = cv2.VideoCapture(2, cv2.CAP_V4L)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

while True:
    ret, frame = cam.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    print(cam.get(cv2.CAP_PROP_FPS))

cam.release()
cv2.destroyAllWindows()
```

The '2' argument inside the VideoCapture initialization corresponds to the port number of the camera. Usually,
if you are using an all-in-one computer, the computer's built-in webcam will be on port 0 and an external camera will
be on port 1 or 2. When in doubt, try out increasing port numbers starting at 0.

## Running the App
Ensure you are using a python interpreter with Kivy installed, navigate to the VideoApp folder, and run the following
in your terminal --
```
python3 VideoApp.py
```