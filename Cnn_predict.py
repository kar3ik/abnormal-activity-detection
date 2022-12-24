import cv2
import numpy as np
import operator
from keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
from keras.models import Sequential, load_model
from keras.preprocessing import image

def predict(img):
    # load model
    img_width, img_height = 128, 128
    model_path = 'cnn.h5'
    model_weights_path = 'weights_cnn.h5'
    model = load_model(model_path)
    model.load_weights(model_weights_path)

    # Prediction on a new picture
    from keras.preprocessing import image as image_utils

    from PIL import Image, ImageTk

    class_labels = ['Abnormal', 'Normal']
    test_image = image.load_img(img, target_size=(128, 128))
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis=0)

    test_image /= 255
    result = model.predict(test_image)

    decoded_predictions = dict(zip(class_labels, result[0]))
    decoded_predictions = sorted(decoded_predictions.items(), key=operator.itemgetter(1), reverse=True)
    print(decoded_predictions[0][0])

    count = 1
    for key, value in decoded_predictions[:5]:
        print("{}. {}: {:8f}%".format(count, key, value * 100))
        count += 1
    frame = cv2.imread(img)
    cv2.putText(frame, decoded_predictions[0][0], (10, 30),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    cv2.imshow("Output", frame)
    return decoded_predictions[0][0]
