import cv2
import pygame
import time
import pickle

pygame.init()
pygame.mixer.init()

ads=[["ADS/M1.mp4","ADS/M2.mp4","ADS/M3.mp4"],["ADS/W1.mp4","ADS/W2.mp4","ADS/W3.mp4"]]
aads=[["ADS/M1.mp3","ADS/M2.mp3","ADS/M3.mp3"],["ADS/W1.mp3","ADS/W2.mp3","ADS/W3.mp3"]]
ad=0
mwcad=1
mmcad=0
gc=0
file_name = ""
window_name = "window"
interframe_wait_ms = 30
cv2.namedWindow(window_name, cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

while (True):
    with open("objs.pkl", "rb") as f:
        check = pickle.load(f)
    print(check)
    if(check==1):
        ad=1
        mwcad=mwcad+1
        if mwcad==3:
            mwcad=0
        gc=mwcad
    elif(check==0):
        ad=0
        mmcad=mmcad+1
        if mmcad==3:
            mmcad=0
        gc=mmcad
    else:
        if(ad==0):
            ad=1
            mwcad=mwcad+1
            if mwcad==3:
                mwcad=0
            gc=mwcad
        else:
            ad=0
            mmcad=mmcad+1
            if mmcad==3:
                mmcad=0
            gc=mmcad 
        
    videofile=ads[ad][gc]
    audiofile=aads[ad][gc]
    cap = cv2.VideoCapture(videofile)
    if not cap.isOpened():
        exit()
    pygame.mixer.music.load(audiofile)
    pygame.mixer.music.play(0)
    time.sleep(1.1)
    
    while (True):
        ret, frame = cap.read()
        if ret:
            cv2.imshow(window_name, frame)
        else:
            break
    
        if cv2.waitKey(interframe_wait_ms) & 0x7F == ord('q'):
            break

cap.release()
pygame.mixer.music.stop()
pygame.mixer.stop()
cv2.destroyAllWindows()