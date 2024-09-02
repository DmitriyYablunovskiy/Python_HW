
staty = {
    'CZ': 'Česko',
    'SK': 'Slovensko',
    'PL': 'Polsko',
    'DE': 'Německo',
    'AT': 'Rakousko',
}

staty['HU'] = 'Maďarsko'

staty_delka = {}
for kod, nazev in staty.items():
    staty_delka[kod] = len(nazev)

print("Původní slovník staty:", staty)
print("Nový slovník staty_delka:", staty_delka)
