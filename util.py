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

texte = ""

# Créer un text parser utilisant de tokenisation
parser = PlaintextParser.from_string(texte, Tokenizer('english'))

parser.document.sentences

def summarizer_textrank(text, num_sentences=5):
# Initialiser le modèle
    summarizer_textrank = TextRankSummarizer()

    # Summariser en 5 phrases
    summary = summarizer_textrank(parser.document, 5)

    # Regrouper les phrases
    text_summary = ""
    for sentence in summary:
        text_summary += str(sentence)

    # Afficher le summary
    return text_summary

def summarizer_lexrank(text, num_sentences=5):
# Initialiser le modèle
    summarizer_lexrank = LexRankSummarizer()

    # Summariser en 5 phrases
    summary = summarizer_lexrank(parser.document, 5)

    # Regrouper les phrases
    text_summary = ""
    for sentence in summary:
        text_summary += str(sentence)
        
    # Afficher le summary
    return text_summary

def summarizer_lsa(text, num_sentences=5):
# Initialiser le modèle
    summarizer_lsa = LsaSummarizer()

    # Summariser en 5 phrases
    summary = summarizer_lsa(parser.document, 5)

    # Regrouper les phrases
    text_summary = ""
    for sentence in summary:
        text_summary += str(sentence)

    # Afficher le summary
    return text_summary


