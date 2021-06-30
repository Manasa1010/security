import cv2
import random
import time
import dropbox 

startTime=time.time()

def take_snapShot():
    rand=random.randint(1,100)
    videoCaptureObject=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=videoCaptureObject.read()
        img_name="img"+str(rand)+".png"
        cv2.imwrite(img_name,frame)
        startTime=time.time()
        result=False
    
    
    print("Picture taken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()

    return(img_name)

def upload_file(img_name):
    access_token="wr2tO2OqL1oAAAAAAAAAARqTRhJFLdRiS7so97AS8UJffeX_wDMjhP4FVLtQ-YAC"
    file_from=img_name
    file_to="/securityFolder/"+img_name
    dbx=dropbox.Dropbox(access_token)
    with open(file_from,'rb') as f:
        dbx.files_upload(f.read(),file_to)
        print("file uploaded")

def main():
    while(True):
        if((time.time()-startTime)>=5):
            name=take_snapShot()
            upload_file(name)

main()


