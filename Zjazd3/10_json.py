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
print(f'nazwa sklepu {file2["nazwa_sklepu"]}')
print(f'Ulica w adresie: {file2["adres"]["ulica"]}')
print(f'Cena myszy {file2["produkty"][1]["cena"]}')
file2["produkty"][0]["stan"] = 'nowy'

nowy_produkt = {
      "nazwa": "monitor",
      "cena": 879.99,
      "kategoria": "Wyswietlanie"
    }

file2["produkty"].append(nowy_produkt)

# JSON zawierający dane o projekcie z uczestnikami i zadaniami
file3 = {
  "projekt": {
    "id": 123,
    "nazwa": "System zarządzania magazynem",
    "status": "w trakcie"
  },
  "uczestnicy": [
    {
      "imie": "Anna",
      "nazwisko": "Nowak",
      "rola": "Project Manager",
      "kontakt": {
        "email": "anna.nowak@example.com",
        "telefon": "+48 123 456 789"
      }
    },
    {
      "imie": "Piotr",
      "nazwisko": "Zieliński",
      "rola": "Developer",
      "kontakt": {
        "email": "piotr.zielinski@example.com"
      }
    }
  ],
  "zadania": [
    {
      "id_zadania": 1,
      "opis": "Analiza wymagań klienta",
      "przypisany_do": "Anna Nowak",
      "status": "zrobione"
    },
    {
      "id_zadania": 2,
      "opis": "Implementacja modułu logowania",
      "przypisany_do": "Piotr Zieliński",
      "status": "w trakcie"
    }
  ]
}
