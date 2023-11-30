import streamlit as st
from PIL import Image
import base64


from util import summarizer_lexrank, summarizer_textrank, summarizer_lsa, summarizer_nltk, background, french_summarizer_nltk, french_summarizer_lsa, french_summarizer_lexrank, french_summarizer_textrank



background('./back.jpg')


st.markdown('<h1 style="background-color: white; color: #f4672f; border: 8px solid #f4672f; padding: 15px; text-align: center">Summarization Application</h1>', unsafe_allow_html=True)

st.markdown("")

st.markdown("")

st.markdown("This application is designed to help you get a fast, reliable summary of your text in English or French.")

st.markdown('#### Please input your text and choose the prefered Model !')

texte_utilisateur = st.text_area('Kindly input the text you want to summarize:',
                                 style='background-color: white; color: black; border: 2px solid #000; padding: 10px;')

resultat = ""

# Choisir la langue
#selected_language = st.selectbox("Please choose your language", ["English", "French"])

# Ajoutez des composants Streamlit pour interagir avec l'utilisateur
col1, col2 = st.columns(2)

with col1:
    st.markdown("Models for English Text:")
    if st.button("NLTK MODEL"):
        resultat = summarizer_nltk(texte_utilisateur)    


    if st.button("TEXT_RANK MODEL"):
        resultat = summarizer_textrank(texte_utilisateur)

    if st.button("LEX_RANK MODEL"):
        resultat = summarizer_lexrank(texte_utilisateur)


    if st.button("LSA MODEL"):
        resultat = summarizer_lsa(texte_utilisateur)


with col2:
    st.markdown("Modèle pour texte en français:")
    if st.button("MODELE NLTK"):
        resultat = french_summarizer_nltk(texte_utilisateur)


    if st.button("MODELE TEXT_RANK"):
        resultat = french_summarizer_textrank(texte_utilisateur)


    if st.button("MODELE LEX_RANK"):
        resultat = french_summarizer_lexrank(texte_utilisateur)


    if st.button("MODELE LSA"):
        resultat = french_summarizer_lsa(texte_utilisateur)



st.markdown("Votre résumé :")

st.write(resultat)

