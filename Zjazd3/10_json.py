# Prosty obiekt zawierający dane o osobie
file1 = {
  "imie": "Jan",
  "nazwisko": "Kowalski",
  "wiek": 30
}
print(f'Imię to: {file1["imie"]}')


# Obiekt zawierający listę produktów
file2 = {
  "nazwa_sklepu": "Sklep Komputerowy",
  "adres": {
    "ulica": "Długa",
    "numer": 10,
    "miasto": "Warszawa"
  },
  "produkty": [
    {
      "nazwa": "Laptop",
      "cena": 3999.99,
      "kategoria": "Elektronika"
    },
    {
      "nazwa": "Mysz bezprzewodowa",
      "cena": 79.99,
      "kategoria": "Akcesoria"
    }
  ]
}
