# 🩺 Detección de neumonía con inteligencia artificial  

Este proyecto utiliza un modelo de aprendizaje profundo para clasificar radiografías de tórax y determinar si muestran signos de neumonía. La aplicación está implementada con **Streamlit** y puede desplegarse fácilmente en **Hugging Face Spaces**.  

## 🚀 Características  
- Clasificación automática de imágenes médicas (con o sin neumonía).  
- Interfaz simple e intuitiva.  
- Procesamiento en tiempo real utilizando un modelo optimizado de `fastai`.  

## 🛠️ Tecnologías utilizadas  
- **Python**  
- **Streamlit**  
- **Fastai**  
- **Torch**  
- **Pillow**  

## 📦 Instalación local  
1. Clona este repositorio:  
   ```bash
   git clone https://github.com/ramiroperata/deteccion_de_neumonia_con_ML
   cd deteccion_de_neumonia_con_ML
   ```  

2. Instala las dependencias:  
   ```bash
   pip install -r requirements.txt
   ```  

3. Ejecuta la aplicación:  
   ```bash
   streamlit run app.py
   ```  

## 🌐 Despliegue en Hugging Face Spaces  
1. Sube los archivos del repositorio a un nuevo espacio en [Hugging Face Spaces](https://huggingface.co/spaces).  
2. Asegurate de incluir el modelo entrenado (`pneumonia_detector.pkl`) en la raíz del espacio.  
3. ¡Listo! La aplicación estará disponible en línea.  

## 🖼️ Ejemplo de uso  
1. Subí una radiografía de tórax (formato JPG/PNG).  
2. Visualiza la predicción junto a la imagen cargada.  
3. Confianza en el resultado mostrada en porcentaje.  

## 🧠 Modelo entrenado  
El modelo fue entrenado utilizando el framework `fastai` con datos de radiografías de tórax. Asegúrate de incluir el archivo `pneumonia_detector.pkl` en la raíz del proyecto para que la aplicación funcione correctamente.  

## 🤝 Contribuciones  
¡Contribuciones, reportes de errores y sugerencias son bienvenidos! Por favor, abre un **issue** o envía un **pull request**.  

## 📜 Licencia  
Este proyecto está bajo la licencia Apache 2.0. Consulta el archivo [LICENSE](LICENSE) para más detalles.  
