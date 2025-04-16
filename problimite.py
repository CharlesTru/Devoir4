import numpy as np
from tridiagonal import tridiagonal

def problimite(h, P, Q, R, a, b, alpha, beta):
    N = len(P)

    # Construction des trois diagonales
    I = np.zeros(N - 1)
    D = np.zeros(N)
    S = np.zeros(N - 1)
    b_vec = np.zeros(N)

    for i in range(N):
        D[i] = 2 + Q[i] * h**2
        if i > 0:
            I[i - 1] = -1 - P[i] * h / 2
        if i < N - 1:
            S[i] = -1 + P[i] * h / 2
        
        # Second membre
        b_vec[i] = -R[i] * h**2
        if i == 0:
            b_vec[i] += (1 + P[0] * h / 2) * alpha
        if i == N - 1:
            b_vec[i] += (1 - P[N - 1] * h / 2) * beta
    
    # Résolution du système
    y_interior = tridiagonal(D, I, S, b_vec)
    
    # Construction du vecteur
    y = np.zeros(N + 2)
    y[0] = alpha
    y[1:N + 1] = y_interior
    y[N + 1] = beta
    
    return y

#test
h = 0.1
a = 0
b = 1
alpha, beta = 3, 4
N = int((b - a) / h) - 1  # Nombre de noeuds intérieurs
x = np.linspace(a + h, b - h, N)  # Noeuds intérieurs x_1 à x_N
P = np.ones(N)  # Exemple : p(x) = 1
Q = np.zeros(N)  # Exemple : q(x) = 0
R = np.ones(N)   # Exemple : r(x) = 1
y = problimite(h, P, Q, R, a, b, alpha, beta)
print(f"Solution y : {y}")