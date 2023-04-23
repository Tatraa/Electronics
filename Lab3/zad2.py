import matplotlib.pyplot as plt
import numpy as np

tep_f_gran = 5273

freq = [10,100,200,500,1000,6000,10000,30000,50000,100000,150000]
u2_u1 = [0.008,0.084,0.175,0.396,0.667,0.959,0.938,0.771,0.542,0.171,0.075]
# phase_diff = [178,178,179,178,178,179,169,154,124,108,99]
fig, ax = plt.subplots()
plt.scatter(freq, u2_u1)
# plt.scatter(freq, phase_diff)
ax.plot(freq, u2_u1)
# ax.plot(freq, phase_diff)
ax.set_xscale('log')
ax.axvline(tep_f_gran, color="red", label="Teoretyczna częstotliwość rezonansowa")
ax.set_xlabel('Częstotliwość (Hz)')
ax.set_ylabel('U2/U1')
ax.set_title('Amplituda vs częstotliwość')
plt.legend()
plt.show()