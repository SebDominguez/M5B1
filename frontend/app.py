import os
import requests
import streamlit as st
from loguru import logger

API_URL = os.getenv("API_URL", "http://localhost:8000")

st.title("M5B1 - Carré d'un entier")

value = st.number_input("Entier", step=1, value=0, format="%d")

if st.button("Calculer"):
    logger.info(f"POST /calcul value={value}")
    try:
        r = requests.post(f"{API_URL}/calcul", json={"value": int(value)}, timeout=5)
        r.raise_for_status()
        result = r.json()["result"]
        logger.success(f"result={result}")
        st.success(f"Résultat : {result}")
    except Exception as e:
        logger.error(e)
        st.error(f"Erreur : {e}")
