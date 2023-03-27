from tkinter import ttk
from CalorieCalc import Kalorid


class CalorieTK:

    def __init__(self, tab, result_label):
        self.tab = tab
        self.result_label = result_label

        # Kaalu textbox loomine(m) TAB 2
        self.kaal_info = ttk.Label(self.tab, text="Palun sisestage oma pikkus sentimeetrites!")
        self.kaal_info.pack(side="left")
        self.kaal_info.place(x=50, y=25)

        # Kaalu (Entry) loomine TAB2
        self.kaal = ttk.Entry(self.tab, font=("Comicsans", 23))
        self.kaal.pack(side="left")
        self.kaal.place(x=50, y=50)

        # Pikkuse textbox loomine(kg) TAB2
        self.pikkus_info = ttk.Label(self.tab, text="Palun sisestage oma kaal kilogrammides!")
        self.pikkus_info.pack(side="left")
        self.pikkus_info.place(x=50, y=125)

        # Pikkuse (Entry) loomine TAB2
        self.pikkus = ttk.Entry(self.tab, font=("Comicsans", 23))
        self.pikkus.pack(side="left")
        self.pikkus.place(x=50, y=150)

        # Vanuse textbox loomine (A) TAB 2
        self.vanus_info = ttk.Label(self.tab, text="Palun sisestage oma vanus aastates!")
        self.vanus_info.pack(side="left")
        self.vanus_info.place(x=50, y=225)

        # Vanuse (Entry) loomine TAB2
        self.vanus = ttk.Entry(self.tab, font=("Comicsans", 23))
        self.vanus.pack(side="left")
        self.vanus.place(x=50, y=250)

        # BMR Nupp
        self.calculation_button = ttk.Button(self.tab, text="Vastus!", command=lambda: self.kalo_calc()) 
        self.calculation_button.pack()
        self.calculation_button.place(x=50, y=325)

        # Lõpp vastus
        self.result_label = ttk.Label(self.tab, text="", font=("Comicsans", 36))
        self.result_label.pack(side="top")
        self.result_label.place(x=425, y=140)

    # Kalorite kalkulaator
    def kalo_calc(self):
            kaal = float(self.kaal.get())
            pikkus = float(self.pikkus.get())
            vanus = int(self.vanus.get())
            kalo_calc = Kalorid(kaal, pikkus, vanus)
            kalo = kalo_calc.säilimine()
            self.result_label.config(text=f"Teie BMR on {kalo}Kcal!")