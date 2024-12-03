
# 🩺 Proyecto de Detección de Neumonía  

Este repositorio contiene el desarrollo completo de un sistema de detección de neumonía basado en imágenes de radiografías de tórax, utilizando técnicas de ciencia de datos e inteligencia artificial.  

## 🛠️ Componentes del Proyecto  
1. **Exploración y Análisis de Datos**  
   - Análisis descriptivo de las imágenes médicas.  
   - Procesamiento de datos y preprocesamiento de imágenes.  

2. **Entrenamiento del Modelo**  
   - Entrenamiento de un modelo de clasificación de imágenes utilizando `fastai`.  
   - Optimización y evaluación del modelo en un conjunto de validación.  

3. **Despliegue de la Aplicación**  
   - Aplicación interactiva construida con Streamlit.  
   - Desplegada en [Hugging Face Spaces](https://huggingface.co/spaces).  

## 📂 Estructura del Repositorio  
```
📁 raiz-del-repositorio  
├── 📂 data/                 # Datos originales y preprocesados  
├── 📂 notebooks/            # Notebooks de análisis y entrenamiento  
├── 📂 app/                  # Código y dependencias de la aplicación  
│   ├── app.py               # Código de la aplicación Streamlit  
│   ├── requirements.txt     # Dependencias de la aplicación  
├── 📂 models/               # Modelos entrenados  
├── 📜 README.md             # Este archivo  
└── 📜 LICENSE               # Información sobre la licencia  
```  

## 🔍 Exploración y Análisis de Datos  
Los datos utilizados en este proyecto provienen de un conjunto de imágenes médicas. En la carpeta `notebooks/` encontrarás:  
- Exploración inicial de los datos.  
- Visualización de imágenes y distribución de clases.  
- Técnicas de aumento de datos para mejorar la generalización del modelo.  

## 🧠 Entrenamiento del Modelo  
El modelo fue entrenado con el framework `fastai`, utilizando una arquitectura preentrenada (`ResNet`) como base. Pasos principales:  
1. Preprocesamiento de datos e imágenes.  
2. Fine-tuning del modelo con métricas de precisión y recall.  
3. Guardado del modelo final como `model.pth`.  

## 🚀 Despliegue de la Aplicación  
La aplicación interactiva se encuentra en la carpeta `app/` y permite a los usuarios cargar imágenes para obtener predicciones en tiempo real.  

Para más detalles sobre la aplicación, consulta el [README de la aplicación](app/README.md).  

## 📊 Resultados  
El modelo alcanzó una precisión del XX% en el conjunto de prueba. Las métricas clave se documentan en el notebook de evaluación dentro de la carpeta `notebooks/`.  

## 🤝 Contribuciones  
¡Contribuciones y sugerencias son bienvenidas! Por favor, abre un **issue** o envía un **pull request**.  

## 📜 Licencia  
Este proyecto está bajo la licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.  
