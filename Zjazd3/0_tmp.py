for _ in range(5):
    print('siema')
print()
for i in range(3, 7):
    print(f'siema{i}')

word = 'piesek'
for i in word:
    print(i)

dogs_names = ['Luna', 'Tosia', 'Barley', 'Max']
for dog_name in dogs_names:
    print(f'Imię to: {dog_name}')
    if dog_name[-1] == 'a':
        print(f'Pani {dog_name}')
    else:
        print(f'Pan {dog_name}')
