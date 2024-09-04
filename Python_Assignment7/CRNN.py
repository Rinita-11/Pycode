import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.layers import TimeDistributed, LSTM, GRU
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import numpy as np
import os
train_dir = 'path/to/your/train_data'  
val_dir = 'path/to/your/validation_data'  
train_datagen = ImageDataGenerator(
    rescale=1.0/255.0,
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest'
)
val_datagen = ImageDataGenerator(rescale=1.0/255.0)
sequence_length = 10  
input_shape = (sequence_length, 150, 150, 3)  
def sequence_generator(generator, batch_size):
    while True:
        data = generator.next()
        images, labels = data[0], data[1]
        sequences = []
        for i in range(0, len(images) - sequence_length + 1, sequence_length):
            sequences.append(images[i:i + sequence_length])
        sequences = np.array(sequences)
        yield sequences, labels[:len(sequences)]
train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=(150, 150),
    batch_size=sequence_length * 32, 
    class_mode='categorical',
    shuffle=True
)

val_generator = val_datagen.flow_from_directory(
    val_dir,
    target_size=(150, 150),
    batch_size=sequence_length * 32,  # Adjust batch size accordingly
    class_mode='categorical',
    shuffle=False
)

# Define the CRNN model
model = Sequential()

# Convolutional layers
model.add(TimeDistributed(Conv2D(32, (3, 3), activation='relu', padding='same'), input_shape=input_shape))
model.add(TimeDistributed(MaxPooling2D(pool_size=(2, 2))))

model.add(TimeDistributed(Conv2D(64, (3, 3), activation='relu', padding='same')))
model.add(TimeDistributed(MaxPooling2D(pool_size=(2, 2))))

model.add(TimeDistributed(Conv2D(128, (3, 3), activation='relu', padding='same')))
model.add(TimeDistributed(MaxPooling2D(pool_size=(2, 2))))

model.add(TimeDistributed(Flatten()))

# Recurrent layers (using LSTM here)
model.add(LSTM(128, return_sequences=False))

# Fully connected layer
model.add(Dense(512, activation='relu'))
model.add(Dropout(0.5))

# Output layer
model.add(Dense(train_generator.num_classes, activation='softmax'))

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train the model
history = model.fit(
    sequence_generator(train_generator, batch_size=32),
    steps_per_epoch=len(train_generator) // sequence_length,
    epochs=20,
    validation_data=sequence_generator(val_generator, batch_size=32),
    validation_steps=len(val_generator) // sequence_length
)

# Evaluate the model
loss, accuracy = model.evaluate(sequence_generator(val_generator, batch_size=32), steps=len(val_generator) // sequence_length)
print(f"Validation Accuracy: {accuracy * 100:.2f}%")

# Save the model
model.save('gait_recognition_crnn.h5')
