import numpy as np
import os
import cv2
import time
from ultralytics import YOLO
import matplotlib.pyplot as plt
# define some parameters
CONFIDENCE = 0.5
font_scale = 1
thickness = 1
cap = cv2.VideoCapture('videos/subject11-18-Train1.avi')
# loading the YOLOv8 model with the default weight file
model = YOLO("yolov8x.pt")

# loading all the class labels (objects)
labels = open("config/coco.names").read().strip().split("\n")

# generating colors for each object for later plotting
colors = np.random.randint(0, 255, size=(len(labels), 3), dtype="uint8")

count = 0
wide = 0.1  # depends upon size of car(~2.5)
flag = True

start = end = 0
time_diff = 0
# Distance between two horizontal lines in (meter)
dist = 3
currencies = 0
veloc1 = 0
veloc2 = 0
veloc3 = 0
veloc4 = 0
veloc5 = 0
veloc6 = 0
veloc7 = 0
veloc8 = 0
#######
acce1 = 0
acce2 = 0
acce3 = 0
acce4 = 0
acce5 = 0
acce6 = 0
acce7 = 0
acce8 = 0

tim1=0
tim2=0
tim3=0
tim4=0
tim5=0
tim6=0
tim7=0
tim8=0
tim9=0
while (cap.isOpened()):
    ret, frame = cap.read()
    image = frame
    
    coord00 = [[220, 300], [130, 400]]
    cv2.line(image, (coord00[0][0], coord00[0][1]), (coord00[1][0], coord00[1][1]), (0, 0, 255), 2)

    coord0 = [[285, 300], [215, 400]]
    cv2.line(image, (coord0[0][0], coord0[0][1]), (coord0[1][0], coord0[1][1]), (0, 0, 255), 2)

    coord1 = [[350, 300], [300, 400]]
    cv2.line(image, (coord1[0][0], coord1[0][1]), (coord1[1][0], coord1[1][1]), (0, 0, 255), 2)

    coord2 = [[415, 300], [390, 400]]
    cv2.line(image, (coord2[0][0], coord2[0][1]), (coord2[1][0], coord2[1][1]), (0, 0, 255), 2)

    coord3 = [[475, 300], [477, 400]]
    cv2.line(image, (coord3[0][0], coord3[0][1]), (coord3[1][0], coord3[1][1]), (0, 0, 255), 2)

    coord4 = [[550, 300], [560, 400]]
    cv2.line(image, (coord4[0][0], coord4[0][1]), (coord4[1][0], coord4[1][1]), (0, 0, 255), 2)

    coord5 = [[620, 300], [645, 400]]
    cv2.line(image, (coord5[0][0], coord5[0][1]), (coord5[1][0], coord5[1][1]), (0, 0, 255), 2)

    coord6 = [[685, 300], [730, 400]]
    cv2.line(image, (coord6[0][0], coord6[0][1]), (coord6[1][0], coord6[1][1]), (0, 0, 255), 2)

    coord7 = [[750, 300], [825, 400]]
    cv2.line(image, (coord7[0][0], coord7[0][1]), (coord7[1][0], coord7[1][1]), (0, 0, 255), 2)
   
    # run inference on the image 
    results = model.predict(image, conf=CONFIDENCE)[0]

    # loop over the detections
    for data in results.boxes.data.tolist():
        # get the bounding box coordinates, confidence, and class id 
        xmin, ymin, xmax, ymax, confidence, class_id = data
         
        # converting the coordinates and the class id to integers
        xmin = int(xmin)
        ymin = int(ymin)
        xmax = int(xmax)
        ymax = int(ymax)
        class_id = int(class_id)
        
        # draw a bounding box rectangle and label on the image
        color = [int(c) for c in colors[class_id]]
        cv2.rectangle(image, (xmin, ymin), (xmax, ymax), color=color, thickness=thickness)
        text = f"{labels[class_id]}: {confidence:.2f}"
        # calculate text width & height to draw the transparent boxes as background of the text
        (text_width, text_height) = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, fontScale=font_scale, thickness=thickness)[0]
        text_offset_x = xmin
        text_offset_y = ymin - 5
        box_coords = ((text_offset_x, text_offset_y), (text_offset_x + text_width + 2, text_offset_y - text_height))
        overlay = image.copy()
        cv2.rectangle(overlay, box_coords[0], box_coords[1], color=color, thickness=cv2.FILLED)
        # add opacity (transparency to the box)
        image = cv2.addWeighted(overlay, 0.6, image, 0.4, 0)
        # now put the text (label: confidence %)
        cv2.putText(image, text, (xmin, ymin - 5), cv2.FONT_HERSHEY_SIMPLEX,fontScale=font_scale, color=(0, 0, 0), thickness=thickness)
        x=xmin
        y=xmin
        #print('x>=coord00[0][0]', x == coord00[0][0])
        #print('y==coord00[0][1]', y >= coord00[0][1])
        #print('x', x, coord00[0][0], coord00[1][0])
        #print('text_offset_x, text_offset_y : ', text_offset_x, text_offset_y)
        # cv2.waitKey(0)
        if (x >= 35 and x <= 198):
            tim1 = time.time()  # Initial time
            break

        if (x >= 199 and x <= 261):
            tim2 = time.time()  # Final time
            veloc1 = dist / (tim2 - tim1)
            acce1 = (veloc1 - 0) / (tim2 - tim1)
            print("acceleration in 1 box (m/s) is:", (veloc1 - 0) / ((tim2 - tim1)))
            print("Speed in 1 box (m/s) is:", dist / ((tim2 - tim1)))
            break

        if (x >= 262 and x <= 345):
            tim3 = time.time()  # Final time
            veloc2 = dist / (tim3 - tim2)
            acce2 = (veloc2 - veloc1) / (tim3 - tim2)
            print("acceleration in 2 box (m/s) is:", (veloc2 - veloc1) / ((tim3 - tim2)))
            print("Speed in 2 box (m/s) is:", dist / ((tim3 - tim2)))
            break
        if (x >= 346 and x <= 422):
            tim4 = time.time()  # Final time
            veloc3 = dist / (tim4 - tim3)
            acce3 = (veloc3 - veloc2) / (tim4 - tim3)
            print("acceleration in 3 box (m/s) is:", (veloc3 - veloc2) / ((tim4 - tim3)))
            print("Speed in 3 box (m/s) is:", dist / ((tim4 - tim3)))
            break
        if (x >= 423 and x <= 493):
            tim5 = time.time()  # Final time
            veloc4 = dist / (tim5 - tim4)
            acce4 = (veloc4 - veloc3) / (tim5 - tim4)
            print("acceleration in 4 box (m/s) is:", (veloc4 - veloc3) / ((tim5 - tim4)))
            print("Speed in 4 box (m/s) is:", dist / ((tim5 - tim4)))
            break
        if (x >= 494 and x <= 600):
            tim6 = time.time()  # Final time
            # print('tim2-tim1',tim2-tim1)
            veloc5 = dist / (tim6 - tim5)
            acce5 = (veloc5 - veloc4) / (tim6 - tim5)
            print("acceleration in 5 box (m/s) is:", (veloc5 - veloc4) / ((tim6 - tim5)))
            print("Speed in 5 box (m/s) is:", dist / ((tim6 - tim5)))
            break
        if (x >= 601 and x <= 669):
            tim7 = time.time()  # Final time
            veloc6 = dist / (tim7 - tim6)
            acce6 = (veloc6 - veloc5) / (tim7 - tim6)
            print("acceleration in 6 box (m/s) is:", (veloc6 - veloc5) / ((tim7 - tim6)))
            print("Speed in 6 box (m/s) is:", dist / ((tim7 - tim6)))
            break
        if (x >= 670 and x <= 755):
            tim8 = time.time()  # Final time
            veloc7 = dist / (tim8 - tim7)
            acce7 = (veloc7 - veloc6) / (tim8 - tim7)
            print("acceleration in 7 box (m/s) is:", (veloc7 - veloc6) / ((tim8 - tim7)))
            print("Speed in 7 box (m/s) is:", dist / ((tim8 - tim7)))
            break
        if (x >= 756):
            tim9 = time.time()  # Final time
            veloc8 = dist / (tim9 - tim8)
            acce8 = (veloc8 - veloc7) / (tim9 - tim8)
            print("acceleration in 8 box (m/s) is:", (veloc8 - veloc7) / ((tim9 - tim8)))
            print("Speed in 8 box (m/s) is:", dist / ((tim9 - tim8)))
            break

        break

    aveage_veloc = (veloc1 + veloc2 + veloc3 + veloc4 + veloc5 + veloc6 + veloc7 + veloc8) / 8
    aveage_acce = (acce1 + acce2 + acce3 + acce4 + acce5 + acce6 + acce7 + acce8) / 8
    print('aveage Speed', aveage_veloc)
    print('aveage acceleration', aveage_acce)
        
    # Output img with window name as 'image'
    cv2.imshow('image', image)
    # Maintain output window utill 
    # user presses a key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
# Destroying present windows on screen 
cv2.destroyAllWindows()
