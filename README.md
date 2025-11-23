# Proyecto final - Machine learning

![Repo Size](https://img.shields.io/github/repo-size/sophie-muriel/ProyectoFinal-Muriel-Vitonco?style=for-the-badge)
![Last Commit](https://img.shields.io/github/last-commit/sophie-muriel/ProyectoFinal-Muriel-Vitonco?style=for-the-badge)
![Contributors](https://img.shields.io/github/contributors/sophie-muriel/ProyectoFinal-Muriel-Vitonco?style=for-the-badge)

---

> **Nota:**  
> El archivo del modelo entrenado (`insurance_renewal_model.pkl`) y el scaler (`scaler.pkl`) no se incluye en este repositorio debido a su tamaño. Ambos se **generan automáticamente** al ejecutar el notebook, específicamente en la **Sección 10**, donde se entrena al modelo y se guarda localmente junto con el scaler.

---

Este repositorio contiene el desarrollo completo del dataset **insurance_company.csv**, cuyo objetivo es analizar, procesar y modelar la información de una aseguradora para predecir la probabilidad de renovación de pólizas. El proyecto incluye el caso de negocio, el análisis exploratorio (EDA), el preprocesamiento, la construcción de modelos de Machine Learning, la selección de modelo final, las conclusiones orientadas a la toma de decisiones comerciales y una aplicación web en Flask para predecir si un cliente renovará o no, siendo esta la pregunta rectora y el objetivo final del análisis.

---

## Descripción general del proyecto

Este proyecto analiza el comportamiento de renovación de pólizas de una compañía de seguros con el objetivo de predecir qué clientes tienen mayor o menor probabilidad de renovar. El trabajo incluye:

- **Caso de negocio**: Identificación del problema de retención de clientes y su impacto financiero.
- **Análisis Exploratorio de Datos (EDA)**: Evaluación del comportamiento de las variables categóricas y numéricas, detección de patrones, outliers y desbalances.
- **Preprocesamiento de datos**: Limpieza, transformación, codificación de variables y manejo del desbalance de la variable objetivo.
- **Modelado Predictivo**: Implementación y comparación de modelos de Machine Learning para clasificar la probabilidad de renovación.
- **Interpretación de resultados**: Análisis de métricas, importancia de variables y hallazgos clave.
- **Recomendaciones estratégicas**: Acciones sugeridas para mejorar la retención y optimizar los esfuerzos comerciales.
- **App web en Flask:** Interfaz gráfica (web) que utiliza el modelo final para predecir si un cliente renovará su póliza.

El objetivo final es proporcionar una herramienta analítica que permita a la empresa anticipar la no renovación y tomar decisiones informadas basadas en datos.

---

## Estructura del repositorio

```
PROYECTOFINAL-MURIEL-VITONCO/
│
├── data/
│   ├── crosstabs/
│   │   ├── proporciones_residence_area_type_renewal.csv
│   │   └── proporciones_sourcing_channel_renewal.csv
│   ├── grouped_describe_by_renewal_cat.csv
│   ├── grouped_describe_by_renewal_num.csv
│   ├── insurance_company.csv
│   └── insurance_company_final.csv
│
├── images/
│   ├── bivariable/
│   ├── models/
│   ├── univariable/
│   ├── corr_matrix_filtered.png
│   ├── corr_matrix.png
│   ├── renewal_dist.png
│   ├── renewal_smote_dist.png
│   ├── ridge_plot.png
│   └── ridge_residuals.png
│
├── static/
│   └── css/
│       └── styles.css
│
├── templates/
│   └── index.html
|
├── app.py
├── notebook.ipynb
├── reporte_eda_profiling.html
├── requirements.txt
├── .python-version
├── .gitignore
└── README.md
```

### `data/` Directorio

Contiene los datos utilizados en el proyecto, tanto los archivos originales como los datos procesados.

- `insurance_company.csv`: database original
- `insurance_company_final.csv`: dataset limpio y transformado para modelado.
- `grouped_describe_by_renewal_cat.csv`: estadísticas descriptivas agrupadas para variables categóricas según la renovación.
- `grouped_describe_by_renewal_num.csv`: estadísticas descriptivas agrupadas para variables
- `crosstabs/`: tablas descriptivas calculadas durante el EDA:
    - `proporciones_residence_area_type_renewal.csv`
    - `proporciones_sourcing_channel_renewal.csv`

---

### `images/` Directorio

Incluye todas las visualizaciones generadas en el análisis:

- `univariable/`: gráficos univariantes (distribuciones, histogramas, boxplots).
- `bivariable/`: relaciones bivariantes (violinplots, stacked bars, boxplots).
- `models/`: gráficos generados durante el entrenamiento y evaluación de modelos.

Además, en la raíz del directorio se incluyen varios archivos PNG individuales:
- `corr_matrix.png`: matriz de correlación completa.
- `corr_matrix_filtered.png`: matriz de correlación filtrada por umbral.
- `renewal_dist.png`: distribución de la variable objetivo (renovación).
- `renewal_smote_dist.png`: distribución posterior a SMOTE.
- `ridge_plot.png`: visualización principal del modelo Ridge.
- `ridge_residuals.png`: análisis de residuos del modelo Ridge.

---

### `notebook.ipynb`

Notebook principal con el EDA, preprocesamiento, modelado y evaluación.

### `app.py`

Despliegue simple del modelo.

### `reporte_eda_profiling.html`

Reporte generado automáticamente con _ydata-profiling_.

### `requirements.txt`

Lista de todas las dependencias necesarias para ejecutar el proyecto.

### `.python-version`

Versión de Python utilizada para asegurar compatibilidad en el entorno.

### `README.md`

Documento principal que describe el proyecto.

## Pre-requisitos

Para ejecutar este proyecto necesitas tener instalado:

- **Python 3.9+**
- **pip** (gestor de paquetes)
- **Virtual environment** (opcional pero recomendado)
- **Jupyter Notebook o JupyterLab**
- Navegador web para visualizar el archivo `reporte_eda_profiling.html`

Además, se requiere instalar las dependencias indicadas en `requirements.txt`, incluyendo:

- pandas
- numpy
- matplotlib
- seaborn
- ydata-profiling
- scipy
- imbalanced-learn
- scikit-learn
- flask
- ipykernel
- ipywidgets

Estas se instalan automáticamente usando:

```bash
pip install -r requirements.txt
```

## Cómo ejecutar el proyecto

### 1. Clonar el repositorio

```bash
git clone https://github.com/sophie-muriel/ProyectoFinal-Muriel-Vitonco.git
cd ProyectoFinal-Muriel-Vitonco
```

### 2. Crear entorno virtual (opcional)

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Ejecutar el notebook

```bash
jupyter notebook
```

Abrir: `notebook.ipynb`
Ejecutar todas las celdas para:

- Cargar datos
- Realizar el EDA
- Preprocesar
- Entrenar modelos
- Evaluar resultados
- Guardar modelo y scaler

### 5. Ejecutar la app Flask

```bash
python app.py
```

---

## Resultados principales del modelo

El modelo final desarrollado para predecir la **probabilidad de renovación de pólizas** se construyó después del EDA, balanceo de clases, escalado y comparación de múltiples algoritmos.

### Desempeño general

- El modelo seleccionado ofrece alta capacidad para distinguir clientes que renuevan vs. no renuevan, incluso con un dataset fuertemente desbalanceado (~6.3% no renuevan).
- Se priorizaron métricas enfocadas en la clase minoritaria, evitando depender únicamente de la accuracy.

### Métricas destacadas

- **Recall (para no renovación)**: Alto, permitiendo identificar una mayor proporción de clientes con riesgo real de no renovar.
- **Precision (para no renovación)**: Adecuada pese al desbalance, reduciendo falsos positivos.
- **F1-score**: Muestra un balance sólido entre recall y precision en la clase minoritaria.
- **ROC-AUC**: Indica buena separación entre ambas clases.

*(Nota: los valores exactos de las métricas se pueden consultar en la sección de modelado del notebook.)*

### Variables más influyentes

El análisis del modelo resalta que los factores más relevantes para predecir la no renovación son:

1. **`perc_premium_paid_by_cash_credit`**: Los clientes que pagan mayor parte de la prima con efectivo/crédito tienen mayor riesgo de no renovar.
2. **Historial de atrasos**: `count_3-6_months_late`, `count_6-12_months_late`, `count_more_than_12_months_late` son señales muy fuertes de riesgo.
3. **`premium`**: Primas más altas se relacionan con una mayor probabilidad de renovación.
4. **`application_underwriting_score`**: Aunque con baja variabilidad, pequeñas diferencias son significativas.
5. **`sourcing_channel`**: Ciertos canales presentan tasas de renovación más bajas, clave para ajustar estrategias comerciales.

### Conclusión

El modelo permite identificar perfiles de clientes con riesgo de no renovar para:

- Aplicar campañas preventivas más eficientes.
- Optimizar incentivos por canal comercial.
- Priorizar clientes donde una intervención temprana puede evitar la pérdida de ingresos.

Este resultado (detallado más en el notebook) se integra en la aplicación Flask incluida en el proyecto, permitiendo realizar predicciones de manera simple y accesible desde una interfaz web.

---

## Contribuyentes

- **Sophie Muriel** – [GitHub](https://github.com/sophie-muriel)
- **Karol Vitonco** – [GitHub](https://github.com/KrlVanessa)

---
