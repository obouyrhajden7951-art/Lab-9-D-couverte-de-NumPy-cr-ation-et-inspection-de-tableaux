import numpy as np

# Tableaux de l'étape 2
tableau_1d = np.array([1, 2, 3, 4, 5])
tableau_2d = np.array([[1, 2, 3],
                       [4, 5, 6]])
zeros = np.zeros((2, 3))
ones = np.ones((3, 2))
progression = np.arange(0, 10, 2)
linspace = np.linspace(0, 1, 5)


def inspect_tableau(tab, nom):
    print(f"=== {nom} ===")
    print(tab)
    print("dtype :", tab.dtype)
    print("ndim  :", tab.ndim)
    print("shape :", tab.shape)
    print("size  :", tab.size)
    print("type(tab) :", type(tab))
    print()


inspect_tableau(tableau_1d, "tableau_1d")
inspect_tableau(tableau_2d, "tableau_2d")
inspect_tableau(zeros, "zeros")
inspect_tableau(ones, "ones")
inspect_tableau(progression, "progression")
inspect_tableau(linspace, "linspace")
