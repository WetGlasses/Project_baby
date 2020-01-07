import keras
from keras.models import model_from_json

print('Started')
model = keras.applications.inception_v3.InceptionV3(include_top=True, weights= None, input_shape=(150, 150, 3), input_tensor=None, pooling=None, classes=1000)
print('Downloaded')
model_json = model.to_json()
with open("arch.json", "w") as json_file:
    json_file.write(model_json)
print('Saved')
