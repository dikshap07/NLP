# pip install nltk



from nltk.stem.wordnet import WordNetLemmatizer

lem = WordNetLemmatizer()

from nltk.stem.porter import PorterStemmer

stem = PorterStemmer()


word = "Advertising"

print("Lemmatized :",lem.lemmatize(word,"v"))

print("Stemmed :",stem.stem(word))