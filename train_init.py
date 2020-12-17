# Initializing training data
training = []
output_empty = [0] * len(classes)
for doc in documents:
     # Initialize bag of words
     bag = []
     # List of tokenized words for the pattern
     pattern_words =  doc[0]
  
  
