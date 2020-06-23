""" This file is a compagnon file for the app to facilitate the interaction
 with the user when needed """

#Import necessary libraries
from tkinter import*
from tkinter import ttk
from tkinter.filedialog import askopenfile
from textsummary import Summary

import os
import sys

class SummaryGUI:
    """ Create a small graphical interface user app for better interaction with the user"""

    def __init__(self, master):
        """ Initialize all the necessary attributes for the class"""

        master.title("Summarizer")
        master.configure(bg='gray40')
        #master.geometry('500x500')
        master.resizable(False, False)

        self.style = ttk.Style()
        self.style.configure('TFrame', background='brown1')
        self.style.configure('TButton', background='#e1d8b9')
        self.style.configure('TLabel', background='#e1d8b9', font=('Arial', 13))
        self.style.configure('Header.TLabel', font=('Arial', 20, 'bold'))

        self.frame_header = ttk.Frame(master)
        self.frame_header.pack()

        ttk.Label(self.frame_header, text='Welcome!', style='Header.TLabel').grid(row=0, column=1)
        ttk.Label(self.frame_header, wraplength=300, text='Summarizing Tool for text articles or files', font=('Arial', 16, 'bold italic')).grid(row=1, column=1)

        self.frame_content = ttk.Frame(master)
        self.frame_content.pack()

        # Add more labels
        ttk.Label(self.frame_content, text="Open a file or copy and paste your text below:").grid(row=1, column=0, padx=0, pady=0)
        ttk.Button(self.frame_content, text='Open', command = self.open_file).grid(row=2, column=0, padx=0, pady=0)

        self.text1 = Text(self.frame_content, width=30, height=20, font = ('Arial', 14))
        self.text1.grid(row=3, column=2, padx = 5 , pady = 10)

        # Create a string variable to be used in the combobox
        #self.country = StringVar()
        #combobox = ttk.Combobox(self.frame_content, textvariable=self.country)
        #combobox.grid(row=4, column=0, padx=10)
        #self.country.set('Countries:')
        #combobox.config(values=self.covid_countries_names())
        #combobox.bind("<<ComboboxSelected>>", self.covid_numbers_country)

        self.text2 = Text(self.frame_content, width=30, height=20, font=('Arial', 13),
                              )
        self.text2.grid(row=3, column=0)

        ttk.Button(self.frame_content, text='Summarize',).grid(row=2, column=2, padx=0, pady=5)
        ttk.Button(self.frame_content, text='Exit',
                       command=self.exit_program).grid( row = 2, column = 1, sticky = W)

    def exit_program(self):

            os._exit(0)

    def open_file(self):

        file = askopenfile(mode = 'r', filetypes = [("file types","*.txt")])
        if file is not None:
            data = file.read()

            return data


def main():
    root = Tk()
    summarize = SummaryGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()

