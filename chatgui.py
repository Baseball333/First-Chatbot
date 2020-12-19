# Create GUI with tkinter library
import tkinter
from tkinter import *

      def send():
             msg = EntryBox.get("1.0", "end-1c").strip()
             EntryBox.delete("0.0", END)
