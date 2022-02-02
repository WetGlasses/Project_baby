import keras

print('Started')
model = keras.applications.inception_v3.InceptionV3(include_top=True, weights= 'imagenet', input_tensor=None, input_shape=(299,299,3), pooling=None, classes=1000)
print('Downloaded')
model.save('Inception_whole.h5')
