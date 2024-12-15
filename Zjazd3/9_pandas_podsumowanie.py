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

