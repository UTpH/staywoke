'''
author : pH
date : 09.02.2019
'''

from scipy.spatial import distance
from imutils import face_utils
import xml.dom.minidom
import requests
import imutils
import random
import time
import dlib
import cv2


def eye_aspect_ratio(eye):
    A = distance.euclidean(eye[1], eye[5])
    B = distance.euclidean(eye[2], eye[4])
    C = distance.euclidean(eye[0], eye[3])
    ear = (A + B) / (2.0 * C)
    return ear

thresh = 0.25
frame_check = 20
detect = dlib.get_frontal_face_detector()

# to identify facial landmarks
predict = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]
cap = cv2.VideoCapture(0)
flag = 0

# blaster songs
songs = ['pink.mp3', 'imagine_dragons.mp3', 'the_nights.mp3']

# speaker's IP
ipaddr = "192.168.1.174"
service = "testing"
reason = "this"
message = "method."
# API key
Key = "ku1IYMERCz8iqwNsMFDMSJJZ1kfYyOhA"

# volume of speaker
volumeVal = "25"

while True:
    ret, frame = cap.read()
    frame = imutils.resize(frame, width=450)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    subjects = detect(gray, 0)
    for subject in subjects:
        shape = predict(gray, subject)
        shape = face_utils.shape_to_np(shape)  # converting to NumPy Array
        leftEye = shape[lStart:lEnd]
        rightEye = shape[rStart:rEnd]
        leftEAR = eye_aspect_ratio(leftEye)
        rightEAR = eye_aspect_ratio(rightEye)
        ear = (leftEAR + rightEAR) / 2.0
        leftEyeHull = cv2.convexHull(leftEye)
        rightEyeHull = cv2.convexHull(rightEye)
        cv2.drawContours(frame, [leftEyeHull], -1, (0, 0, 139), 1)
        cv2.drawContours(frame, [rightEyeHull], -1, (0, 0, 139), 1)
        if ear < thresh:
            flag += 1
            print(flag)
            if flag >= frame_check: 
                # print ALERT on screen upon drowsy detection
                cv2.putText(frame, "****************ALERT!****************", (10, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                cv2.putText(frame, "****************ALERT!****************", (10, 325),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                # random song selected and song url formed
                song = random.choice(songs)
                url = 'https://radsn23.github.io/' + song
               
                sendXML = "<play_info><app_key>" + Key + "</app_key><url>" + url + "</url><service>" + service + "</service><reason>" + reason + "</reason><message>" + message + "</message><volume>" + volumeVal + "</volume></play_info>"
                # form and send the /speaker POST request to start song
                send = requests.post('http://' + ipaddr + ':8090/speaker', data=sendXML)
      
        else:
            flag = 0
            # form and send the /speaker GET request to stop song
            stop = requests.get('http://' + ipaddr + ':8090/standby')

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
cv2.destroyAllWindows()
cap.stop()
