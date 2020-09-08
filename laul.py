class Laul:
"""Klass laul

Klassi omadused (Attributes):
#ealkiri (str) - laulu pealkiri
laulja(str)  - laulu laulja (artist)
"""
    def __init__(self, pealkiri, laulja ):
        self.p = pealkiri
        self.l = laulja


laul_test  = Laul("Für Oksana", "Nublu")
print(laul_test.l, laul_test.p)
