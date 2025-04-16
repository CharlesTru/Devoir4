import numpy as np
from scipy.sparse import diags
from scipy.sparse.linalg import spsolve
import time

def tridiagonal(D, I, S, b):

    N = len(D)
    diago = [I, D, S]
    decalage = [-1, 0, 1]
    A = diags(diago, offsets=decalage, shape=(N, N)).tocsr()
    x = spsolve(A, b)

    return x

n = 15000
D = 4 * np.ones(n)
I = 1 * np.ones(n - 1)
S = 1 * np.ones(n - 1)
b = np.ones(n)

temps_deb_sparse = time.time()
x_sparse = tridiagonal(D, I, S, b)
temps_sparse = time.time() - temps_deb_sparse
print(f"Temps sparse:{temps_sparse} s")

A_complet = np.diag(D) + np.diag(I, -1) + np.diag(S, 1)
temps_deb_complet = time.time()
x_dense = np.linalg.solve(A_complet, b)
temps_complet = time.time() - temps_deb_complet
print(f"Temps complet:{temps_complet} s")