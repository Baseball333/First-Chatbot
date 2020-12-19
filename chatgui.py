# Create GUI with tkinter library
import tkinter
from tkinter import *

      def send():
             msg = EntryBox.get("1.0", "end-1c").strip()
             EntryBox.delete("0.0", END)

             if msg != "":
                   ChatLog.config(state=NORMAL)
                   Chatlog.insert(END, "You: " + msg + "\n\n")
                   ChatLog.config(foreground="#442265", font=(("Verdana", 12))
                                  
                   res = chatbot_response(msg)
                   Chatlog.insert(END, "Bot: " + res + "\n\n")
                                 
                   ChatLog.config(state=DISABLED)           
                   ChatLog.yview(END)        
                                  
                                  
       base = Tk()
       base.title("Hello")
       base.geometry("400x500")
       base.resizable(width=FALSE, height=FALSE)
                                  
       # Create the chat window
       ChatLog = Text(base, bd=0, bg="white", height="8", width=50, font="Arial")
                        
       ChatLog.config(state=DISABLED)
                                  
                        
                                  
