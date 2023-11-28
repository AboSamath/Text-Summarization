import streamlit as st
from PIL import Image
import base64


from util import summarizer_lexrank, summarizer_textrank, summarizer_lsa

def set_background(image_file):
    with open(image_file, "bg") as f:
        img_data = f.read()

    b64_encoded = base64.b64encode(img_data).decode()
    style = f"""
        <style>
        .stApp {{
            background-image: url(data:./jpg;base64,{b64_encoded});
            background-size: cover;
        }}
        </style>
    """
    st.markdown(style, unsafe_allow_html=True)


st.title("Application de Summarization")

# Ajoutez des composants Streamlit pour interagir avec l'utilisateur
texte_utilisateur = st.text_area("Entrez le texte à résumer", "")


if st.button("Résumer Modèle TextRankSummarizer"):
    resultat = summarizer_textrank(texte_utilisateur)
    st.write("Résumé (TextRankSummarizer):", resultat)

if st.button("Résumer Modèle LexRankSummarizer"):
    resultat = summarizer_lexrank(texte_utilisateur)
    st.write("Résumé (LexRankSummarizer):", resultat)

if st.button("Résumer Modèle LsaSummarizer"):
    resultat = summarizer_lsa(texte_utilisateur)
    st.write("Résumé (LsaSummarizer):", resultat)
