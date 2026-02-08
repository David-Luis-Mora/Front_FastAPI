# Front_FastAPI

Interfaz frontend desarrollada con **Gradio** para consumir un modelo desplegado mediante **FastAPI**.
Permite enviar parámetros (día, mes, municipio y distribuidora eléctrica) y obtener una predicción de consumo energético en kWh.

---

## Instalación

Clonar el repositorio e instalar dependencias:

```bash
git clone <URL_DEL_REPO>
cd Front_FastAPI
pip install -r requirements.txt
```

---

## Ejecución

Ejecutar la aplicación:

```bash
python front.py
```

Se abrirá la interfaz web en tu navegador.

---

## Funcionamiento

La aplicación:

1. Recoge los parámetros desde la interfaz Gradio
2. Construye un `payload` JSON
3. Envía una petición POST a la API:

```
https://api-modelo-fi4h.onrender.com/predict
```

4. Muestra la predicción devuelta (`prediccion_kWh`)

---

## Estructura

```
.
├── front.py
├── requirements.txt
└── README.md
```

---

## Notas

* Asegúrate de que la API esté disponible antes de ejecutar la app
* Si cambian municipios o distribuidoras, actualiza las listas en `front.py`

---

## Dependencias

```
requests
gradio
```
