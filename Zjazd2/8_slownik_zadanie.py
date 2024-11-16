zakupy = {'chleb': 4, 'maslo': 1, 'sok': 2, 'jabko': 5}

ceny_lidl = {'chleb': 2.5, 'maslo': 9, 'sok': 4.7, 'jabko': 5, 'kurczak': 9.98}
ceny_aldi = {'chleb': 6, 'maslo': 7, 'sok': 0.99, 'jabko': 7, 'kurczak': 13}
ceny_dino = {'chleb': 4, 'maslo': 4, 'sok': 9.99, 'jabko': 0, 'kurczak': 14}

total_lidl = 0
total_aldi = 0
total_dino = 0
# gdzie najtaniej?
for produkt in zakupy.keys():
    print(produkt)
    print(f'Cena {produkt} w lidlu wynosi: {ceny_lidl[produkt]}')
    total_lidl += ceny_lidl[produkt] * zakupy[produkt]
    total_aldi += ceny_aldi[produkt] * zakupy[produkt]
    total_dino += ceny_dino[produkt] * zakupy[produkt]

print(f'Lidl: {total_lidl}')
print(f'Aldi: {total_aldi}')
print(f'Dino: {total_dino}')



