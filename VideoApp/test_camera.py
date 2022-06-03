import cv2

cam = cv2.VideoCapture(0, cv2.CAP_V4L)  # change port number (the first argument) if needed
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
