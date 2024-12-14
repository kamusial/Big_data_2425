data = input('Wprowadź daną:   ')
try:
    data = int(data)
    print(f'{data} jest intem\n{type(data)}')
except:
    try:
        data = float(data)
        print(f'{data} jest floatem\n{type(data)}')
    except:
        print(f'{data} jest stringiem\n{type(data)}')

