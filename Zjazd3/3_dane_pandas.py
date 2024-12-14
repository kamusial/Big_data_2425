import pandas as pd

# df = pd.read_csv('dane\\ndiabetes.csv')
# df = pd.read_csv(r'dane\ndiabetes.csv')   # raw string
df = pd.read_csv(r'C:\Users\vdi-belfer\Desktop\Big_data_2425\Zjazd3\dane\ndiabetes.csv')
print(f'wypisuję wszystko albo i niewszystko:\n{df}')
print(f'wypisuję typ:\ntype(df)')
print(f'ilość danych: {df.shape}\nliczba kolumn: {df.shape[1]}')
print(f'wypisuję tak, jak chcę:\n{df.head(3).to_string()}')  # wypisz WSZYSTKO
print(f'opis danych:\n{df.describe().T.to_string()}')   # T - zamiana wierszy z kolumnami
print(f'ilosc pustych komórek:\n{df.isna().sum()}')

