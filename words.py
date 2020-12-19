for intent in intents["intents"]:
   for pattern in intents["patterns"]
    
               # Tokenize each word
               w = nltk_word.tokenize(pattern)
               words.extend(w)
               # Add each document
               documents.append((w, intent["tag"]))
  
