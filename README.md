# First-Chatbot
This repository is the source code for my first chatbot. Note that I have not implemented this project in my CLI or on a GUI. The source code was written from a Medium article and hosted here for my own pleasure. Shoutout to Jere Xu, I'll fork his repo as well.

First Commit:
The description was quite vague, so I'll spare some of the viewers of this repository. When I was attempting to find a basic chatbot whose code I were to analyze and implement on my operating system's command line (Bash on Debian) I found Xu's Medium article. As I read his code and description of the chatbot's functionality I was intrigued to uploading the code on a repository as my own project. The code will be publicated in my own repository to record 2020's programming progress. I will still fork Xu's repository although I executed my separate implementation of the chatbot.

Second Commit:
Now that the nature of the project has been established, the functionality of the code is to be described. As Xu mentioned in the Medium article this repository is divided into nine files. More on this tomorrow.

Third Commit:
The eight files in this repository(excluding the README) are chatgui.py, gui.py, intents.json, libraries.py, train_init.py, train.py, init.py and words.py. Note that of these eight one is a JSON file meant for protocol communication between certain files in the repository. Among these files the first procedure is to import the necessary libraries. These libraries are NLTK, JSON, and Pickle. The links to their respective documentation will be provided at the end of the repository README. NLTK is a family of Python libraries which specify natural language processing. JSON is a prominent JavaScript library which applies human text to store and transmit data. Finally Pickle is another standard library which provides data serialization. In programming serialization is the process of translating a data structure which will be stored and translated into another format.

Fourth Commit:
The second file in this repository is init.py Its functionality is mostly based upon the writing of several components through the table type. These tables are also related to the initialization of the JSON dependencies which will be applied in a later commit.

Fifth Commit:
The third file is perhaps the most important in this section of the repository. The JSON intents specify language protocols between the chatbot and user.

Sixth Commit:
After the intiaization of the JSON dependencies, the lem.py file is written. This file is based on lemmatization, which is the process of reducing an inflected word to its base. Lemmatization will sort the lists and view the output in the interpreter.

Seventh Commit:
It is time to build the deep learning model. The deep learning model is distributed among the files train.py and train_init.py.

Eighth Commit:
Across these two files are specific features such as model compilation with "Nesterov Gradient Acceleration" and intents/pattern recognition. The code is somewhat self-explanatory.

Ninth Commit:
Time to add another intents file. The file mostly specifies intents.

Tenth Commit:
The final main procedure of the project is to build the chatbot's main GUI. Although I did not build it on my command-line, Xu specifies its code on his Medium article. As such I will write the first file(chatgui.py).
