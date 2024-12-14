print('Siema')

while True:
    age = int(input('Ile masz lat?  '))
    if 0 < age < 18:
        print(f'Wiec masz {age} lat')
        print(f'Będziesz dorosły za {18 - age} lat')
        break
    else:
        print('zły wiek, jeszcze raz')

print('Dalsza część programu')