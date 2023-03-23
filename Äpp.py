from BMICalc import BMI
import tkinter as tk
from tkinter import *

win = tk.Tk()

# Äppi geomeetriline suurus
win.geometry("800x400")

# Äppi nimi
name = tk.Label(text="Health!")
name.pack()

# Kaalu (Entry) loomine
kaal = Entry(master=win, font=("Comicsans", 23))
kaal.pack(side="left")
kaal.place(x=50, y=100)

# Pikkuse (Entry) loomine
pikkus = Entry(master=win, font=("Comicsans", 23))
pikkus.pack(side="left")
pikkus.place(x=50, y=200)

calc_1 = Button(master=win, text="BMICalc", command=) 

# Excecutable
win.mainloop()



