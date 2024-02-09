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
import base64

# current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
# css_file = current_dir / "styles" / "main.css"

# st.image('dark_night.jpg', width=230)
st.set_page_config(layout="wide")
# row1, row2 = st.columns(2)

# Membuat layout kolom dengan 10 kolom
col1, col2, col3, col4, col5 = st.columns(5)
st.write('---')
col6, col7, col8, col9, col10 = st.columns(5)

# Menampilkan judul film dan gambar untuk setiap kolom
with col1:
    st.subheader("The Dark Night")
    st.image("dark_night.jpg", width=150)  # Ganti "img1.jpg" dengan path gambar film yang sesuai

with col2:
    st.subheader("Inception")
    st.image("inceptionn.jpg", width=150)

with col3:
    st.subheader("The Matrix")
    st.image("the_matrix.jpg", width=150)

with col4:
    st.subheader("The Shawshank Redemption")
    st.image("the_shawshank.jpg", width=150)

with col5:
    st.subheader("Schindler's List")
    st.image("Schindler's_List_movie.jpg", width=150)

# st.write('---')  # Membuat garis pemisah antara baris

with col6:
    st.subheader("Star Wars")
    st.image("star_wars.jpg", width=150)

with col7:
    st.subheader("The Lord of the Rings")
    st.image("the_LOTR.jpg", width=150) 

with col8:
    st.subheader("The Godfather")
    st.image("the_godfather.jpg", width=150)

with col9:
    st.subheader("Taxi Driver")
    st.image("Taxi_Driver.jpg", width=150)

with col10:
    st.subheader("Gone with the Wind")
    st.image("gone_with_the_wind.jpg", width=150)



path_dataset = st.secrets.path_configuration.path_dataset
filename = "imdb_reviews.csv"

df = pd.read_csv(f"{path_dataset}{filename}")

def csvdownload(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # Convert CSV string menjadi base64 (binary)
    href = f'<a href="data:file/csv;base64,{b64}" download="imdb_reviews.csv">Download CSV File</a>'
    return href

st.markdown(csvdownload(df), unsafe_allow_html=True)


# if st.markdown("Download CSV"):
#     # Tautan untuk mengunduh file CSV
#     csv = df.to_csv(index=False)
#     b64 = base64.b64encode(csv.encode()).decode()  # Convert CSV string menjadi base64 (binary)
#     href = f'<a href="data:file/csv;base64,{b64}" download="dataset.csv">Download CSV File</a>'
#     st.markdown(href, unsafe_allow_html=True)