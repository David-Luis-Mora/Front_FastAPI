import gradio as gr
import requests

URL = "https://api-modelo-fi4h.onrender.com/predict"

municipios = [
    'TANQUE, EL', 'SANTA CRUZ DE TENERIFE', 'BUENAVISTA DEL NORTE',
    'SANTA ÚRSULA', 'GUÍA DE ISORA', 'OROTAVA, LA', 'REALEJOS, LOS',
    'GUANCHA, LA', 'GÜÍMAR', 'ROSARIO, EL',
    'SAN CRISTÓBAL DE LA LAGUNA', 'SILOS, LOS', 'TACORONTE',
    'VICTORIA DE ACENTEJO, LA', 'ADEJE', 'ICOD DE LOS VINOS', 'ARONA',
    'MATANZA DE ACENTEJO, LA', 'GARACHICO', 'CANDELARIA', 'ARAFO',
    'GRANADILLA DE ABONA', 'ARICO', 'FASNIA', 'SANTIAGO DEL TEIDE',
    'SAUZAL, EL', 'TEGUESTE', 'VILAFLOR DE CHASNA',
    'PUERTO DE LA CRUZ'
]

distribuidoras = [
    'EDISTRIBUCIÓN',
    'DISTRIBUIDORA ELÉCTRICA DEL PUERTO DE LA CRUZ, S.A.'
]

def consumir_api(dia, mes, municipio, distribuidora):
    payload = {
        "dia": dia,
        "mes": mes,
        "cups_municipio": municipio,
        "cups_distribuidor": distribuidora
    }
    r = requests.post(URL, json=payload)

    if r.status_code != 200:
        return f"Error de la API: {r.text}"

    return r.json()["prediccion_kWh"]

iface = gr.Interface(
    fn=consumir_api,
    inputs=[
        gr.Number(label="Día"),
        gr.Number(label="Mes"),
        gr.Dropdown(choices=municipios, label="Municipio"),
        gr.Dropdown(choices=distribuidoras, label="Distribuidora")
    ],
    outputs=gr.Text(label="Predicción kWh")
)

iface.launch()