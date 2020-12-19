for intent in intents["intents"]:
   for pattern in intents["patterns"]
    
               # Tokenize each word
               w = nltk_word.tokenize(pattern)
               words.extend(w)
               # Add each document
               documents.append((w, intent["tag"]))
               
               # Add each class to the class list
               if intent["tag"] not in classes:
                  classes.append(intent["tag"])
                                    
               
