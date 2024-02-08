import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize
nltk.download("stopwords")
from nltk.corpus import stopwords
import string

def preProcess():
    for i in range(1, 1000):
        with open(f'text_files/file{i}.txt') as f:
            text = f.read()
            print("Original - ")
            print(text)
            print("(a) Lowercase the text - ")
            text = text.lower()
            print(text)
            print("(b) Perform tokenization - ")
            text = word_tokenize(text)
            print(text)
            print("(c) Remove stop words - ")
            text = [word for word in text if word not in stopwords.words("english")]
            print(text)
            print("(d) Remove punctuations - ")
            punct_set = set(string.punctuation)
            text = [word for word in text if word not in punct_set]
            print(text)
            text = ",".join(text)
        
        with open(f'processed_files/file{i}.txt', 'w') as f:
            f.write(text)

def preProcessString(text):
    text = text.lower()
    text = word_tokenize(text)
    text = [word for word in text if word not in stopwords.words("english")]
    punct_set = set(string.punctuation)
    text = [word for word in text if word not in punct_set]
    return text

if (__name__ == '__main__'):
    preProcess()