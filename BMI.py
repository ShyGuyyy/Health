class BMI:
    
    def __init__(self, pikkus, kaal):
        self.height = pikkus
        self.weight = kaal
        self.calc = round(kaal / pikkus ** 2)
        
    # BMI (alakaalust kuni ülekaaluni)
    def calculation(self):   
        if self.calc < 18.5:
            print(f"Teie BMI on {self.calc}, olete alakaaluline.")
        elif self.calc < 25:
            print(f"Teie BMI on {self.calc}, olete normaalkaalus.")
        elif self.calc < 30:
            print(f"Teie BMI on {self.calc}, olete ülekaaluline.")
        elif self.calc < 35:
            print(f"Teie BMI on {self.calc}, olete rasvunud.")
        else:
            print(f"Teie BMI on {self.calc}, olete kliiniliselt rasvunud.")