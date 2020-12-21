import cv2
import matplotlib.pyplot as plt
import os

xml_path1 = "C:\Anaconda3\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml"
xml_path2 = "C:\Anaconda3\Lib\site-packages\cv2\data\haarcascade_profileface.xml"
xml_path3 = "C:\Anaconda3\Lib\site-packages\cv2\data\haarcascade_frontalface_alt.xml"
xml_path4 = "C:\Anaconda3\Lib\site-packages\cv2\data\haarcascade_frontalface_alt_tree.xml"
xml_path5 = "C:\Anaconda3\Lib\site-packages\cv2\data\haarcascade_frontalface_alt2.xml"

face_classifier  = cv2.CascadeClassifier(xml_path1)
face_classifier2 = cv2.CascadeClassifier(xml_path2)
face_classifier3 = cv2.CascadeClassifier(xml_path3)
face_classifier4 = cv2.CascadeClassifier(xml_path4)
face_classifier5 = cv2.CascadeClassifier(xml_path5)





def face_detecting(data):
    img = cv2.imread(data)
    try:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_classifier.detectMultiScale(gray, 1.3, 5)
        if len(faces) ==0:
            faces = face_classifier2.detectMultiScale(gray,1.3,5)   
            if len(faces) ==0:
                faces = face_classifier3.detectMultiScale(gray,1.3,5)          
                if len(faces) ==0:
                    faces = face_classifier4.detectMultiScale(gray,1.3,5)     
                    if len(faces) ==0:
                        faces = face_classifier5.detectMultiScale(gray,1.3,5)                   
                        if len(faces) ==0:
                            return []
    except:
        return []

    if len(faces) != 0:
        result = []
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            result.append(roi_gray)
        return result
    else:
        return []

if __name__ =='__main__':
    data_path = {
        'su':'./image_data/origin_data/su',
        'nam' : './image_data/origin_data/nam'
    }
    save_path = {
        'su':'D:/project/face_detecting_project/image_data/gray_data/su/',
        'nam' :  'D:/project/face_detecting_project/image_data/gray_data/nam/'
        }

for key in data_path.keys():
    names = os.listdir(data_path[key])

    count =0
    print(key)
    for name in names:
        data = os.path.join(data_path[key],name)
        detected_img = face_detecting(data)
        if len(detected_img) != 0 :
            for img in detected_img:
                tmp = cv2.resize(img,(200,200))
                cv2.imwrite(save_path[key]+str(count)+'.png', tmp)
                count += 1

