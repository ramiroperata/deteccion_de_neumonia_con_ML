
# 🩺 Proyecto de detección de neumonía  

Este repositorio contiene el desarrollo completo de un sistema de detección de neumonía basado en imágenes de radiografías de tórax, utilizando una red neuronal convolucional.  
*[Probalo acá](https://huggingface.co/spaces/ramiropm/detector_neumonia)*

## 🛠️ Componentes del Proyecto  
1. **Exploración y transformación de datos**   
   - Procesamiento de datos y preprocesamiento de imágenes.  

2. **Entrenamiento del Modelo**  
   - Entrenamiento de un modelo de clasificación de imágenes utilizando `fastai`.  
   - Optimización y evaluación del modelo en un conjunto de validación.  

3. **Despliegue de la Aplicación**  
   - Aplicación interactiva construida con Streamlit.  
   - Desplegada en [Hugging Face Spaces](https://huggingface.co/spaces).  

## 📂 Estructura del Repositorio  
```
📁 deteccion_de_neumonia_con_ML 
├── 📂 notebook/             # Notebook de análisis y entrenamiento  
├── 📂 app/                  # Código y dependencias de la aplicación  
│   ├── app.py               # Código de la aplicación Streamlit  
│   ├── requirements.txt     # Dependencias de la aplicación  
├── 📂 model/                # Modelo entrenado
├── 📜 README.md             # Este archivo  
└── 📜 LICENSE               # Información sobre la licencia  
```  


## 🧠 Entrenamiento del Modelo  
El modelo fue entrenado con el framework `fastai`, utilizando una arquitectura preentrenada (`ResNet`) como base. Pasos principales:  
1. Preprocesamiento de datos e imágenes.  
2. Fine-tuning del modelo con métricas.  
3. Guardado del modelo final como `pneumonia_detector.pkl`.  

## 🚀 Despliegue de la Aplicación  
La aplicación interactiva se encuentra en la carpeta `app/` y permite a los usuarios cargar imágenes para obtener predicciones en tiempo real.  

Para más detalles sobre la aplicación, consulta el [README de la aplicación](app/README.md).  

## 📊 Resultados  
El modelo alcanzó una f1 score del 98% en el conjunto de prueba. Las métricas clave se documentan en el notebook de evaluación dentro de la carpeta `notebooks/`.  

## 🤝 Contribuciones  
¡Contribuciones y sugerencias son bienvenidas! Por favor, abrí un **issue** o envia un **pull request**.  

## 📜 Licencia  
Este proyecto está bajo la licencia Apache 2.0. Consulta el archivo [LICENSE](LICENSE) para más detalles.  
