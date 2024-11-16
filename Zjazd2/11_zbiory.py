NFZ = {1234, 3476, 4544, 3423, 3254, 8769, 5436, 2345, 6532, 1243, 6435, 1298, 6732, 7688, 7648, 2345, 2356}
chorzy_rok = set([1234, 3476, 4544, 3423, 3254, 8769, 5436])
chorzy_miesiac = set([1234, 3476, 3098, 4544, 3423])
krzyki = {4544, 3423, 3254, 8769, 5436, 2345, 6532, 1243}
centrum = {7648, 2345, 2356, 3987, 1234, 3476, 3254}
zbior_pusty = set()

# suma = zbior1 | zbior2
# przeciecie = zbior1 & zbior2
# roznica = zbior1 - zbior2
# roznica_symetryczna = zbior1 ^ zbior2

# sprawdźmy, ile osób chorowało w ostatnim roku na krzykach
print(f'\nChorzy w ostatnim roku na krzykach: {chorzy_rok & krzyki}')
print(f'ilość: {len(chorzy_rok & krzyki)}')

# sprawdźmy ile osób z Krzyków chorowało w ostatnim roku
print(f'\nChorzy w ostatnim roku na krzykach: {krzyki & chorzy_rok}')
print(f'ilość: {len(krzyki & chorzy_miesiac)}')

# sprawdźmy, ile osób chorowało w ostatnim miesiącu w centrum
print(f'\nChorzy w ostatnim miesiącu w centrum {centrum & chorzy_miesiac}')
print(f'Ilość {len(centrum & chorzy_miesiac)}')

# sprawdźmy, ile osób mieszka w sumie w centrum i na krzykach
print(f'\nMieszkańcy centrum i krzyków: {krzyki | centrum}')
print(f'Ilosc {len(krzyki | centrum)}')

# sprawdźmy poprawność danych:
print('\nPoprawność danych')

# każdy, kto chorował w ostatnim miesiącu,
# jednocześnie chorował w ostatnim roku
print(f'\nLudzie chorujący w ostatnim miesiącu i NIE chorujący w ostatnim roku {chorzy_miesiac - chorzy_rok}')
print(f'Ilosc {len(chorzy_miesiac - chorzy_rok)}')
if len(chorzy_miesiac - chorzy_rok) == 0:
    print('ok')

# nikt nie powinien mieszkać jendocześnie
# w centrum i na krzykach – jeśli tak, trzeba usunąć
duplikaty = krzyki & centrum
if len(duplikaty) != 0:
    print('\nznaleziono duplikaty - usuwam')
    krzyki = krzyki - duplikaty
if len(krzyki & centrum) == 0:
    print('ok, brak duplikatow')

# każdy: chory, zdrowy, z krzyków i z centrum,
# powinien być w bazie NFZ. Jeśli nie ma, trzeba dopisać

# pesele żeńskie mają ostatnią cyfrę parzystą, męskie – nieparzystą.

# wypiszmy mężczyzn z centrum, którzy NIE byli chorzy w ostatnim roku