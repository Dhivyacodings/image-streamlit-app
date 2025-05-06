import streamlit as st
import cv2
import numpy as np
from PIL import Image

st.title("??? Image Processing with OpenCV")

uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Original Image", use_column_width=True)

    # Convert PIL to OpenCV format
    image_np = np.array(image)
    image_cv = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)

    # Convert to grayscale
    gray = cv2.cvtColor(image_cv, cv2.COLOR_BGR2GRAY)
    st.image(gray, caption="Grayscale", use_column_width=True, channels="GRAY")

    # Apply Gaussian blur
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    st.image(blurred, caption="Blurred", use_column_width=True, channels="GRAY")

    # Detect edges using Canny
    edges = cv2.Canny(blurred, 50, 150)
    st.image(edges, caption="Edge Detection", use_column_width=True, channels="GRAY")
