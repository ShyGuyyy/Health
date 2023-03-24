from BMICalc import BMI
import tkinter as tk
from tkinter import *
from tkinter import ttk

# Funktsioon mis kutsub BMI klassi ja entrid kokku et kalkuleerida BMI.
def bmi_calc(kaal_entry, pikkus_entry, result_lable):
    kaal = float(kaal_entry.get())
    pikkus = float(pikkus_entry.get())
    bmi_calc = BMI(kaal, pikkus)
    bmi = bmi_calc.calculation()
    result_lable.config(text=f"Teie BMI on {bmi}!")

# Tkinter akna avamine
win = tk.Tk()

# Äppi nimi
win.title("Health!")

# Äppi geomeetriline suurus
win.geometry("800x400")

# Kaalu textbox loomine(m)
kaal_info = tk.Label(text="Palun sisestage oma pikkus meetrites!")
kaal_info.pack(side="left")
kaal_info.place(x=50, y=75)

# Kaalu (Entry) loomine
kaal = Entry(master=win, font=("Comicsans", 23))
kaal.pack(side="left")
kaal.place(x=50, y=100)

# Pikkuse textbox loomine(kg)
pikkus_info = tk.Label(text="Palun sisestage oma kaal kilogrammides!")
pikkus_info.pack(side="left")
pikkus_info.place(x=50, y=175)

# Pikkuse (Entry) loomine
pikkus = Entry(master=win, font=("Comicsans", 23))
pikkus.pack(side="left")
pikkus.place(x=50, y=200)

# BMI nupp
calculation_button = tk.Button(master=win, text="Vastus!", command=lambda: bmi_calc(kaal, pikkus, result_label)) 
calculation_button.pack()
calculation_button.place(x=50, y=300)

# Lõpp vastus 
result_label = tk.Label(text="", font=("Comicsans", 36))
result_label.pack(side="top")
result_label.place(x=425, y=145)

# Excecutable
win.mainloop()



