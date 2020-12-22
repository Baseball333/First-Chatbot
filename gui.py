from keras.models import load_model
model = load_model("chatbot_model.h5")
import json
import random
intents = json.loads(open("intents.json").read())
words = pickle.load(open("words.pkl", "rb"))
classes = pickle.load(open("classes.pkl", "rb"))

# Extract information from the files
def clean_sentences(sentences):









