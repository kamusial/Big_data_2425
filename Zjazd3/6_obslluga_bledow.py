try:
    a = int(input('Podaj dzielną:   '))
    b = int(input('Podaj dzielnik:   '))
    result = a / b
    print('piesek'[6])
except ValueError:
    print('Nie da się przeksztalcic danej wejsciowej na int')
except IndexError:
    print('Za daleko w indeksach')
except ZeroDivisionError:
    print('dzielnik jest 0')
    raise



print('Dalej')