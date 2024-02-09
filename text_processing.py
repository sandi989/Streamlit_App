import re
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
from typing import List

class TextProcessing:
    def __init__(self) -> None:
        self.stopword_en = stopwords.words('english')
        self.stopword_id = stopwords.words('indonesian')

    def lowercase(self, data: str) -> str:
        result = data.lower()
        return result

    def tokenization(self, data: str) -> List[str]:
        result = word_tokenize(data)
        return result

    def text_cleaning(self, data: str) -> str:
        # number
        data = re.sub(r"\d+", "", data)
        # @pattern
        at_pattern = re.compile(r'@\S+')
        data = at_pattern.sub(r'', data)
        # double quotes
        data = re.sub(r'"', '', data)
        # url
        url_pattern = re.compile(r'https?://\S+|www\.\S+')
        hasil = url_pattern.sub(r'', data)
        # puctuation
        data = data.translate(str.maketrans("", "", string.punctuation))
        # whitespace
        data = data.strip()

        return hasil

    def stopword_removal(self, data: List[str]) -> str:
        stop_words = self.stopword_id
        result_words = [word for word in data if word not in stop_words]
        result = ' '.join(result_words)
        return result

    def stemming(self, data: str) -> str:
        st = PorterStemmer()
        return st.stem(data)
    
    def lemmatize(self, data: List[str]) -> List[str]:
        lemmatizer = WordNetLemmatizer()
        result_words = [lemmatizer.lemmatize(word) for word in data]
        result = ' '.join(result_words)
        return result



if __name__ == '__main__':
    test = " Selamat Pagi Indonesia 100 #@ duapuluh. Data ini dikirimkan dari planet nun jauh dari sana"

    mod = TextProcessing()
    hasil = mod.lowercase(test)
    hasil = mod.text_cleaning(hasil)  # Panggil text_cleaning setelah lowercase
    hasil = mod.tokenization(hasil)
    hasil = mod.stopword_removal(hasil)
    hasil = mod.stemming(hasil)
    # hasil = mod.lemmatize(hasil)

    print(hasil)
