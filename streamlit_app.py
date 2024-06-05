

import streamlit as st
import numpy as np
from PIL import Image


# Load the trained model
@st.cache(allow_output_mutation=True)
def load_model():
    model_path = "/content/drive/My Drive/Data/Dataset/Date Palm data/palmtree_disease_model.h5"
    return tf.keras.models.load_model(model_path)

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

if __name__ == "__main__":
    main()
