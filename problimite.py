import numpy as np
from tridiagonal import tridiagonal

def problimite(h, P, Q, R, a, b, alpha, beta):
    N = int(((b - a)/h) - 1)

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
        
        b_vec[i] = -R[i] * h**2
        if i == 0:
            b_vec[i] += (1 + P[0] * h / 2) * alpha
        if i == N - 1:
            b_vec[i] += (1 - P[N - 1] * h / 2) * beta
    
    y_interieur = tridiagonal(D, I, S, b_vec)
    
    y = np.zeros(N + 2)
    y[0] = alpha
    y[1:N + 1] = y_interieur
    y[N + 1] = beta
    
    return y

h = 0.1
a = 0
b = 1
alpha = 3
beta = 4
N = int((b - a) / h) - 1
x = np.linspace(a + h, b - h, N)
P = np.ones(N)
Q = np.zeros(N)
R = np.ones(N)
y = problimite(h, P, Q, R, a, b, alpha, beta)
print(f"Solution y:{y}")