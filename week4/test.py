import numpy as np
import matplotlib.pyplot as plt

# Constants (SI units)
k = 1.38e-23  # Boltzmann constant
m = 1.67e-27  # Mass of a proton
T = 300       # Temperature in Kelvin

# Energy range
E = np.linspace(0, 10*k*T, 1000)

# Probability density function
p = (2*np.pi*m/(k*T))**(3/2) * (E/(k*T))**(1/2) * np.exp(-E/(k*T))

# Plotting
plt.plot(E/k, p, label='Maxwell-Boltzmann distribution')
plt.xlabel('Energy (kT)')
plt.ylabel('Probability density')
plt.title('Maxwell-Boltzmann energy distribution for an ideal gas at T=300 K')
plt.legend()
plt.show()
