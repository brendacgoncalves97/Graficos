# -*- coding: utf-8 -*-

# Importação da biblioteca
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 7, 1, 0]
z = [200, 25, 400, 330, 100]
titulo = "Scatterplot: gráfico de dispersão"
eixoX = "Eixo X"
eixoY = "Eixo Y"

# Legendas
plt.title(titulo)
plt.xlabel(eixoX)
plt.ylabel(eixoY)

plt.plot(x, y, color="k", linestyle="--")
plt.scatter(x, y, label="Meus pontos", color="g", marker=".", s=z)
plt.legend()
plt.show()
#plt.savefig("teste.png", dpi=300)