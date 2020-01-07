from keras.models import model_from_json
from contextlib import redirect_stdout 

print('Architecture Loading..')
json_file = open('arch.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
model = model_from_json(loaded_model_json)
print('Architecture Loaded')

print('Weights Loading..')
model.load_weights("weight.h5")
print('Weights Loaded')

print('Getting Summary')

with open('Summary.txt', 'w') as f:
    with redirect_stdout(f):
        model.summary()
        
print('Saved Summary')

print('Saving as a whole..')
model.save('inceptionv3.h5')
print('DONE')
