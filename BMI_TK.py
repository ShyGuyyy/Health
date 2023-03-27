from BMICalc import BMI
from tkinter import ttk

class BMI_TK:

    def __init__(self, tab, result_label):
        self.tab = tab
        self.result_label = result_label

        # Kaalu textbox loomine(m)
        self.kaal_info = ttk.Label(self.tab, text="Palun sisestage oma pikkus meetrites!")
        self.kaal_info.pack(side="left")
        self.kaal_info.place(x=50, y=75)

        # Kaalu (Entry) loomine
        self.kaal = ttk.Entry(self.tab, font=("Comicsans", 23))
        self.kaal.pack(side="left")
        self.kaal.place(x=50, y=100)

        # Pikkuse textbox loomine(kg)
        self.pikkus_info = ttk.Label(self.tab, text="Palun sisestage oma kaal kilogrammides!")
        self.pikkus_info.pack(side="left")
        self.pikkus_info.place(x=50, y=175)

        # Pikkuse (Entry) loomine
        self.pikkus = ttk.Entry(self.tab, font=("Comicsans", 23))
        self.pikkus.pack(side="left")
        self.pikkus.place(x=50, y=200)

        # BMI nupp
        self.calculation_button = ttk.Button(self.tab, text="Vastus!", command=lambda: self.bmi_calc()) 
        self.calculation_button.pack()
        self.calculation_button.place(x=50, y=300)

        # Lõpp vastus 
        self.result_label = ttk.Label(self.tab, text="", font=("Comicsans", 36))
        self.result_label.pack(side="top")
        self.result_label.place(x=425, y=140)

    # BMI kalkulaator
    def bmi_calc(self):
            kaal = float(self.kaal.get())
            pikkus = float(self.pikkus.get())
            bmi_calc = BMI(kaal, pikkus)
            bmi = bmi_calc.calculation()
            self.result_label.config(text=f"Teie BMI on {bmi}!")