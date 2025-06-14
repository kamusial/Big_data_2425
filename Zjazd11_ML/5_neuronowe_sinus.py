import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import random

# Określenie zakresu wartości x (od -2π do 2π z krokiem 0.1)
x = np.arange(-4 * np.pi, 4 * np.pi, 0.1)

# Obliczenie wartości funkcji sinus dla każdego x
#y = []

# for number in x:
#     y.append(np.sin(number) * random.uniform(0.8, 1.2))
y = np.array([np.sin(number) * random.uniform(1, 1) for number in x])
#y = np.array(y)


# Tworzenie wykresu
plt.figure(figsize=(10, 5))  # Ustawienie rozmiaru wykresu
plt.scatter(x, y, label='sin(x)', color='blue')  # Narysowanie funkcji sinus

# Dodanie tytułu i etykiet osi
plt.title('Wykres funkcji sinus')
plt.xlabel('x')
plt.ylabel('sin(x)')

# Dodanie siatki i legendy
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()

# Zaznaczenie punktów charakterystycznych (np. miejsca zerowe, maksima, minima)
plt.axhline(0, color='black', linewidth=0.5)  # Oś X
plt.axvline(0, color='black', linewidth=0.5)  # Oś Y

# Zaznaczenie π/2, π, itd. na osi X
plt.xticks(
    ticks=[-2*np.pi, -3*np.pi/2, -np.pi, -np.pi/2, 0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi],
    labels=['-2π', '-3π/2', '-π', '-π/2', '0', 'π/2', 'π', '3π/2', '2π']
)


plt.show()


model = Sequential()
model.add(Dense(1, input_dim=1, activation='linear'))  # Warstwa wejściowa
model.add(Dense(100, activation='relu'))
model.add(Dense(100, activation='linear'))
# model.add(Dense(100, activation='linear'))
# model.add(Dense(100, activation='sigmoid'))
# model.add(Dense(100, activation='relu'))
model.add(Dense(100, activation='linear'))
model.add(Dense(1))  # Warstwa wyjściowa
model.compile(optimizer='adam', loss='mse')

# Reshape danych do 2D (wymagane przez Keras)
x_reshape = x.reshape(-1, 1)
y_reshape = y.reshape(-1, 1)

model.fit(x_reshape, y_reshape, epochs=1000, verbose=2)

y_pred = model.predict(x)
plt.scatter(x, y)
plt.plot(x, y_pred, c='r')

# Dodanie tytułu i etykiet osi
plt.title('Wykres funkcji sinus')
plt.xlabel('x')
plt.ylabel('sin(x)')

# Dodanie siatki i legendy
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()

# Zaznaczenie punktów charakterystycznych (np. miejsca zerowe, maksima, minima)
plt.axhline(0, color='black', linewidth=0.5)  # Oś X
plt.axvline(0, color='black', linewidth=0.5)  # Oś Y

# Zaznaczenie π/2, π, itd. na osi X
plt.xticks(
    ticks=[-2*np.pi, -3*np.pi/2, -np.pi, -np.pi/2, 0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi],
    labels=['-2π', '-3π/2', '-π', '-π/2', '0', 'π/2', 'π', '3π/2', '2π']
)

plt.show()



