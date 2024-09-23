
class Planeta:
    def __init__(self, poradi, nazev):
        self.poradi = poradi
        self.nazev = nazev

    def info(self):
        return f"Toto je {self.nazev} a je {self.poradi}. od Slunce"


zeme = Planeta(3, 'Země')
mars = Planeta(4, 'Mars')


print(zeme.info())
print(mars.info())
