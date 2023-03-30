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
        self.kaal = ttk.Entry(self.tab, font=("Arial", 23))
        self.kaal.pack(side="left")
        self.kaal.place(x=50, y=50)

        # Pikkuse textbox loomine(kg) TAB2
        self.pikkus_info = ttk.Label(self.tab, text="Palun sisestage oma kaal kilogrammides!")
        self.pikkus_info.pack(side="left")
        self.pikkus_info.place(x=50, y=125)

        # Pikkuse (Entry) loomine TAB2
        self.pikkus = ttk.Entry(self.tab, font=("Arial", 23))
        self.pikkus.pack(side="left")
        self.pikkus.place(x=50, y=150)

        # Vanuse textbox loomine (A) TAB 2
        self.vanus_info = ttk.Label(self.tab, text="Palun sisestage oma vanus aastates!")
        self.vanus_info.pack(side="left")
        self.vanus_info.place(x=50, y=225)

        # Vanuse (Entry) loomine TAB2
        self.vanus = ttk.Entry(self.tab, font=("Arial", 23))
        self.vanus.pack(side="left")
        self.vanus.place(x=50, y=250)

        # BMR Nupp
        self.calculation_button_1 = ttk.Button(self.tab, text="Vastus!", command=lambda: self.kalo_calc(1)) 
        self.calculation_button_1.pack()
        self.calculation_button_1.place(x=50, y=325)
        
        self.aktiivsuse_info = ttk.Label(self.tab, text="Kuidas hindaksid oma aktiivsuse tasemet?")
        self.aktiivsuse_info.place(x=575, y=300)

        # BMR Nupp(Mõõdukas aktiivsus [1.5]) 1-2 Korda Nädalas
        self.calculation_button_2 = ttk.Button(self.tab, text="Mõõdukas", command=lambda: self.kalo_calc(2)) 
        self.calculation_button_2.pack()
        self.calculation_button_2.place(x=550, y=325)
        # BMR Nupp(Rohke aktiivsus [1.8]) 3-5 Korda nädalas
        self.calculation_button_3 = ttk.Button(self.tab, text="Rohke", command=lambda: self.kalo_calc(3)) 
        self.calculation_button_3.pack()
        self.calculation_button_3.place(x=650, y=325)
        # BMR Nupp(Kõrge aktiivsus [2.2]) 6-7 Korda nädalas
        self.calculation_button_4 = ttk.Button(self.tab, text="Kõrge", command=lambda: self.kalo_calc(4)) 
        self.calculation_button_4.pack()
        self.calculation_button_4.place(x=750, y=325)

        # self.calculation_button_5 = ttk.Button(self.tab, text="Mees", command=lambda: self.kalo_calc(5)) 
        # self.calculation_button_5.pack()
        # self.calculation_button_5.place(x=600, y=250)

        # self.calculation_button_6 = ttk.Button(self.tab, text="Naine", command=lambda: self.kalo_calc(6)) 
        # self.calculation_button_6.pack()
        # self.calculation_button_6.place(x=700, y=250)

        # Lõpp vastus
        self.result_label = ttk.Label(self.tab, text="", font=("Arial", 36))
        self.result_label.pack(side="top")
        self.result_label.place(x=425, y=140)

    # Kalorite kalkulaator
    def kalo_calc(self, aktiivsus_tase):
            kaal = float(self.kaal.get())
            pikkus = float(self.pikkus.get())
            vanus = int(self.vanus.get())
            kalo_calc = Kalorid(kaal, pikkus, vanus)
            kalo = kalo_calc.säilimine()
            # Kontrollib mis nuppu sa vajutasid ja selle järelt teeb arvutused.
            if aktiivsus_tase == 1:
                self.result_label.config(text=f"Teie BMR on {round(kalo, 0)}Kcal")
            elif aktiivsus_tase == 2:
                 self.result_label.config(text=f"Teie BMR on {round(kalo * 1.5, 0)}Kcal")
            elif aktiivsus_tase == 3:
                 self.result_label.config(text=f"Teie BMR on {round(kalo * 1.8, 0)}Kcal")
            elif aktiivsus_tase == 4:
                 self.result_label.config(text=f"Teie BMR on {round(kalo * 2.2, 0)}Kcal")