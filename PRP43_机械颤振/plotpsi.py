import numpy as np
import matplotlib.pyplot as plt

# Define the wave function in position space
def psi_x(x, n, lam):
    if -n*lam < x < n*lam:
        return 1/np.sqrt(2*n*lam)*np.exp(2j*np.pi*x/lam)
    else:
        return 0

# Define the wave function in momentum space
def psi_p(p, n, lam):
    return 1/2/np.pi*np.sqrt(lam/n)*np.exp(-1j*p*n*lam/2)*np.sin(p*n*lam/2)/np.sin(p*lam/2)

# Set the parameters
n = 3
lam = 1

# Create the x and p arrays
x = np.linspace(-5, 5, 1000)
p = np.linspace(-10, 10, 1000)

# Calculate the wave function values
psi_x_values = np.array([psi_x(xi, n, lam) for xi in x])
psi_p_values = np.array([psi_p(pi, n, lam) for pi in p])

# Plot the probability densities
plt.figure(figsize=(10, 5))
plt.subplot(121)
plt.plot(x, np.abs(psi_x_values)**2)
plt.xlabel("x")
plt.ylabel("$|\Psi(x, 0)|^2$")
plt.title("Position space")
plt.subplot(122)
plt.plot(p, np.abs(psi_p_values)**2)
plt.xlabel("p")
plt.ylabel("$|\Psi(p, 0)|^2$")
plt.title("Momentum space")
plt.show()
