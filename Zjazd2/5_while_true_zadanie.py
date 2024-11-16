import random

# program losuje liczbe
# uzytkownik zgaduje tę liczbę
# program informuje, czy za dużo, czy za mało, czy ok

liczba = random.randint(0, 100)
while True:
    liczba_uzytkownika = int(input('Podaj liczbe:  '))
    if liczba_uzytkownika == 9999:
        print('Tryb tajny')
        passwd = input('Wpisz haslo:  ')
        if passwd == 'Merito':
            break
    elif liczba_uzytkownika > liczba:
        print('Za duzo')
    elif liczba_uzytkownika < liczba:
        print('Za malo')
    else:
        print('Ok')
        break