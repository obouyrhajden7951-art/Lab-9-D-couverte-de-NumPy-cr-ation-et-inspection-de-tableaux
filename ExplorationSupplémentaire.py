import numpy as np

# Task 5.1 – Types et formats
tableau = np.array([1, 2, 3], dtype=np.float32)
print("Tableau float32 :", tableau, "dtype :", tableau.dtype)

tableau_int = tableau.astype(np.int32)
print("Tableau converti en int32 :", tableau_int, "dtype :", tableau_int.dtype)

print("Mémoire utilisée (bytes) :", tableau.nbytes, "pour float32")
print("Mémoire utilisée (bytes) :", tableau_int.nbytes, "pour int32")
print()

# Task 5.2 – Tableaux utilitaires
matrice_identite = np.eye(4)
print("Matrice identité 4x4 :\n", matrice_identite)

tableau_constant = np.full((2, 2), 7)
print("Tableau constant 2x2 rempli de 7 :\n", tableau_constant)

# Exemple de reshape avec arange
tableau_reshape = np.arange(12).reshape((4, 3))
print("Tableau 4x3 avec arange :\n", tableau_reshape)
print()

# Task 5.3 – Opérations vectorisées
vecteur = np.array([1, 2, 3, 4, 5])
matrice = np.arange(1, 10).reshape((3, 3))

print("Matrice multipliée par 10 :\n", matrice * 10)
print("Racine carrée du vecteur :", np.sqrt(vecteur))
