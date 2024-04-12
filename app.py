import streamlit as st
import pandas as pd
import tensorflow as tf
import numpy as np
import cv2
from PIL import Image

# Set page title
st.title("Fruits Classification")
st.write("Please upload an image in jpeg format to test the fruit detection model.")

# Upload image
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg"])

# Load Model
model = tf.keras.models.load_model('/content/FruitDetectorCNN.h5')

# Preprocess the input image
def preprocess_image(image_path):
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert to RGB format
    image = cv2.resize(image, (224, 224))  # Resize to match model input shape
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    return image

# Pass the preprocessed image through the model to obtain predictions
def predict_objects(image):
    localization_head, classification_head = model.predict(image)
    return localization_head, classification_head

# Parse prediction results
def parse_detections(localization_head, classification_head, confidence_threshold=0.5):
    xmin, ymin, xmax, ymax = localization_head[0]
    class_probabilities = classification_head[0]
    return xmin, ymin, xmax, ymax, class_probabilities

if uploaded_file is not None:
  # Display uploaded image
  image = Image.open(uploaded_file)
  st.image(image, caption="Uploaded Image", use_column_width=True)
  st.success("Model is running.")

  # Load and preprocess the input image
  image_pre = preprocess_image(image)
  localization_head, classification_head = predict_objects(image_pre)
  xmin, ymin, xmax, ymax, classes = parse_detections(localization_head, classification_head)
  LabelDict = {0:"Apple", 1:"Banana", 2:"Orange"}
  label = np.argmax(classes)
  class_name = LabelDict.get(label)

  #Diplay results
  st.markdown("**Fruit is**", class_name)
