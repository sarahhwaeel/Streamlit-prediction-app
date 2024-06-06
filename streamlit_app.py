import streamlit as st
import requests
import io
import tensorflow as tf
import numpy as np
from PIL import Image

# Function to load model from GitHub URL
@st.cache(allow_output_mutation=True)
def load_model():
    model_url = "https://github.com/sarahhwaeel/Streamlit-prediction-app/releases/download/v1.0.0/palmtree_disease_model.h5"
    response = requests.get(model_url)
    model_file = io.BytesIO(response.content)
    model = tf.keras.models.load_model(model_file)
    return model

# Function to preprocess the uploaded image
def preprocess_image(img):
    img = img.resize((256, 256))
    img_array = np.array(img) / 255.0  # Normalize pixel values
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

# Main app
def main():
    st.title("Palm Tree Disease Prediction Application")

    # Load model
    model = load_model()

    # Upload image
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Display uploaded image
        img = Image.open(uploaded_file)
        st.image(img, caption="Uploaded Image", width=300)

        # Preprocess the image
        img_array = preprocess_image(img)

        # Make prediction
        predictions = model.predict(img_array)
        class_labels = ['brown spots', 'healthy', 'white scale']
        predicted_class = class_labels[np.argmax(predictions)]

        # Display prediction
        st.markdown(f"**<h3 style='font-size:24px'>Predicted Class: {predicted_class}</h3>**", unsafe_allow_html=True)

        # Display pesticide suggestion
        if predicted_class == 'brown spots':
            pesticide_info = "Use Fungicidal sprays containing copper."
        elif predicted_class == 'healthy':
            pesticide_info = "No pesticide used."
        elif predicted_class == 'white scale':
            pesticide_info = "Use Chemical insecticides as buprofezin or pyriproxyfen."

        st.markdown(f"**<h3 style='font-size:24px'>Pesticide suggested: {pesticide_info}</h3>**", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
