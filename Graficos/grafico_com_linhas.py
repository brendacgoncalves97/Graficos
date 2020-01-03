# -*- coding: utf-8 -*-

# Importação da biblioteca
import matplotlib.pyplot as plt

x = [1, 2, 5]
y = [2, 3, 7]

# Título
plt.title("Meu primeiro gráfico com python")

# Eixos
plt.xlabel("X")
plt.ylabel("Y")

plt.plot(x, y)
plt.show()