import streamlit as st
from fastai.vision.all import *
import torch
from PIL import Image

# Configuración de la app
st.set_page_config(page_title="Detección de neumonía", page_icon="🩺", layout="centered")

st.title("🩺 Detección de neumonía")
st.write("Subí una radiografía de tórax y el modelo determinará si hay signos de neumonía.")

# Cargar modelo entrenado
@st.cache_resource
def load_model():
    path_model = "pneumonia_detector.pkl"
    learn = load_learner(path_model, cpu=torch.device('cpu'))
    return learn

model = load_model()

# Cargar imagen del usuario
uploaded_file = st.file_uploader("Subí una imagen", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Mostrar predicción y resultados en columnas
    col1, col2 = st.columns([1, 1])

    with col1:
        image = Image.open(uploaded_file).convert("RGB")  # Convertir a RGB
        st.image(image, caption="Imagen cargada", use_container_width=True)

    with col2:
        st.write("Procesando la imagen...")
        prediction = model.predict(image)
        label, _, probs = prediction
        if label == 'NORMAL':
            label = 'No tiene neumonía'
        else:
            label = 'Tiene neumonía'
        st.success(f"Predicción: {label}")
        st.write(f"Confianza: {probs.max().item() * 100:.2f}%")