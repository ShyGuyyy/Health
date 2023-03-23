from BMICalc import BMI
import tkinter as tk
from tkinter import *

# Funktsioon mis kutsub BMI klassi ja entrid kokku et kalkuleerida BMI.
def bmi_calc(kaal_entry, pikkus_entry, result_lable):
    kaal = float(kaal_entry.get())
    pikkus = float(pikkus_entry.get())
    bmi_calc = BMI(kaal, pikkus)
    bmi = bmi_calc.calculation()
    result_lable.config(text=f"Teie BMI on {bmi}!")

# Tkinter akna avamine
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

# BMI nupp
calculation_button = tk.Button(master=win, text="Vastus!", command=lambda: bmi_calc(kaal, pikkus, result_label)) 
calculation_button.pack()

result_label = tk.Label(text="")
result_label.pack()

# Excecutable
win.mainloop()



