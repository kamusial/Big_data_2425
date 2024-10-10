import pandas as pd
import os


datasets_dir = os.path.join(os.path.dirname(__file__), "datasets")

# Odczyt wszystkiego
df = pd.read_csv(f"{datasets_dir}/username.csv", sep=";")
print(df.head())


# Odczyt tylko danych kolumn
df = pd.read_csv(f"{datasets_dir}/username.csv", sep=";", usecols=["Username", "Identifier"])
print(df.head())


df = pd.read_csv(f"{datasets_dir}/employment-data.csv")
print(df.head())
