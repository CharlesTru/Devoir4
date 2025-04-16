import numpy as np
import matplotlib.pyplot as plt
from problimite import problimite  # Suppose que cette fonction est fournie

# Solution exacte
def y_exact(x):
    c, d = 0.4, 0.81
    return (c - 0.4 / x**2) - (c - 0.4 / d) * (np.log(x) / np.log(0.9))

# Paramètres
a, b = 0.9, 1.0
alpha, beta = 0.0, 0.0
h_values = [1/30, 1/100]

plt.figure(figsize=(10, 6))
for h in h_values:
    N = int((b - a) / h) - 1
    x_interior = np.linspace(a + h, b - h, N)
    P = -1 / x_interior
    Q = np.zeros(N)
    R = -1.6 / x_interior**4
    y_num = problimite(h, P, Q, R, a, b, alpha, beta)
    x_full = np.linspace(a, b, N + 2)
    plt.plot(x_full, y_num, label=f"Solution numérique (h={h:.3f})")

# Solution exacte
x_exact = np.linspace(a, b, 100)
plt.plot(x_exact, y_exact(x_exact), 'k--', label="Solution exacte")
plt.xlabel("x")
plt.ylabel("y(x)")
plt.title("Comparaison des solutions")
plt.legend()
plt.grid(True)

h_err = [10**-k for k in range(2, 6)]
errors = []

for h in h_err:
    N = int((b - a) / h) - 1
    x_interior = np.linspace(a + h, b - h, N)
    P = -1 / x_interior
    Q = np.zeros(N)
    R = -1.6 / x_interior**4
    y_num = problimite(h, P, Q, R, a, b, alpha, beta)
    x_full = np.linspace(a, b, N + 2)
    y_ex = y_exact(x_full)
    error = np.max(np.abs(y_num[1:-1] - y_ex[1:-1]))
    errors.append(error)

plt.figure(figsize=(8, 6))
plt.loglog(h_err, errors, 'o-', label="Erreur E(h)")
plt.loglog(h_err, [h**2 for h in h_err], 'r--', label="h^2")
plt.xlabel("h")
plt.ylabel("Erreur E(h)")
plt.title("Analyse de l’erreur")
plt.legend()
plt.grid(True)
plt.show()