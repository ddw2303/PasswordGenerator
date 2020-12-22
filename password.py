import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
import random, string

#function for generating password
def generate():
    password.set(''.join(random.choices(data,k=int(x.get()))))

window = tk.Tk() #create window
window.title("Password Generator") #label window
window.geometry("300x150") #set size of window
window.configure(bg="#066960") #set color of window

x = tk.StringVar()
password = tk.StringVar()
data = '!@#$%^&*()' + string.ascii_letters + string.digits

#set font for buttons
buttonFont = tkFont.Font(family='Arial', size=11, weight='bold')

#lable dropdown and location of button
ttk.Label(window, text = "Length: ", font=buttonFont).grid(column=0, row=0, pady=10)


combo = ttk.Combobox(window, width=4, textvariable=x)
combo['values'] = [i for i in range(6,21)]
combo.grid(column=1, row=0, pady=5)

pass_button = tk.Button(window, text="Generate", font=buttonFont, command=generate)
pass_button.grid(row=1, column=0, pady=10, padx=5)#create, label, and set location of button
ttk.Entry(window, textvariable=password).grid(row=1, column=1, padx=1, pady=5)

window.mainloop()
