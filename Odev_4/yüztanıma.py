import cv2
from time import time

camera=cv2.VideoCapture(0)
yuz=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
zaman=0
merkezler=[]
tolerans=0.25
tespit= False
ctime=time()

while True:
    ret,frame=camera.read()
    if not ret:
        print("HATA!")
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    yuzler = yuz.detectMultiScale(gray, 1.2, 6, minSize=(80, 80))

    if len(yuzler)>0:
        if not tespit: #ilk tespit değil ise
             zaman = time() 
             tespit = True #artık tespit edildi
        ctime=time()

        for x1,y1,w,h in yuzler:
             x2=w+x1
             y2=h+y1
             cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
             m1=int((x1+x2)/2)
             m2=int((y1+y2)/2)
             cv2.putText(frame,f"merkez:{m1},{m2}",(435,20),cv2.FONT_HERSHEY_SIMPLEX,0.75,(0,0,255),2,cv2.LINE_AA)
        
        if not merkezler:
          merkezler.append((m1,m2))
        else:  
          son_m1, son_m2 = merkezler[-1]
          if  -50<(m1-son_m1)<50 and -50<m2-son_m2<50:
             merkezler.append((m1,m2))
             for i in range(1,len(merkezler)):
                 cv2.line(frame,merkezler[i-1],merkezler[i],(255,0,255),2)
             if len(merkezler)>60:
                 merkezler.pop(0) #baştakini kaldır 
  
        sayac=int(time()-zaman)
        cv2.putText(frame,f"zaman:{sayac}",(10,20),cv2.FONT_HERSHEY_SIMPLEX,0.75,(0,0,255),2,cv2.LINE_AA)   

    else:
         if (time()-ctime)>tolerans:
             tespit=False  
             merkezler=[]

    cv2.imshow("ekran",frame)
    if cv2.waitKey(5)==ord("q"):
          break

    
   
   
camera.release()    
cv2.destroyAllWindows()   