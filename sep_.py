from tkinter import *
from tkinter import filedialog
from tkinter import END
from pandastable import Table
import numpy as np
import pandas as pd
import tkinter as tk

global window
window = Tk()
window.title("Data Visualization")
window.geometry("1080x720")
window.config(background = "white")






label_file_explorer = Label(window, 
							text = "File Explorer using Tkinter",
							width = 155, height = 4, 
							fg = "blue")

button_explore = Button(window, 
						text = "Browse a File",
						command = lambda: browseFiles())

button_visualize = Button(window,
						  text="Load file",
						  command=lambda: visualize())

label_file_explorer.grid(column = 1, row = 1)
button_explore.grid(column = 1, row = 2)
button_visualize.grid(column=1,row=3)

class DisplayTable(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, relief="sunken")

        label = tk.Label(self, text="DisplayTable", relief="sunken")
        label.grid(row=0, column=1, padx=10, pady=10, columnspan=4)

        df = pd.read_csv("titanic.csv")

        self.table_FRAME = tk.Frame(self)
        self.table = Table(self.table_FRAME,
                           dataframe=df,
                           showtoolbar=True,
                           showstatusbar=True)
        self.table.grid(row=0, column=0, padx=10, pady=10, columnspan=4)
        self.table_FRAME.grid(row=1, column=1, padx=30, pady=10, columnspan=4,
                              rowspan=10)
        # self.table_FRAME.grid_propagate(False)
        # self.table_FRAME.configure(width=10, height=20)
        self.table.show()

def browseFiles():
	global filename
	filename = filedialog.askopenfilename(initialdir = "/",
										title = "Select a File",
										filetypes = (("Comma Separated Values file",
														"*.csv*"),
													("Excel Files",
			                                           "*.xls*" ),
													("all files",
														"*.*")))
	label_file_explorer.configure(text="File Opened: "+filename)

def visualize():
	if filename.endswith('.csv'):
		df=pd.read_csv(filename)
		app=DisplayTable(window)
		app.pack(fill='both',expand=True)
		app.pack_propagate(0)
		
window.mainloop()