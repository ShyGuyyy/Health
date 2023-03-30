class Kalorid:

    def __init__(self, pikkus, kaal, vanus):
        self.pikkus = pikkus
        self.kaal = kaal
        self.vanus = vanus
        # Kalorite tarbimise säilitamine(Mees v Naine)
        # self.sugu = str(input('Kui olete mees sisestage "M" ja kui naine siis "N": ')).lower()
        self.bmr = (10 * kaal) + (6.25 * pikkus) - (5 * vanus)

    def säilimine(self):
            return self.bmr