import tensorflow as tf
from tensorflow.keras.applications import VGG16, DenseNet201
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Dropout, GlobalAveragePooling2D
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
import os
train_dir = 'path/to/your/train_data' 
val_dir = 'path/to/your/validation_data'  
train_datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest'
)
val_datagen = ImageDataGenerator(rescale=1./255)
train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=(224, 224),  
    batch_size=32,
    class_mode='binary'  
)
val_generator = val_datagen.flow_from_directory(
    val_dir,
    target_size=(224, 224),
    batch_size=32,
    class_mode='binary'
)
def build_model(base_model):
    model = Sequential()
    model.add(base_model)
    model.add(GlobalAveragePooling2D())
    model.add(Dense(512, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(1, activation='sigmoid'))  # Binary classification
    return model

# Load VGG16 and DenseNet201 with pretrained weights
vgg16_base = VGG16(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
densenet_base = DenseNet201(weights='imagenet', include_top=False, input_shape=(224, 224, 3))

# Freeze the base models to prevent them from being trained
vgg16_base.trainable = False
densenet_base.trainable = False

# Build the models
vgg16_model = build_model(vgg16_base)
densenet_model = build_model(densenet_base)

# Compile the models
vgg16_model.compile(optimizer=Adam(lr=0.0001), loss='binary_crossentropy', metrics=['accuracy'])
densenet_model.compile(optimizer=Adam(lr=0.0001), loss='binary_crossentropy', metrics=['accuracy'])

# Callbacks for early stopping and saving the best model
callbacks = [
    EarlyStopping(patience=5, monitor='val_loss', restore_best_weights=True),
    ModelCheckpoint('best_vgg16_model.h5', save_best_only=True, monitor='val_loss')
]

# Train the VGG16 model
history_vgg16 = vgg16_model.fit(
    train_generator,
    epochs=20,
    validation_data=val_generator,
    callbacks=callbacks
)

# Save the VGG16 model
vgg16_model.save('vgg16_breast_cancer.h5')

# Update the checkpoint file name for DenseNet201
callbacks[1] = ModelCheckpoint('best_densenet_model.h5', save_best_only=True, monitor='val_loss')

# Train the DenseNet201 model
history_densenet = densenet_model.fit(
    train_generator,
    epochs=20,
    validation_data=val_generator,
    callbacks=callbacks
)

# Save the DenseNet201 model
densenet_model.save('densenet201_breast_cancer.h5')

# Evaluate the models on the validation set
vgg16_val_loss, vgg16_val_acc = vgg16_model.evaluate(val_generator)
print(f"VGG16 Validation Accuracy: {vgg16_val_acc * 100:.2f}%")

densenet_val_loss, densenet_val_acc = densenet_model.evaluate(val_generator)
print(f"DenseNet201 Validation Accuracy: {densenet_val_acc * 100:.2f}%")
