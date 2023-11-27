#A tool that can automatically create a basic HTML web page

import tkinter as tk
from tkinter import *
import webbrowser

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("Web Page Generator")
        #Creatind a custom text
        self.custom = Label(self.master, text="Enter Custom Text")
        self.custom.grid(row=1, column=1, padx=(10,10), pady=(0,0))
        #Create a default HTML page button
        self.btn = Button(self.master, text="Default HTML Page", width=30, height=2, command=self.defaultHTML)
        self.btn.grid(row=3, column=1, padx=(0, 0), pady=(10, 10), sticky='E')
        #Create a Submit button
        self.submit_btn = Button(text="Submit Custom Text", width=30, height=2, command=self.get_label)
        self.submit_btn.grid(row=3, column=2, padx=(0,10), pady=(10, 10), sticky='E')
        #Creating an input widget
        self.userEntry = Entry(self.master, text="", width=100)
        self.userEntry.grid(row=2, column=1, padx=(10,10), pady=(0,0), sticky='NSEW', columnspan=2)
        self.userEntry.focus_set()
    
    # Create a function to return the Input data
    def get_label(self):
        htmlText = self.userEntry.get()
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")

           
    #New function to create an HTML document
    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer sale!"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")



if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
