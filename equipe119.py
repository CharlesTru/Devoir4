import numpy as np
import matplotlib.pyplot as plt
from problimite import problimite

def y(x):
    c, d = 0.4, 0.81
    return (c - 0.4 / x**2) - (c - 0.4 / d) * (np.log(x) / np.log(0.9))

a, b = 0.9, 1.0
alpha, beta = 0.0, 0.0
val_h = [1/30, 1/100]

plt.figure(figsize=(10, 6))
for h in val_h:
    N = int((b - a)/h) - 1
    x_interieur = np.linspace(a + h, b - h, N)
    P = 1 / x_interieur
    Q = np.zeros(N)
    R = -1.6 / x_interieur**4
    y_num = problimite(h, P, Q, R, a, b, alpha, beta)
    x_complet = np.linspace(a, b, N + 2)
    plt.plot(x_complet, y_num, label=f"Solution numérique (h={h:.3f})")

x_exacte = np.linspace(a, b, 100)
plt.plot(x_exacte, y(x_exacte), 'k-', label="Solution exacte")
plt.xlabel("x")
plt.ylabel("y(x)")
plt.title("Comparaison des solutions")
plt.legend()
plt.grid(True)

h_err = [10**-2, 10**-3, 10**-4, 10**-5]
erreurs = []

for h in h_err:
    N = int((b - a)/h) - 1
    x_interieur = np.linspace(a + h, b - h, N)
    P = 1 / x_interieur
    Q = np.zeros(N)
    R = -1.6 / x_interieur**4
    y_num = problimite(h, P, Q, R, a, b, alpha, beta)
    x_complet = np.linspace(a, b, N + 2)
    y_sol = y(x_complet)
    erreur = np.max(np.abs(y_num[1:-1] - y_sol[1:-1]))
    erreurs.append(erreur)

plt.figure(figsize=(8, 6))
plt.loglog(h_err, erreurs, 'o-', label="Erreur E(h)")
plt.xlabel("h")
plt.ylabel("Erreur E(h)")
plt.title("Analyse de l’erreur")
plt.legend()
plt.grid(True)
plt.show()