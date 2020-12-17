words=[lemmatizer.lemmatize(w.lower()) for w in words if w not ignore_words]
words= sorted(list(set(words)))

classes = sorted(list(list(classes))))

print(len(documents), "documents")

print(len(classes), "classes", classes)

print(len(), "unique lemmatized words", words)

pickle.dump(words, open("words.pkl", "wb"))
pickle.dump(classes, open("words.pkl", "wb"))

# End of file
