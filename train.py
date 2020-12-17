# Create model with 3 layers
# The first layer is 128 neurons the second 64 and the third varied
# The third output is equal to the number of intents
model = Sequential()
model.add(Dense(128, input_shape=len(train_x[0]),), activation="relu"))
model.add(Dropout(0.5))
model.add(Dense(64, activation="relu"))
model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]), activation = "softmax"))

# Compile model with Nesterov gradient acceleration, which provides results for the model
sgd = SGD(lr = 0.01, decay=le-6, momentum=6, nesterov=True)
model.compile(loss = "categorical crossentrophy" optimizer=SGD, metrics=["accur"])
