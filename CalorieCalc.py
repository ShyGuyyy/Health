class Kalorid:

    def __init__(self, pikkus, kaal, vanus):
        self.pikkus = pikkus
        self.kaal = kaal
        self.vanus = vanus
        # Kalorite tarbimise säilitamine(Mees v Naine)
        self.sugu = str(input('Kui olete mees sisestage "M" ja kui naine siis "N": ')).lower()
        self.mees = (f"Teie säilituskalorid on {str((10 * kaal) + (6.25 * pikkus) - (5 * vanus) + 5)} Kcal")
        self.naine = (f"Teie säilituskalorid on {str((10 * kaal) + (6.25 * pikkus) - (5 * vanus) - 161)} Kcal")

    def säilimine(self):
        if self.sugu == "m":
            print(self.mees)
        elif self.sugu == "n":
            print(self.naine)