# 1. Odczyt pliku CSV z zapisem poszczególnych pól


with open('rozliczenie.csv', 'r') as file1:
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








