# for i in range(5):
#     print('okrążenie nr',i+1)
#     print('koniec iteracji')

napis = input('Napisz coś: ')
print(napis)
print(napis[0])   # pierwszy znak
print(napis[3])   # czwarty znak
print(napis[3:7]) # napisz od 4 do 7 znaku
print('długość napisu to:', len(napis))

for i in range(len(napis)):
    print('Znak', i+1, 'to', napis[i])
    if napis[i] == 'a':
        print('znalazłem literę a na miejscu', i+1)

for i in range(len(napis)):
    if napis[i] == ' ':
        print('pierwsze słowo to', napis[0:i])

