import os
from BMI import BMI
from CalorieCalc import Kalorid

# BMI
pikkus = float(input("Palun sisestage enda pikkus (Meeter)\n: "))
kaal = float(input("Palun sisestage oma kaal (KG)\n: "))

ratio = BMI(pikkus, kaal)
os.system("cls")
ratio.calculation()

cont = str(input("Kas soovite ka teada teie säilituskalorid (Kcal)?\nKui jah sisestage 'Y' kui ei siis 'N'\n: ")).lower()
os.system("cls")
if cont == "y":
# Kalorid
    pikkus = int(input("Palun sisestage enda pikkus (Sentimeeter)\n: "))
    kaal = float(input("Palun sisestage oma kaal (KG)\n: "))
    vanus = float(input("Mis on teie vanus\n: "))

    daily = Kalorid(pikkus, kaal, vanus)
    os.system("cls")
    daily.säilimine()
else:
    quit