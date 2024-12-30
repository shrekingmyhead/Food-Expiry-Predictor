import streamlit as st
import numpy as np
import cv2
import tensorflow as tf

# Load the CNN model
model = tf.keras.models.load_model('cnnmodel.h5')

# Define categories for image prediction
categories = ['apples', 'banana', 'orange', 'carrot', 'tomato', 'strawberry', 'potato', 'bellpepper', 'cucumber', 'mango']

# Function to preprocess image for CNN
def preprocess_image(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB
    image = cv2.resize(image, (64, 64))
    image = image / 255.0
    return image

# Function to predict image category and freshness
def predict_image(image):
    image = preprocess_image(image)
    image = np.expand_dims(image, axis=0)
    prediction = model.predict(image)[0]
    predicted_label = np.argmax(prediction)
    predicted_category = categories[predicted_label // 2]
    freshness = "Fresh" if predicted_label % 2 == 0 else "Expired"
    return predicted_category, freshness

# Streamlit App Layout
st.title("Food Expiry Predictor 🍎🥕")

# Option to choose between camera and upload
option = st.radio("Choose an option:", ("Take a Picture", "Upload a Photo"))

if option == "Take a Picture":
    # Camera Input Section
    st.header("Take a Picture for Prediction")
    camera_image = st.camera_input("Take a picture of a fruit or vegetable")

    if camera_image is not None:
        # Read the image from the camera input
        file_bytes = np.asarray(bytearray(camera_image.read()), dtype=np.uint8)
        image = cv2.imdecode(file_bytes, 1)

        # Convert the image from BGR to RGB
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Display the image
        st.image(image_rgb, caption="Captured Image", use_container_width=True)

        # Predict button
        if st.button("Predict"):
            predicted_category, freshness = predict_image(image)
            st.write(f"**Predicted Category:** {predicted_category}")
            st.write(f"**Freshness:** {freshness}")

else:
    # Upload Photo Section
    st.header("Upload a Photo for Prediction")
    uploaded_file = st.file_uploader("Upload an image of a fruit or vegetable", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Read the uploaded image
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        image = cv2.imdecode(file_bytes, 1)

        # Convert the image from BGR to RGB
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Display the image
        st.image(image_rgb, caption="Uploaded Image", use_container_width=True)

        # Predict button
        if st.button("Predict"):
            predicted_category, freshness = predict_image(image)
            st.write(f"**Predicted Category:** {predicted_category}")
            st.write(f"**Freshness:** {freshness}")