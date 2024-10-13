lista_zakupow = ['marchew', 'seler', 'majonez', 'chleb']
print(lista_zakupow)
print(lista_zakupow[2])
print(lista_zakupow[1:3])
print(lista_zakupow[1][0:2])


for i in range(len(lista_zakupow)):
    if len(lista_zakupow[i]) > 5:
        print(lista_zakupow[i])
