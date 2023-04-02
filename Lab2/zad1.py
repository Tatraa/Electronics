import matplotlib.pyplot as plt
import numpy as np

tep_f_gran = 11901

freq = [30, 50, 80, 120, 240, 500, 1000, 5000, 50000, 1000000]
u1 = [1.96, 1.96, 1.96, 1.96, 1.96, 1.96, 1.96, 1.96, 1.96, 1.96]
u2 = [0.048, 0.084, 0.134, 0.402, 0.780, 1.290, 1.690, 1.910, 1.940, 1.940]
u2_u1 = [0.024, 0.043, 0.068, 0.205, 0.398, 0.658, 0.862, 0.974, 0.990, 0.990]

fig, ax = plt.subplots()
# plt.scatter(freq, u2)
# ax.plot(freq, u2, label='U2')
plt.scatter(freq, u2_u1)
ax.plot(freq, u2_u1, label='U2/U1')
ax.set_xscale('log')
ax.axvline(x=tep_f_gran, color='red', linestyle='--', label='Teoretyczna częstotliwość graniczna')
ax.set_xlabel('Częstotliwość (Hz)')
ax.set_ylabel('Amplituda (V)')
ax.set_title('Amplituda vs częstotliwość')
ax.legend()
plt.show()
