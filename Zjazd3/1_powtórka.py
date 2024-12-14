print('Siema')

input()

age = int(input('Ile masz lat?  '))

if 0 < age < 18:
# if age < 0 and age > 18:
    print(f'Wiec masz {age} lat')
    print(f'Będziesz dorosły za {18 - age} lat')
else:
    print('zły wiek')
