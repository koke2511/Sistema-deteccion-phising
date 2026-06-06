# Sistema de detección de phishing con Machine Learning

## Descripción del proyecto

Este proyecto consiste en el desarrollo de un sistema de detección de phishing basado en el análisis de URLs y el uso de técnicas de Machine Learning.

El objetivo principal es clasificar automáticamente una URL como legítima o phishing a partir de diferentes características extraídas de su estructura, como la longitud de la URL, el uso de HTTPS, la presencia de palabras sospechosas, el número de subdominios o la aparición de patrones habituales en enlaces maliciosos.


---

## Estructura del proyecto

```text
phishing-detector/
│
├── data/
│   └── urls.csv
│
├── models/
│   └── phishing_model.pkl
│
├── src/
│   ├── features.py
│   ├── predict.py
│   ├── test.py
│   ├── test_features.py
│   └── train_model.py
│
├── requirements.txt
└── README.md
````

---

## Archivos del proyecto

### `urls.csv`

Este archivo contiene el dataset utilizado para entrenar y evaluar el modelo.

Incluye URLs legítimas y URLs de phishing, junto con su etiqueta correspondiente.

Ejemplo de formato:

```csv
url,label,source
https://www.google.com,0,manual
http://secure-login-paypal-update.com,1,manual
```

Donde:

* `url`: URL que será analizada.
* `label`: etiqueta de clasificación.

  * `0`: URL legítima.
  * `1`: URL phishing.
* `source`: fuente de la URL o del dataset.

Este archivo es fundamental porque sirve como base para entrenar el sistema de detección.

---

### `phishing_model.pkl`

Este archivo contiene el modelo de Machine Learning ya entrenado.

Se genera automáticamente al ejecutar el archivo `train_model.py`.

Su función es permitir que el sistema pueda realizar predicciones sin tener que entrenar el modelo cada vez que se quiere analizar una URL.

El archivo se guarda dentro de la carpeta `models/`.

---

### `features.py`

Este archivo contiene las funciones encargadas de extraer características de una URL.

Convierte cada URL en un conjunto de datos numéricos que el modelo puede entender.

Algunas de las características extraídas son:

* Longitud total de la URL.
* Longitud del dominio.
* Número de puntos.
* Número de guiones.
* Número de barras.
* Cantidad de dígitos.
* Uso de HTTPS.
* Presencia de dirección IP.
* Número de subdominios.
* Presencia de palabras sospechosas.

Este archivo es una de las partes más importantes del proyecto, ya que el modelo no trabaja directamente con el texto de la URL, sino con las características extraídas.

---

### `train_model.py`

Este archivo se utiliza para entrenar el modelo de Machine Learning.

Sus principales funciones son:

* Cargar el dataset `urls.csv`.
* Extraer características de todas las URLs mediante `features.py`.
* Dividir los datos en entrenamiento y prueba.
* Entrenar diferentes modelos de clasificación.
* Comparar los resultados obtenidos.
* Seleccionar el mejor modelo.
* Guardar el modelo entrenado en `models/phishing_model.pkl`.

En este proyecto se han utilizado modelos como:

* Logistic Regression.
* Random Forest.

El modelo con mejores resultados se guarda para ser utilizado posteriormente por el sistema de predicción.

---

### `predict.py`

Este archivo permite analizar manualmente una URL introducida por el usuario.

Su funcionamiento es el siguiente:

* Carga el modelo entrenado desde `models/phishing_model.pkl`.
* Solicita al usuario una URL.
* Extrae sus características mediante `features.py`.
* Clasifica la URL como legítima o phishing.
* Muestra las probabilidades de cada clase.
* Proporciona una explicación básica de los indicadores sospechosos detectados.

Este archivo representa la parte práctica del sistema, ya que permite utilizar el modelo entrenado para analizar nuevas URLs.

---

### `test.py`

Este archivo se utilizó como prueba inicial del entorno de desarrollo.

Su objetivo fue comprobar que Python, el entorno virtual y las librerías principales estaban correctamente instaladas.

No forma parte del funcionamiento principal del sistema, pero sirvió para validar que el proyecto estaba preparado correctamente antes de empezar el desarrollo.

---

### `test_features.py`

Este archivo se utiliza para comprobar que la extracción de características funciona correctamente.

Permite analizar una URL de prueba y mostrar por pantalla todas las características generadas.

Es útil para validar que el archivo `features.py` está funcionando correctamente antes de entrenar el modelo.

---

## Tecnologías utilizadas

* Python
* pandas
* scikit-learn
* tldextract
* joblib
* Visual Studio Code
* GitHub

---

## Instalación

### 1. Clonar el repositorio

```bash
git clone URL_DEL_REPOSITORIO
```

### 2. Entrar en la carpeta del proyecto

```bash
cd phishing-detector
```

### 3. Crear un entorno virtual

```bash
python -m venv .venv
```

### 4. Activar el entorno virtual en Windows

```bash
.venv\Scripts\activate
```

### 5. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## Uso del proyecto

### 1. Entrenar el modelo

Para entrenar el modelo con el dataset disponible:

```bash
python src/train_model.py
```

Al finalizar, se generará el archivo:

```text
models/phishing_model.pkl
```

---

### 2. Analizar una URL

Para analizar manualmente una URL:

```bash
python src/predict.py
```

Después, el programa solicitará introducir una URL.

Ejemplo:

```text
Introduce una URL para analizar: http://secure-login-paypal-update.com
```

Salida esperada:

```text
Predicción: Phishing
Probabilidad legítima: 0.0000
Probabilidad phishing: 1.0000
```

---

## Resultados

Durante las pruebas realizadas, el sistema fue capaz de clasificar URLs legítimas y phishing utilizando características estructurales de cada enlace.

Además, se compararon diferentes modelos de clasificación y se seleccionó el modelo con mejores métricas para realizar las predicciones finales.

Las métricas utilizadas fueron:

* Accuracy
* Precision
* Recall
* F1-score

---

## Relación con ciberseguridad

Este proyecto simula una tarea habitual dentro de un entorno SOC/MDR, donde los analistas deben revisar URLs sospechosas y determinar si pueden estar asociadas a campañas de phishing.

El sistema permite automatizar parte de este proceso y sirve como una herramienta de apoyo para el análisis inicial de enlaces sospechosos.

---

## Líneas futuras

Algunas posibles mejoras futuras son:

* Ampliar el dataset utilizado.
* Añadir más características a la extracción de URLs.
* Integrar APIs externas como VirusTotal o AbuseIPDB.
* Crear una interfaz web.
* Añadir análisis dinámico de páginas web.
* Integrar el sistema en un flujo de trabajo tipo SOC/SOAR.

---

## Autor

Jorge Ferrero de Lara

Proyecto desarrollado como parte de la memoria de prácticas en el ámbito de ciberseguridad y MDR.

```
```
