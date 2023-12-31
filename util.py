import base64
import streamlit as st
from PIL import ImageOps, Image
import os
import numpy as np
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Dropout, BatchNormalization, Flatten, Dense
from keras.preprocessing.image import ImageDataGenerator
from bs4 import BeautifulSoup as bs
from requests import get
import re
import nltk
nltk.download('punkt')
nltk.download('stopwords')
from sumy.summarizers.text_rank import TextRankSummarizer
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.summarizers.lsa import LsaSummarizer

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer

def background(image_file):
    with open(image_file, "rb") as f:
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

texte_utilisateur = ""



# Créer un text parser utilisant de tokenisation
parser = PlaintextParser.from_string(texte_utilisateur, Tokenizer('english'))

parser.document.sentences

def summarizer_nltk(texte_utilisateur, num_sentences=5):

    sentence_list = nltk.sent_tokenize(texte_utilisateur)

    # Stopwords
    stopwords = nltk.corpus.stopwords.words('english')
    # Dictionnaire de fréquences des mots
    word_frequencies = {}
    for word in nltk.word_tokenize(texte_utilisateur):
        if word not in stopwords:
            if word not in word_frequencies.keys():
                word_frequencies[word] = 1
            else:
                word_frequencies[word] += 1

        # Fréquence maximale
    maximum_frequency = max(word_frequencies.values())
    # Calculer la fréquence pondérée
    for word in word_frequencies.keys():
        word_frequencies[word] = word_frequencies[word] / maximum_frequency

        sentence_scores = {}
    # Calculer le score de chaque phrase
    for sent in sentence_list:
        for word in nltk.word_tokenize(sent.lower()):
            if word in word_frequencies.keys():
                if len(sent.split(' ')) < 30:
                    if sent not in sentence_scores.keys():
                        sentence_scores[sent] = word_frequencies[word]
                    else:
                        sentence_scores[sent] += word_frequencies[word]

    # Ordonner les phrases par pondération et recupérer les 10 premières phrases
    summary_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=False)[:10]
    # regrouper ensemble les phrases qui ont les poids les plus élévés
    summary = ' '.join(summary_sentences)

    # Afficher le résumé

    return summary


def summarizer_textrank(texte_utilisateur, num_sentences=5):
# Initialiser le modèle
    summarizer_textrank = TextRankSummarizer()

    #tokeniser
    parser = PlaintextParser.from_string(texte_utilisateur, Tokenizer('english'))

    # Summariser en 5 phrases
    summary = summarizer_textrank(parser.document, 5)

    # Regrouper les phrases
    text_summary = ""
    for sentence in summary:
        text_summary += str(sentence)

    # Afficher le summary
    return text_summary

def summarizer_lexrank(texte_utilisateur, num_sentences=5):
# Initialiser le modèle
    summarizer_lexrank = LexRankSummarizer()

    parser = PlaintextParser.from_string(texte_utilisateur, Tokenizer('english'))


    # Summariser en 5 phrases
    summary = summarizer_lexrank(parser.document, 5)

    # Regrouper les phrases
    text_summary = ""
    for sentence in summary:
        text_summary += str(sentence)
        
    # Afficher le summary
    return text_summary

def summarizer_lsa(texte_utilisateur, num_sentences=5):
# Initialiser le modèle
    summarizer_lsa = LsaSummarizer()

    parser = PlaintextParser.from_string(texte_utilisateur, Tokenizer('english'))

    # Summariser en 5 phrases
    summary = summarizer_lsa(parser.document, 5)

    # Regrouper les phrases
    text_summary = ""
    for sentence in summary:
        text_summary += str(sentence)

    # Afficher le summary
    return text_summary

#- ---------------------------------------------------FRENCH---------------------------------------------

# Créer un text parser utilisant de tokenisation
parser_french = PlaintextParser.from_string(texte_utilisateur, Tokenizer('french'))

parser_french.document.sentences

def french_summarizer_nltk(texte_utilisateur, num_sentences=5):

    sentence_list = nltk.sent_tokenize(texte_utilisateur)

    # Stopwords
    stopwords = nltk.corpus.stopwords.words('french')
    # Dictionnaire de fréquences des mots
    word_frequencies = {}
    for word in nltk.word_tokenize(texte_utilisateur):
        if word not in stopwords:
            if word not in word_frequencies.keys():
                word_frequencies[word] = 1
            else:
                word_frequencies[word] += 1

        # Fréquence maximale
    maximum_frequency = max(word_frequencies.values())
    # Calculer la fréquence pondérée
    for word in word_frequencies.keys():
        word_frequencies[word] = word_frequencies[word] / maximum_frequency

        sentence_scores = {}
    # Calculer le score de chaque phrase
    for sent in sentence_list:
        for word in nltk.word_tokenize(sent.lower()):
            if word in word_frequencies.keys():
                if len(sent.split(' ')) < 30:
                    if sent not in sentence_scores.keys():
                        sentence_scores[sent] = word_frequencies[word]
                    else:
                        sentence_scores[sent] += word_frequencies[word]

    # Ordonner les phrases par pondération et recupérer les 10 premières phrases
    summary_sentences_french = sorted(sentence_scores, key=sentence_scores.get, reverse=False)[:10]
    # regrouper ensemble les phrases qui ont les poids les plus élévés
    summary = ' '.join(summary_sentences_french)

    # Afficher le résumé

    return summary

def french_summarizer_textrank(texte_utilisateur, num_sentences=5):
# Initialiser le modèle
    summarizer_textrank = TextRankSummarizer()

    #tokeniser
    parser_french = PlaintextParser.from_string(texte_utilisateur, Tokenizer('french'))

    # Summariser en 5 phrases
    summary = summarizer_textrank(parser_french.document, 5)

    # Regrouper les phrases
    text_summary = ""
    for sentence in summary:
        text_summary += str(sentence)

    # Afficher le summary
    return text_summary

def french_summarizer_lexrank(texte_utilisateur, num_sentences=5):
# Initialiser le modèle
    summarizer_lexrank = LexRankSummarizer()

    parser_french = PlaintextParser.from_string(texte_utilisateur, Tokenizer('french'))


    # Summariser en 5 phrases
    summary = summarizer_lexrank(parser_french.document, 5)

    # Regrouper les phrases
    text_summary = ""
    for sentence in summary:
        text_summary += str(sentence)
        
    # Afficher le summary
    return text_summary

def french_summarizer_lsa(texte_utilisateur, num_sentences=5):
# Initialiser le modèle
    summarizer_lsa = LsaSummarizer()

    parser_french = PlaintextParser.from_string(texte_utilisateur, Tokenizer('french'))

    # Summariser en 5 phrases
    summary = summarizer_lsa(parser_french.document, 5)

    # Regrouper les phrases
    text_summary = ""
    for sentence in summary:
        text_summary += str(sentence)

    # Afficher le summary
    return text_summary