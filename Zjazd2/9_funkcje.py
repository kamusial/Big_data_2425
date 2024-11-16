def przywitanie(imie):
    print(f'Siema {imie}')

def pole_trojkata(a, h):
    pole = a * h / 2
    return pole

def create_mail(name, age):
    if age < 18:
        print('Nie mozna')
        return ''
    else:
        if name[-1] == 'a':
            return 'Ms.'+name+'@.company.com'
        else:
            return 'Mr.'+name+'@.company.com'

mail = create_mail('Kamil', 34)


przywitanie('Kamil')
przywitanie('Monia')
print(pole_trojkata(3, 7))

