words=[]
classes=[]
documents=[]
ignore_words= ["?", "!"]
data_file = open("intents.json").read()
intents = json.loads(data_file)
