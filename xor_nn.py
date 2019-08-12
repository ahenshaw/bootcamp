import numpy as np
from keras.models import Sequential
from keras.layers.core import Dense
import tensorflow as tf

tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)

#                 A  B -> A^B
data = np.array([[0, 0,   0],
                 [0, 1,   1],
                 [1, 0,   1],
                 [1, 1,   0]
                ], "float32")

training = data[:,0:2]
target   = data[:,2]

model = Sequential()
model.add(Dense(16, input_dim=2, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='mean_squared_error',
              optimizer='adam',
              metrics=['binary_accuracy'])

model.fit(training, target, epochs=500, verbose=0)

print(model.predict(training).round())