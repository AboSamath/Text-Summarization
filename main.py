import streamlit as st
from PIL import Image
import base64


from util import summarizer_lexrank, summarizer_textrank, summarizer_lsa, summarizer_nltk, background, french_summarizer_nltk, french_summarizer_lsa, french_summarizer_lexrank, french_summarizer_textrank



background('./back.jpg')


st.title("Summarization Application")

st.markdown("This application is designed to help you get a fast, reliable summary of your text in English or French.")

st.header('Please choose your text language !')


# Ajoutez des composants Streamlit pour interagir avec l'utilisateur
col1, col2 = st.columns(2)

# Définir une clé pour le bouton
button_key1 = "mon_bouton1"
button_key2 = "mon_bouton2"


with col1:
    if st.button("English", key=button_key1):
        texte_utilisateur = st.text_area("Kindly input the text you want to summarize:", "")
        if st.button("NLTK MODEL"):
            resultat = summarizer_nltk(texte_utilisateur)
            st.write("Your resume (NLTK):", resultat)
        if st.button("TEXT_RANK MODEL"):
            resultat = summarizer_textrank(texte_utilisateur)
            st.write("Your resume (TextRank):", resultat)

        if st.button("LEX_RANK MODEL"):
            resultat = summarizer_lexrank(texte_utilisateur)
            st.write("Your Resume (LexRank):", resultat)

        if st.button("LSA MODEL"):
            resultat = summarizer_lsa(texte_utilisateur)
            st.write("Your resume (LSA):", resultat)

with col2:
    if st.button("French", key=button_key2):
        texte_utilisateur = st.text_area("Veuillez insérer le texte à résumer svp:", "")
        if st.button("MODELE NLTK"):
            resultat = french_summarizer_nltk(texte_utilisateur)
            st.write("Votre resumé (NLTK):", resultat)
        if st.button("MODELE TEXT_RANK"):
            resultat = french_summarizer_textrank(texte_utilisateur)
            st.write("Votre resumé (TextRank):", resultat)

        if st.button("MODELE LEX_RANK"):
            resultat = french_summarizer_lexrank(texte_utilisateur)
            st.write("Votre resumé (LexRank):", resultat)

        if st.button("MODELE LSA"):
            resultat = french_summarizer_lsa(texte_utilisateur)
            st.write("Votre resumé (LSA):", resultat)

st.markdown(
    f"""
    <style>
        div[data-baseweb="button"] #{button_key1} {{
            width: 500px;  /* Ajustez la largeur selon vos besoins */
            height: 90px;  /* Ajustez la hauteur selon vos besoins */
            font-size: 50px;  /* Ajustez la taille de la police selon vos besoins */
        }}
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    f"""
    <style>
        div[data-baseweb="button"] #{button_key2} {{
            width: 500px;  /* Ajustez la largeur selon vos besoins */
            height: 90px;  /* Ajustez la hauteur selon vos besoins */
            font-size: 50px;  /* Ajustez la taille de la police selon vos besoins */
        }}
    </style>
    """,
    unsafe_allow_html=True
)