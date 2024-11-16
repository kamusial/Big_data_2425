lista_imion = ['Kamil', 'Ewa', 'Monika', 'Grzegorz']
# wypiszmy osobno imiona męskie i żeńkie

for imie in lista_imion:  # imie to kolejne imie
    if imie[-1] == 'a':
        print(imie, 'to imie żeńkie')
    else:
        print(imie, 'to imie męskie')

suma = 0
suma_parzystych = 0
iloczyn = 1
lista_liczb = [3, 65, 43, 7, 54, 12, 13]
for liczba in lista_liczb:
    # suma liczb
    suma += liczba
    # iloczyn liczb
    iloczyn *= liczba
    # suma_parzystych
    if liczba % 2 == 0:   #reszta z dzielenia przez 2
        suma_parzystych += liczba

print('suma wynosi', suma)
print('iloczyn wynosi', iloczyn)



