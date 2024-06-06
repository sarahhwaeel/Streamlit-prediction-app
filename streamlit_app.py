import streamlit as st
import numpy as np
from PIL import Image
import tensorflow as tf
import requests
from io import BytesIO

# Function to download the model file from the URL
def download_model(model_url):
    response = requests.get(model_url)
    response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
    return BytesIO(response.content)

# Load the trained model
@st.cache(allow_output_mutation=True)
def load_model():
    model_url = "https://drive.google.com/uc?id=183hiluvIbiUNEJh8aZR3yL1DKT1KCT3l"
    model_file = download_model(model_url)
    return tf.keras.models.load_model(model_file)

# Preprocess the uploaded image
def preprocess_image(img):
    img = img.resize((256, 256))
    img_array = np.array(img) / 255.0  # Normalize pixel values
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

# Main app
def main():
    st.title("Palm Tree Disease Prediction Application")

    # Upload image
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Display uploaded image
        img = Image.open(uploaded_file)
        st.image(img, caption="Uploaded Image", width=300)

        # Preprocess the image
        img_array = preprocess_image(img)

        # Load model and make prediction
        model = load_model()
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
