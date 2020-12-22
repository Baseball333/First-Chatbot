from keras.models import load_model
model = load_model("chatbot_model.h5")
import json
import random
intents = json.loads(open("intents.json").read())
words = pickle.load(open("words.pkl", "rb"))
classes = pickle.load(open("classes.pkl", "rb"))

# Extract information from the files
def clean_sentences(sentences):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]

    return sentence_words

# Return bag of words array; 0 or 1 that exists for each sentence

def bow(sentence, words show_details = True):
       # Tokenize the pattern
       sentence_words = clean_sentence(sentence)
