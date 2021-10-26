#!/usr/bin/env python3

import csv
import argparse
import tkinter as tk

class ScrollableFrame():
    def __init__(self, parent):
        self.canvas = tk.Canvas(master = parent)
        scrolly = tk.Scrollbar(master=parent, orient="vertical", command=self.canvas.yview)
        scrollx = tk.Scrollbar(master=parent, orient="horizontal", command=self.canvas.xview)
        self.frame = tk.Frame(master=self.canvas, borderwidth=1)

        self.frame = tk.Frame(master=self.canvas, borderwidth=1)
        scrolly.pack(side = tk.RIGHT, fill = tk.Y)
        scrollx.pack(side = tk.BOTTOM, fill = tk.X)
        self.frame.bind(
        "<Configure>",
        lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        self.canvas.create_window((0, 0), window=self.frame, anchor="nw")
        self.canvas.configure(yscrollcommand=scrolly.set)
        self.canvas.configure(xscrollcommand=scrollx.set)
        self.canvas.pack(side = "top", fill="both", expand=True)


def open_file(file_pth):
    string = type(file_pth) #Type check the arg
    if string != str: #Check if its a string 
        print("File Path Input Type not string\n") #print error 
        print(string) #Print the type of the string 
        exit(1) #Exit with error 
    try:
        csvfile = open(file_pth)
    except FileNotFoundError: #if file not found exception occurs when opening  
        print(f"File {file_pth} does not exist") #print error 
        exit(2) #exit with error
    else:
        csvdata = csv.reader(csvfile, delimiter=',') #else read the data from the file 
        return csvdata

def create_gui(data):
    window = tk.Tk()
    csvcontent = ScrollableFrame(window)
    rowcount = 0 #row counter
    colcount = 0 #column counter
    for rows in data:
        rowcount += 1
        colcount = 0
        for cols in rows:
            colcount += 1
            entry = tk.Entry(master=csvcontent.frame, width=20, fg='black')
            entry.insert(tk.END, cols)
            entry.grid(row=rowcount, column=colcount)

    lbl_cols = tk.Label(master=csvcontent.frame, text=f"Column Count: {str(colcount)}")
    lbl_cols.grid(row=rowcount+1, column=1)
    lbl_rows = tk.Label(master=csvcontent.frame, text=f"Row Count: {str(rowcount)}")
    lbl_rows.grid(row=rowcount+2, column=1)

    window.mainloop()

if __name__ == "__main__":
    parse = argparse.ArgumentParser(description="simple CSV data displayer")
    parse.add_argument("-p", "--path", metavar='path', help='Path to csv file to open')
    args = parse.parse_args()
    data = open_file(args.path);
    create_gui(data)
