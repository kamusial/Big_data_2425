print('a')
print("a")

a = 5
print(a)
print(type(a))
b = 7.5
print(type(b))
napis = 'piesek'
print('napis')
print(napis)
print(type(napis))
slowo = 'kotek'

print(a + b)
print(a*b)
# print(a + napis)
print(a*napis)
# print(b*slowo)
print(slowo + napis)

wiek = int(input('Podaj wiek:   '))

if wiek < 18:
    print('Masz',wiek,'lat')
    print('Będziesz pełnoletni za',18 - wiek,'lat')
    print('I tyle')
else:
    print('jeste już pełnoletni')
    print('rob co chcesz')
print('koniec programu')

correct_password = 1234
password = int(input('Podaj haslo:   '))
if password != correct_password:
    print('Zle haslo, brak dostepu:    ')
else:
    print('Poprawne haslo')
    print('Wejscie do systemu')
print('dalsza czesc programu')



# program, który pyta o zarobki, liczbę dzieci i zwierząt
# dziecko 800+, zwierze kosztuje 300zł.
# ile pienięzy na osobę
# zarobki = float(input('Ile zarabiasz?  '))
# liczba_dzieci = int(input('Ile masz dzieci?   '))
# liczba_zwierzat = int(input('Ile masz zwierzat?   '))
# suma_pieniedzy = zarobki + liczba_dzieci * 800 - liczba_zwierzat * 300
# pieniadze_na_glowe = suma_pieniedzy / (liczba_dzieci + 2)
# print('Macie ',pieniadze_na_glowe,'na osobe')


