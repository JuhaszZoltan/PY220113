szoveg = input('írj be egy tetszőleges szöveget: ')

szamlalo = 0
for karakter in szoveg:
    if karakter == 'e': szamlalo += 1

print(f'e betűk száma: {szamlalo}')