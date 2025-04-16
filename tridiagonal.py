import numpy as np
from scipy.sparse import diags
from scipy.sparse.linalg import spsolve
import time

def tridiagonal(D, I, S, b):

    N = len(D)

    diagonal = [I, D, S]
    offsets = [-1, 0, 1]
    A = diags(diagonal, offsets=offsets, shape=(N, N)).tocsr()
    x = spsolve(A, b)

    return x

n = 15000
# Définition des diagonales
D = 4 * np.ones(n)          # Diagonale principale
I = 1 * np.ones(n - 1)      # Diagonale inférieure
S = 1 * np.ones(n - 1)      # Diagonale supérieure
b = np.ones(n)
    
# Mesure du temps avec matrice sparse
start_time = time.time()
x_sparse = tridiagonal(D, I, S, b)
sparse_time = time.time() - start_time
print(f"Temps avec la matrice sparse : {sparse_time:.4f} secondes")
    
# Comparaison avec une matrice dense
A_dense = np.diag(D) + np.diag(I, -1) + np.diag(S, 1)
start_time = time.time()
x_dense = np.linalg.solve(A_dense, b)
dense_time = time.time() - start_time
print(f"Temps avec la matrice dense : {dense_time:.4f} secondes")

print(f"Différence maximum entre les solutions : {np.max(np.abs(x_sparse - x_dense)):.2e}")