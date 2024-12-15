import pandas as pd

# wczytanie danych
df = pd.read_json('dane\\dane.json')

# wyświetlanie danych
print("Pierwsze 5 wierszy danych:")
print(df.head())

# filtracja danych
mlodsi_niz_30 = df[df["wiek"] < 30]
print("\nOsoby młodsze niż 30 lat:")
print(mlodsi_niz_30)#

# Dodanie nowej kolumny
df["wiek_za_5_lat"] = df["wiek"] + 5
print("\nDane z dodaną kolumną 'wiek_za_5_lat':")
print(df)

# statystyka
sredni_wiek = df['wiek'].mean()
print(f'\nŚredni wiek: {sredni_wiek}')

# sortowanie
df_sorted = df.sort_values('wiek', ascending=False)
print("\nDane posortowane po wieku malejąco:")
print(df_sorted)

# eksport danych
df.to_json('dane_po_obrobce\\json_deafult.json', indent=4)
df.to_json('dane_po_obrobce\\json_split.json', orient="split", indent=4)
df.to_json('dane_po_obrobce\\json_records.json', orient='records', indent=4)
df.to_json('dane_po_obrobce\\json1_index.json', orient="index", indent=4)
df.to_json('dane_po_obrobce\\json1_columns.json', orient='columns', indent=4)
df.to_json('dane_po_obrobce\\json1_values.json', orient="values", indent=4)
df.to_json('dane_po_obrobce\\json1_table.json', orient='table', indent=4)


