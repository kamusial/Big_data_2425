do_kupienia = ['machew', 'chleb', 'maslo', 'mleko']
w_domu = ['miod', 'chleb', 'mleko', 'pomidor', 'sok']

# program napisze co kupic

for produkt in do_kupienia:
    mam = False
    for item in w_domu:
        if produkt == item:
            mam = True
            print(f'Nie kupuj {produkt}')
    if mam == False:
        print(f'Kup {produkt}')

print('drugie podejscie')
for produkt in do_kupienia:
    if produkt not in w_domu:
        print(f'Kup {produkt}')
