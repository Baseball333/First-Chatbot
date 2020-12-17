# Initializing training data
training = []
output_empty = [0] * len(classes)
for doc in documents:
     # Initialize bag of words
     bag = []
     # List of tokenized words for the pattern
     pattern_words =  doc[0]
     # Lemmatize each word, creating its base
     pattern_words = [lemmatizer.lemmatize(word.lower()) for word in pattern_words]
     # Create the bag of words array with 1 if word is matched in pattern
     for w in words:
          bag.append(1) if w in pattern_words else bag.append(0)
          
      # Output is a "0" for each tag and "1" for the current tag
      output_row = list(output_empty)
      output_row[classes.index(doc[1])] = 1
     
          
          
          
