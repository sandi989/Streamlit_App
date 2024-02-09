import pandas as pd
from nlp_id.lemmatizer import Lemmatizer
from nlp_id.tokenizer import Tokenizer, PhraseTokenizer
from nlp_id.postag import PosTag
from nlp_id.stopword import StopWord
import nltk
from text_processing import TextProcessing
from pandas import DataFrame
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk import ngrams
from tqdm import tqdm
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import streamlit as st 
from pathlib import Path

# current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
# css_file = current_dir / "styles" / "main.css"

# st.image('dark_night.jpg', width=230)
st.set_page_config(layout="wide")
row1, row2 = st.columns(2)

for i in range(2):
    st.write('---')  # Membuat garis pemisah antara baris

    # Membuat layout kolom dengan 5 kolom
    col1, col2, col3, col4, col5 = st.columns(5)

    # Menampilkan judul film dan gambar untuk setiap kolom
    with col1:
        st.subheader(df.iloc[i*5]['judul_film'])
        st.image(df.iloc[i*5]['gambar'], width=150)  # Ubah width sesuai kebutuhan

    with col2:
        st.subheader(df.iloc[i*5+1]['judul_film'])
        st.image(df.iloc[i*5+1]['gambar'], width=150)

    with col3:
        st.subheader(df.iloc[i*5+2]['judul_film'])
        st.image(df.iloc[i*5+2]['gambar'], width=150)

    with col4:
        st.subheader(df.iloc[i*5+3]['judul_film'])
        st.image(df.iloc[i*5+3]['gambar'], width=150)

    with col5:
        st.subheader(df.iloc[i*5+4]['judul_film'])
        st.image(df.iloc[i*5+4]['gambar'], width=150)

# Baris 1
with row1:

    # Kolom 1
    st.subheader("The Dark Night")
    st.image("dark_night.jpg", width=150)  # Ganti "img1.jpg" dengan path gambar film yang sesuai
    # Kolom 2
    st.subheader("Inception")
    st.image("inception.jpg", width=150)  # Ganti "img2.jpg" dengan path gambar film yang sesuai
    # Kolom 3
    st.subheader("The Matrix")
    st.image("the_matrix.jpg", width=150)  # Ganti "img3.jpg" dengan path gambar film yang sesuai
    # Kolom 4
    st.subheader("The Shawshank Redemption")
    st.image("the_shawshank.jpg", width=150)  # Ganti "img4.jpg" dengan path gambar film yang sesuai
    # Kolom 5
    st.subheader("Schindler's List")
    st.image("Schindler's_List_movie.jpg", width=150)  # Ganti "img5.jpg" dengan path gambar film yang sesuai

with row2:
    st.subheader("Star Wars: Episode IV - A New Hope")
    st.image("star_wars.jpg", width=150)  # Ganti "img6.jpg" dengan path gambar film yang sesuai
    # Kolom 2
    st.subheader("The Lord of the Rings: The Fellowship of the Ring")
    st.image("the_LOTR.jpg", width=150)  # Ganti "img7.jpg" dengan path gambar film yang sesuai
    # Kolom 3
    st.subheader("The Godfather")
    st.image("the_godfather.jpg", width=150)  # Ganti "img8.jpg" dengan path gambar film yang sesuai
    # Kolom 4
    st.subheader("Taxi Driver")
    st.image("Taxi_Driver.jpg", width=150)  # Ganti "img9.jpg" dengan path gambar film yang sesuai
    # Kolom 5
    st.subheader("Gone with the Wind")
    st.image("gone_with_the_wind.jpg", width=150)  # Ganti "img10.jpg" dengan path gambar film yang sesuai


    