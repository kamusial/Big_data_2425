# 1. Odczyt pliku CSV z zapisem poszczególnych pól


with open('../rozliczenie.csv', 'r') as file1:
    # content = file1.read()
    # print(content)
    # content = file1.read(5)
    # print(content)
    # content = file1.read(5)
    # print(content)
    # content = file1.read(5)
    # print(content)
    # content = file1.readline()
    # print(content)
    # content = file1.readline()
    # print(content)
    # content = file1.readline()
    # print(content)
    content = file1.readlines()
print(content)

# podział na linie
for i in range(len(content)):
    print('przed:',content[i])
    content[i] = content[i].split(',') # rozdziamy linie względem przecinków
    print('po:',content[i])

print(content)
print(content[5])   # wszystko
print(content[5][2])  # jeden wiersz
print(content[0][2])  # jedno pole
print(content[0][2][3:10])  # kawałek pola
print('koniec części pierwszej\n')

# 2. Oblicz średnią wypłatę
total = 0
licznik = 0
for i in range(1, len(content)): #cała bez pierwszej linii
    print(content[i][1])
#    content[i][1] = int(content[i][1])  # zamień na liczbę
    total += int(content[i][1])
    if int(content[i][1]) > 4000:
        licznik += 1    # licz ile osób zarabia ponad 4k
print('suma wyplat to:', total)
print('średnia wypłata wynosi', total / (len(content)-1))
# print('Liczba kolumn',len(content[2]))

# 3. Ile kobiet jest na macierzyńskim?
macierzynski = 0
for i in range(1, len(content)):
    if content[i][3] == 'k':
        content[i][4] = content[i][4].replace('\n','')
        if content[i][4][0].lower() == 't':
            macierzynski += 1
print('liczba Pań na macierzynskim: ',macierzynski)

# 4. Ile najwięcej kolumn mają linie
max_kolumn = 0
index = -1
for i in range(len(content)):
    if len(content[i]) > max_kolumn:
        max_kolumn = len(content[i])
        index = i
print('max', max_kolumn, 'kolumn w linii', index+1)