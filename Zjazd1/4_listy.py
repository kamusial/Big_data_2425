slowo = 'Margaryna'
print(slowo)
print(slowo[3:5])
print(slowo[-1])  # ostatni znam
print(slowo[-2])  # przed ostatni znak

lista_imion = ['Kamil', 'Ewa', 'Monika', 'Grzegorz']
# wypiszmy osobno imiona męskie i żeńkie

for i in range(len(lista_imion)):
    if lista_imion[i][-1] == 'a':
        print(lista_imion[i], 'to imie żeńkie')
    else:
        print(lista_imion[i], 'to imie męskie')

suma = 0
suma_parzystych = 0
iloczyn = 1
lista_liczb = [3, 65, 43, 7, 54, 12, 13]
for i in range(len(lista_liczb)):
    # suma licz
    #    suma = suma + lista_liczb[i]
    suma += lista_liczb[i]
    # iloczyn liczb
    # iloczyn = iloczyn * lista_liczb[i]
    iloczyn *= lista_liczb[i]
    # suma_parzystych
    if lista_liczb[i] % 2 == 0:   #reszta z dzielenia przez 2
        suma_parzystych += lista_liczb[i]

print('suma wynosi', suma)
print('iloczyn wynosi', iloczyn)



