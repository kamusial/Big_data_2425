import pandas as pd

# Wczytanie danych z pliku CSV
df = pd.read_csv('plik.csv')

# Wczytanie z pliku Excel (xlsx)
df_excel = pd.read_excel('plik.xlsx', sheet_name='Arkusz1')

df.head()      # Domyślnie wyświetla 5 pierwszych wierszy
df.head(10)    # Wyświetla 10 pierwszych wierszy

df.tail()      # Domyślnie wyświetla 5 ostatnich wierszy
df.tail(10)    # 10 ostatnich wierszy

df.info()      # Wyświetla liczbę wierszy, kolumn, typy danych oraz liczbę niepustych rekordów w każdej kolumnie

df.describe()  # Opis statyczny

df['nazwa_kolumny']             # Zwraca Series z danej kolumny
df[['kolumna1', 'kolumna2']]    # Zwraca DataFrame z wybranych kolumn

df[df['kolumna'] == 'wartość']
df[df['kolumna'] > 10]
df[(df['kolumna1'] > 5) & (df['kolumna2'] == 'abc')]

df.loc[0:10, ['kolumna1', 'kolumna2']]  # wiersze od 0 do 10, tylko dwie kolumny
df.iloc[0:10, 0:2]                      # wiersze od 0 do 10, kolumny od 0 do 2

df['kolumna_numeryczna'].sum()
df.sum()  # domyślnie wykona sumę dla każdej kolumny numerycznej
df['kolumna'].count()   # Zwraca liczbę niepustych (nie-NaN) wartości w kolumnie
df.count()
df['kolumna_numeryczna'].mean()
df['kolumna_numeryczna'].median()
df['kolumna_numeryczna'].std()
df['kolumna_kategoryczna'].unique()   # Lista unikalnych wartości
df['kolumna_kategoryczna'].nunique()  # Liczba unikalnych wartości

grupa = df.groupby('kolumna_kategoryczna')
grupa['kolumna_numeryczna'].mean()
# Zwraca średnie wartości kolumny numerycznej w podziale na unikalne wartości w kolumnie kategorycznej

df.groupby('kolumna_kategoryczna')['kolumna_numeryczna'].agg(['count', 'mean', 'sum'])

df['nowa_kolumna'] = df['kolumna1'] + df['kolumna2']

df.drop('kolumna_do_usunięcia', axis=1, inplace=True)
# axis=1 oznacza usuwanie kolumn
# inplace=True modyfikuje oryginalnego DataFrame bez tworzenia kopii

df.dropna(inplace=True)
# Usuwa wszystkie wiersze, gdzie znajduje się wartość NaN

df['kolumna'].fillna(0, inplace=True)    # wypełnia braki wartością 0

df.to_csv('nowy_plik.csv', index=False)
df.to_excel('nowy_plik.xlsx', sheet_name='Wyniki', index=False)








