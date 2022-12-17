# import pandas as pd
import numpy as np
import pickle
import re
from nltk.stem import PorterStemmer


def clean_text(text):
  """
  Function that cleans text to be added to api

  text - text fetched from GET request.
  """

  ps = PorterStemmer()

  # change to lowercase
  new_text = text.lower()

  # Remove apostrophes
  new_text = re.sub(r"'s\b", "", new_text)

  # Remove punctuation
  new_text = re.sub(r"[^\w\s]", "", new_text)

  words = []

  for word in new_text.split():
    if len(word) >= 3:
      words.append(ps.stem(word))

  new_text = " ".join(words)

  return (new_text)

def classify(text):
  """
  predict_news - predicts the authenticity of news given in text.

  @text: text representing news to classify as real or fake
  
  Return: Real if news is real and fake otherwise
  """
  text = np.array([text])

  # loading label encoder
  with open("./Model/encoder.pkl", "rb") as handle:
    encoder = pickle.load(handle)

  # loading vectorizer
  with open('./Model/vectorizer.pkl', 'rb') as handle:
    vectorizer = pickle.load(handle)

  # loading model
  with open('./Model/model.pkl', 'rb') as handle:
    model = pickle.load(handle)

  enc_text = vectorizer.transform(text)

  pred = model.predict(enc_text)

  return (encoder.inverse_transform(pred)[0])
