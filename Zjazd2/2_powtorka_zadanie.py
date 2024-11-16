do_kupienia = ['machew', 'chleb', 'maslo', 'mleko']
w_domu = ['miod', 'chleb', 'mleko', 'pomidor', 'sok']

# program napisze co kupic

for produkt in do_kupienia:
    for item in w_domu:
        if produkt == item:
            print(f'Nie kupuj {produkt}')
        else:
            print(f'kup {produkt}')