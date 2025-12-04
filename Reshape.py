import numpy as np

# Task 4.1 – Restructurer un vecteur
vecteur = np.arange(1, 10)  # 1 à 9
print("Vecteur :", vecteur)

# Transformer le vecteur en matrice 3x3
matrice = vecteur.reshape((3, 3))
print("Matrice 3x3 :\n", matrice)

# Vérifier les tailles
print("Shape :", matrice.shape)
print("Size  :", matrice.size)
print()

# Task 4.2 – Dimension déduite automatiquement
matrice_auto = vecteur.reshape((3, -1))  # 3 lignes, colonnes calculées automatiquement
print("Matrice reshape auto (3x?) :\n", matrice_auto)
print("Shape auto :", matrice_auto.shape)

# Exemple d'erreur si dimensions incohérentes
try:
    vecteur.reshape((4, 3))  # Impossible, 9 éléments ne peuvent pas former 4x3
except ValueError as e:
    print("Erreur reshape :", e)
