from keras.models import load_model
import numpy as np
from keras.applications.imagenet_utils import decode_predictions
from keras.preprocessing import image

def preprocess_input(x):
    x /= 255.
    x -= 0.5
    x *= 2.
    return x

model = load_model('Inception_whole.h5')
img_path = 'dog_cat.jpg'
img = image.load_img(img_path, target_size=(299, 299))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)

x = preprocess_input(x)

preds = decode_predictions(model.predict(x))

preds = str(preds)
preds= list(preds)

name = ''
name_list = []
acc = ''
acc_list = []

x = 0
comma_cnt = 0

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

print(name_list)
print(acc_list)


