import cv2

from keras.models import load_model
import numpy as np
from keras.applications.imagenet_utils import decode_predictions
from keras.preprocessing import image

def preprocess_input(x):
    #x /= 255.
    x = np.true_divide(x,255.0)
    x -= 0.5
    x *= 2.
    return x

x_name = []

def recognition(image):
    global x_name
    
    img = cv2.resize(image, (299, 299))
    img = np.expand_dims(img, axis=0)

    img = preprocess_input(img)

    preds = decode_predictions(model.predict(img))

    preds = str(preds)
    preds= list(preds)

    name = ''
    name_list = []
    acc = ''
    acc_list = []

    x = 0
    comma_cnt = 0

    try:
        
        while(x < len(preds) ):
            if(preds[x]== "'"):
                comma_cnt = comma_cnt+1
                x=x+1
            if(comma_cnt==3):
                name = name+ preds[x]    
            x=x+1
            if(comma_cnt==4):
                #acc extract
                x=x+1
                while(preds[x]!= ')'):
                    acc = acc+ preds[x]
                    x=x+1
                acc = float(acc)
                #decision
                if(acc<.4):
                    break
                acc_list.append(acc)
                acc = ''
                name_list.append(name)
                name= ''
                comma_cnt = 0
    except:
        print('Handled an error')

    if((len(name_list)>0)&(x_name != name_list)):
        print(name_list)
        x_name = name_list

print('Loading Model')
model = load_model('inceptionv3.h5')
print('Model Loaded. I am ready to open my eyes now..')

cap = cv2.VideoCapture(0)
cv2.namedWindow('Raw')

while(True):
    ret, img = cap.read()
    cv2.imshow('Raw',img)
    recognition(img)
    if cv2.waitKey(5) & 0xFF == ord('o'):
        break
