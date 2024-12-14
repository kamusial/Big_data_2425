import pandas as pd
import numpy as np

# df = pd.read_csv('dane\\ndiabetes.csv')
# df = pd.read_csv(r'dane\ndiabetes.csv')   # raw string
df = pd.read_csv(r'C:\Users\vdi-belfer\Desktop\Big_data_2425\Zjazd3\dane\ndiabetes.csv')
print(f'wypisuję wszystko albo i niewszystko:\n{df}')
print(f'wypisuję typ:\ntype(df)')
print(f'ilość danych: {df.shape}\nliczba kolumn: {df.shape[1]}')
print(f'wypisuję tak, jak chcę:\n{df.head(3).to_string()}')  # wypisz WSZYSTKO
print(f'opis danych:\n{df.describe().T.to_string()}')   # T - zamiana wierszy z kolumnami
print(f'ilosc pustych komórek:\n{df.isna().sum()}')

# wszędzie, gdzie są zera lub brak wartości - wpisać średnią (bez zer)

# df['bmi'] += 1000
# df['nowa_testowa'] = df['bmi'] / df['glucose'] - 50 * df.shape[1]
# print(f'opis danych:\n{df.describe().T.to_string()}')
# df['bmi'] = df['bmi'].replace(0, np.NaN)

for col in ['glucose', 'bloodpressure', 'skinthickness', 'insulin',
       'bmi', 'diabetespedigreefunction', 'age']:
    df[col].replace(0, np.NaN, inplace=True)   # usuwamy zera
    mean_ = df[col].mean()    #liczymy średnią
    df[col].replace(np.NaN, mean_, inplace=True)   # wpisujemy srednią tam, gdzie puste pola

print('Po czyszczeniu danych')
print(df.describe().T.to_string())
print(df.isna().sum())    # suma pustych pól

# df.to_csv(r'..\Zjazd2\cukrzyca.csv')
df.to_csv(r'dane_po_obrobce\cukrzyca.csv')
df.to_csv(r'C:\Users\vdi-belfer\Desktop\cukrzyca.csv', sep=';', index=False)


