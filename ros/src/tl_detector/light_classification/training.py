from keras.models import Sequential
from keras.layers.core import Flatten, Dense, Lambda, Dropout, Activation
from keras.layers.convolutional import Conv2D, Cropping2D
from keras.layers.pooling import MaxPooling2D

#TODO implement LeNet and train on data collected from the simulator

model = Sequential()
# Update Conv layer sizes
model.add(Conv2D(32, 5, 5, border_mode="same", input_shape=(depth,height,width)))
model.add(Activation('relu'))
# Update pooling layer sizes
model.add(MaxPooling2D(pool_size=(2,2), strides=(2,2)))
model.add(Conv2D(32, 5, 5, border_mode="same", input_shape=(depth,height,width)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2,2),strides=(2,2)))
# Update FC layer sizes
model.add(Dense(32,input_dim=8))
model.add(Activation('relu'))
model.add(Dense(32,input_dim=1))
