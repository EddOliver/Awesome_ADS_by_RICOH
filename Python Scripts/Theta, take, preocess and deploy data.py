# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 23:14:14 2019

@author: VAI
"""

# importing the requests library 
import requests 
import json
import shutil
import cv2 as cv
import argparse
import pickle
import time

check=0

# obj0, obj1, obj2 are created here...

def getFaceBox(net, frame, conf_threshold=0.7):
    frameOpencvDnn = frame.copy()
    frameHeight = frameOpencvDnn.shape[0]
    frameWidth = frameOpencvDnn.shape[1]
    blob = cv.dnn.blobFromImage(frameOpencvDnn, 1.0, (300, 300), [104, 117, 123], True, False)

    net.setInput(blob)
    detections = net.forward()
    bboxes = []
    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > conf_threshold:
            x1 = int(detections[0, 0, i, 3] * frameWidth)
            y1 = int(detections[0, 0, i, 4] * frameHeight)
            x2 = int(detections[0, 0, i, 5] * frameWidth)
            y2 = int(detections[0, 0, i, 6] * frameHeight)
            bboxes.append([x1, y1, x2, y2])
            cv.rectangle(frameOpencvDnn, (x1, y1), (x2, y2), (0, 255, 0), int(round(frameHeight/150)), 8)
    return frameOpencvDnn, bboxes

parser = argparse.ArgumentParser(description='Use this script to run age and gender recognition using OpenCV.')
parser.add_argument('--input', help='Path to input image or video file. Skip this argument to capture frames from a camera.')

args = parser.parse_args()

faceProto = "opencv_face_detector.pbtxt"
faceModel = "opencv_face_detector_uint8.pb"

ageProto = "age_deploy.prototxt"
ageModel = "age_net.caffemodel"

genderProto = "gender_deploy.prototxt"
genderModel = "gender_net.caffemodel"

faceCascade = cv.CascadeClassifier("haarcascade_frontalface_alt.xml")

MODEL_MEAN_VALUES = (78.4263377603, 87.7689143744, 114.895847746)
ageList = ['(0-2)', '(4-6)', '(8-12)', '(15-20)', '(25-32)', '(38-43)', '(48-53)', '(60-100)']
genderList = ['Male', 'Female']

# Load network
ageNet = cv.dnn.readNet(ageModel, ageProto)
genderNet = cv.dnn.readNet(genderModel, genderProto)
faceNet = cv.dnn.readNet(faceModel, faceProto)

while(True):
    start = time.time()
    # defining the api-endpoint 
    API_ENDPOINT = "http://192.168.1.1:80/osc/commands/execute"
    
    # your API key here 
    data = {"name":"camera.takePicture"} 
    
    headers={"Content-Type":"application/json"}
    
    # sending post request and saving response as response object 
    r = requests.post(url = API_ENDPOINT, data = json.dumps(data),headers=headers) 
    
    # extracting response text 
    pastebin_url = r.text 
    
    print("Take Picture Complete") 
    
    idp=json.loads(r.text)["id"]
    
    print("Checking Url") 
    
    API_ENDPOINT = "http://192.168.1.1:80/osc/commands/status"
    
    # your API key here 
    data = {"id":idp} 
    
    headers={"Content-Type":"application/json"}
    
    # sending post request and saving response as response object 
    r = requests.post(url = API_ENDPOINT, data = json.dumps(data),headers=headers) 
    
    # extracting response text 
    pastebin_url = json.loads(r.text) 
    
    while (json.loads(r.text)["state"]!= "done"):
        r = requests.post(url = API_ENDPOINT, data = json.dumps(data),headers=headers)
        pastebin_url = json.loads(r.text)
        print(".", end = '')
    print("")
    print("Check Url Complete") 
    
    img_url = pastebin_url["results"]["fileUrl"]
    
    with open('image.png', 'wb') as output_file,\
    	requests.get(img_url, stream=True) as response:
    	shutil.copyfileobj(response.raw, output_file)
        
    
    print("Save Image Complete Complete") 
        
    API_ENDPOINT = "http://192.168.1.1:80/osc/commands/execute"
    
    # your API key here 
    data = { 
        "name": "camera.delete", 
        "parameters": 
        {
        	"fileUrls":
        	[img_url]
        	
        }
    }
    
    headers={"Content-Type":"application/json"}
    
    # sending post request and saving response as response object 
    r = requests.post(url = API_ENDPOINT, data = json.dumps(data),headers=headers) 
    
    # extracting response text 
    pastebin_url = r.text 
    
    print("Delete Image From Internal Storage Complete") 
    
    frame = cv.imread("image.png")
    
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv.CASCADE_SCALE_IMAGE
    )
    var=0
    
    male=0
    female=0
    
    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        try:
            var=var+1
            cloneframe = frame[(y-200):y+h+200, (x-200):x+w+200] 
            
            padding=20
            
            frameFace, bboxes = getFaceBox(faceNet, cloneframe)
            
            for bbox in bboxes:
                # print(bbox)
                face = cloneframe[max(0,bbox[1]-padding):min(bbox[3]+padding,cloneframe.shape[0]-1),max(0,bbox[0]-padding):min(bbox[2]+padding, cloneframe.shape[1]-1)]
                blob = cv.dnn.blobFromImage(face, 1.0, (227, 227), MODEL_MEAN_VALUES, swapRB=False)
                genderNet.setInput(blob)
                genderPreds = genderNet.forward()
                gender = genderList[genderPreds[0].argmax()]
                if(gender=="Male"):
                    male=male+1
                else:
                    female=female+1
                #print("Gender : {}, conf = {:.3f}".format(gender, genderPreds[0].max()))
            
                ageNet.setInput(blob)
                agePreds = ageNet.forward()
                age = ageList[agePreds[0].argmax()]
                #print("Age Output : {}".format(agePreds))
                #print("Age : {}, conf = {:.3f}".format(age, agePreds[0].max()))
                label = "{},{}".format(gender, age)
                ##cv.putText(frameFace, label, (bbox[0], bbox[1]-10), cv.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2, cv.LINE_AA)
                ##cv.imwrite( "imageMod"+str(var)+".jpg", frameFace);
        except Exception as e:
            break
    
    if(male>female):
        check=0
    elif (male<female):
        check=1
    else:
        check=2
    
    with open('objs.pkl', 'wb') as f:  # Python 3: open(..., 'wb')
        pickle.dump(check, f)
    
    print(check)
    end = time.time()
    while((end - start)<20):
        time.sleep(1)
        end = time.time()
    print(end - start)
    