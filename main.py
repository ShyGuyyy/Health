from tkinter import *
from tkinter import ttk
from CalorieTK import CalorieTK
from BMI_TK import BMI_TK

root = Tk()

root.geometry("1000x400")

tabControl = ttk.Notebook(root)

tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)

tabControl.add(tab1, text='BMI Kalkulaator')
tabControl.add(tab2, text='Kalorite kalkulaator')

result_label = ttk.Label(tab2, text="", font=("Arial", 36))
result_label.pack(side="top")
result_label.place()

BMICalculator = BMI_TK(tab1, result_label)
CalorieCalculator = CalorieTK(tab2, result_label)

tabControl.pack(expand=1, fill="both")

root.mainloop()



