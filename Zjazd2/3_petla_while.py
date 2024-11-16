x = 0
while x < 5:
    print('Wykonuje kod')
    x += 1   # dodaj 1 do X
print('koniec')

passwd = '1234'
user_passwd = input('Podaj haslo: ')
while user_passwd != passwd:
    user_passwd = input('Podaj haslo: ')
print('haslo poprawne')

