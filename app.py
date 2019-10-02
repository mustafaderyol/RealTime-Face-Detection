import cv2

face_cascade = cv2.CascadeClassifier('C:\ProgramData\Anaconda3\Library\etc\haarcascades\haarcascade_frontalface_default.xml')

scale = 1.3
cap = cv2.VideoCapture(0)
while(True):
    ret,frame = cap.read()
    
    faces = face_cascade.detectMultiScale(frame, scale, 5)
    
    for(x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y),(x+w, y+h),(255,0,0), 2)
    
    cv2.imshow('frame',frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows() 