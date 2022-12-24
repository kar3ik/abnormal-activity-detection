from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.preprocessing.image import ImageDataGenerator

def build():
    # Initialize the CNN
    classifier = Sequential()
    # Convolution and Max pooling
    classifier.add(Conv2D(32, (3, 3), input_shape=(128, 128, 3), activation='relu'))
    classifier.add(MaxPooling2D(pool_size=(2, 2)))
    classifier.add(Conv2D(64, (3, 3), activation='relu'))
    classifier.add(MaxPooling2D(pool_size=(2, 2)))
    classifier.add(Conv2D(128, (3, 3), activation='relu'))
    classifier.add(MaxPooling2D(pool_size=(2, 2)))
    # Flatten
    classifier.add(Flatten())

    # Full connection
    classifier.add(Dense(128, activation='relu'))
    classifier.add(Dense(2, activation='softmax'))

    # Compile classifier
    classifier.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    # Fitting CNN to the images
    train_datagen = ImageDataGenerator(rescale=1. / 255, shear_range=0.2, zoom_range=0.2, horizontal_flip=True)
    test_datagen = ImageDataGenerator(rescale=1. / 255)
    training_set = train_datagen.flow_from_directory('./dataset/train', target_size=(128, 128), batch_size=32,
                                                     class_mode='categorical')
    test_set = test_datagen.flow_from_directory('./dataset/test', target_size=(128, 128), batch_size=32,
                                                class_mode='categorical')
    classifier.fit_generator(training_set, steps_per_epoch=25, epochs=50, validation_data=test_set,
                             validation_steps=200 / 32)

    # save model    
    classifier.save('cnn.h5')
    classifier.save_weights('weights_cnn.h5')
#build()

