class BMI:
    
    def __init__(self, pikkus, kaal):
        self.pikkus = pikkus
        self.kaal = kaal
        self.calc = round (kaal / pikkus ** 2)
        
    # BMI (al kaalust kuni ül kaaluni)
    def calculation(self):   
        if self.calc < 18.5:
            print(f"Teie BMI on {self.calc}, olete al kaaluline.")
        elif self.calc < 25:
            print(f"Teie BMI on {self.calc}, olete normaa kaalus.")
        elif self.calc < 30:
            print(f"Teie BMI on {self.calc}, olete ül kaaluline.")
        elif self.calc < 35:
            print(f"Teie BMI on {self.calc}, olete rasvunud.")
        else:
            print(f"Teie BMI on {self.calc}, olete kliiniliselt rasvunud.")