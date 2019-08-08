import cv2 as cv
import time
import numpy as np
import amcrest
import time
test=1
speed = 1
fps = 30

ip = "192.168.1.108"
port = "80"
username = "admin"
password = "internsarethebest1"
url = "rtsp://" + username + ":" + password + "@" + ip + ":" + port + "/cam/realmonitor?channel=1&subtype=0"
cam = amcrest.AmcrestCamera(ip, port, username, password).camera
moved = False
speed=1
video = cv.VideoCapture(url)


def move(dir): 
    moved = True
    cam.ptz_control_command(action="start", code=dir, arg1=0, arg2=speed, arg3=0)

while True:
    _, frame = video.read()

    cv.imshow(('Camera'), frame)

    key = cv.waitKey(1) & 0xFF
    
    if key == ord('q'):
        break
###  for adding photos MAKE SURE THE PATH IS CORRECT FOR THE PERSON
  #  if key == ord(' '):
     #   cam.snapshot(path_file="unprocessed_dataset/Alex_Valente/%d.jpg"%(test))
     #   test=test+1
    elif key == ord('w'):
        move("Up")
        time.sleep(0.5)
        cam.ptz_control_command(action="stop", code="Up", arg1=0, arg2=speed, arg3=0)
    elif key == ord('a'):
        move("Left")
        time.sleep(0.5)
        cam.ptz_control_command(action="stop", code="Left", arg1=0, arg2=speed, arg3=0)
    elif key == ord('s'):
        move("Down")
        time.sleep(0.5)
        cam.ptz_control_command(action="stop", code="Down", arg1=0, arg2=speed, arg3=0)
    elif key == ord('d'):
        move("Right")
        time.sleep(0.5)
        cam.ptz_control_command(action="stop", code="Right", arg1=0, arg2=speed, arg3=0)
    elif key == ord('+'):
        cam.zoom_in(action="start")
        time.sleep(0.5)
        cam.zoom_in(action="stop")
    elif key == ord('-'):
        cam.zoom_out(action="start")
        time.sleep(0.5)
        cam.zoom_out(action="stop")
   # elif moved:
  #      moved = False
   #     cam.ptz_control_command(action="stop", code="Up", arg1=0, arg2=0, arg3=0)
    #    cam.ptz_control_command(action="stop", code="Down", arg1=0, arg2=0, arg3=0)
     #   cam.ptz_control_command(action="stop", code="Left", arg1=0, arg2=0, arg3=0)
     #   cam.ptz_control_command(action="stop", code="Right", arg1=0, arg2=0, arg3=0)

cv.destroyAllWindows()
