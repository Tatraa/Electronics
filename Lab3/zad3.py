import matplotlib.pyplot as plt
import numpy as np

tep_f_gran = 11901

freq = [10,20,100,200,500,1000,10000,15000,30000,50000,80000]
u2_u1 = [10.97, 10.94,11.29,11.29,10.77,10.77,10.62,10.15,7.13,4.23,3.11]
phase_diff = [178,178,179,178,178,179,169,154,124,108,99]
fig, ax = plt.subplots()
# plt.scatter(freq, u2_u1)
plt.scatter(freq, phase_diff)
# ax.plot(freq, u2_u1)
ax.plot(freq, phase_diff)
ax.set_xscale('log')
# ax.axvline(x=tep_f_gran, color='red', linestyle='--', label='Częstotliwość rezonansowa')
ax.set_xlabel('Częstotliwość (Hz)')
ax.set_ylabel('Phase')
ax.set_title('Przesunięcie fazowe vs częstotliwość')
ax.legend()
plt.show()