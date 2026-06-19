import streamlit as st

if "logged_in" not in st.session_state:
    st.warning("Please Login First")
    st.stop()

if not st.session_state.logged_in:
    st.warning("Please Login First")
    st.stop()
import pandas as pd
from datetime import datetime
import os
import streamlit as st
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model

model = load_model("deepfake_model.h5")

st.title("🔍 Deepfake Detection")

uploaded_file = st.file_uploader(
    "📂 Drag & Drop or Upload Image",
    type=["jpg", "jpeg", "png"]
)

camera_image = st.camera_input("📷 Take a Picture")

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    image_name = uploaded_file.name

elif camera_image is not None:
    image = Image.open(camera_image)
    image_name = "Camera_Image.jpg"

else:
    image = None

if image is not None:

    st.image(image, caption="Selected Image")

    img = image.resize((128, 128))
    img = np.array(img) / 255.0
    img = np.expand_dims(img, axis=0)

    prediction = model.predict(img)
    score = float(prediction[0][0])

    if score > 0.5:
        result = "Fake"
        st.error(f"🚨 Fake Image ({score*100:.2f}% confidence)")
    else:
        result = "Real"
        st.success(f"✅ Real Image ({(1-score)*100:.2f}% confidence)")

    st.write("Prediction Score:", round(score, 4))

    data = {
    "Username": [st.session_state.username],
    "Date": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
    "Image": [image_name],
    "Score": [round(score, 4)],
    "Result": ["Fake" if score > 0.5 else "Real"]
}

    df = pd.DataFrame(data)

    if os.path.exists("history.csv"):
        df.to_csv("history.csv", mode="a", header=False, index=False)
    else:
        df.to_csv("history.csv", index=False)

    st.success("Result Saved Successfully ✅")