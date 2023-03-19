import matplotlib.pyplot as plt
import numpy as np

wejsciowe = np.array([1.16, 1.92, 2.92, 3.88, 4.80])

dane_teoretyczne = np.array([0.27, 0.45, 0.69, 0.92, 1.14])
dane_oscyloskop = np.array([0.288, 0.464, 0.712, 0.952, 1.20])

slope, intercept = np.polyfit(wejsciowe, dane_teoretyczne, 1)
ax = plt.subplots()

plt.scatter(wejsciowe, dane_oscyloskop)
plt.plot(wejsciowe, slope*wejsciowe + intercept, 'r')

plt.title("współczynnik Uwyj / Uwej")
plt.xlabel('Napięcie wejściowe')
plt.ylabel('Napięcie wyjściowe')
plt.legend(["Obliczenia oscyloskopu", "Obliczenia Teoretyczne"])

plt.show()
