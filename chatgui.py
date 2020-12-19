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
                                  
