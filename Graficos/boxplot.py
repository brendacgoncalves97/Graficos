# Boxplot - diagrama de caixa

import matplotlib.pyplot as plt
import random

vet = []

for i in range(10):
	num_aleatorio = random.randint(0,5)
	vet.append(num_aleatorio)

plt.boxplot(vet)
plt.title("Boxplot")
plt.show()