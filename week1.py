#!/bin/python

import tkinter as tk


class entry:
    def __init__(self, field_name, grid_row, parent):
        self.lbl = tk.Label(master=parent, text=field_name)
        self.entry = tk.Entry(master=parent, width=20, fg='black')
        self.lbl.grid(row=grid_row, column=0)
        self.entry.grid(row=grid_row, column=1)

class button:
    def __init__(self, btn_text, grid_row, grid_col, parent, method):
        self.btn = tk.Button(master=parent, text=btn_text, command=method)
        self.btn.grid(row=grid_row, column=0, columnspan=grid_col, sticky = tk.W+tk.E)

class label:
    def __init__(self, lbl_text, grid_row, col_span, parent):
        self.lbl = tk.Label(master=parent, text=lbl_text)
        self.lbl.grid(row=grid_row, column=0, columnspan=col_span, sticky = tk.W+tk.E)

#Takes in args from button press
def calc_bmi(weight, height, output):
    height = float(height) #convert from str to float 
    weight = float(weight) 
    height /= 100 #Convery height to meters
    height *= height #square it
    bmi = weight / height
    output.lbl['text'] = "Your BMI is: " + str(round(bmi,1))

def main():
    window = tk.Tk()
    frame = tk.Frame(
        master=window,
        borderwidth=1
    )
    result = 0 #temp so this symbol is defined when passing.
    weight = entry("Weight [kg]: ", 0, frame)
    height = entry("Height [cm]", 1, frame)
    btn_submit = button("Submit", 2, 2, frame, lambda : calc_bmi(weight.entry.get(), height.entry.get(), result))
    result = label("Result: ", 3, 2, frame)
    btn_close = button("Close", 4, 2, frame, window.destroy) 
    
    

    frame.pack()
    window.mainloop()

#From what I understand this is basically a way to check
#if this script is being run from somewhere else
#or run directly.
#So if the script is run directly it will run this code and invoke main
#else it won't run anything and will expect it's code to be invoked elsewhere
if __name__ == "__main__":
    main()
