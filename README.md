# Lab-9-D-couverte-de-NumPy-cr-ation-et-inspection-de-tableaux

      # Étape 1 : Préparation de l’environnement

<img width="851" height="461" alt="Capture d’écran 2025-12-04 232637" src="https://github.com/user-attachments/assets/7789a2fc-83c8-4e50-9f15-34fedd350025" />

<img width="626" height="442" alt="image" src="https://github.com/user-attachments/assets/2e81c05c-07f5-4087-bfeb-508d6a0d30ff" />

       # Étape 2 : Création de tableaux NumPy

<img width="459" height="212" alt="Capture d’écran 2025-12-05 000145" src="https://github.com/user-attachments/assets/31b0a076-842e-48df-ad72-e4dee2044769" />

         # Étape 3 : Inspection et métadonnées
<img width="386" height="355" alt="Capture d’écran 2025-12-05 001401" src="https://github.com/user-attachments/assets/c55e137f-9d24-463a-bb03-0eccaaeffb72" />
<img width="361" height="375" alt="Capture d’écran 2025-12-05 001540" src="https://github.com/user-attachments/assets/94a748a7-29ca-4cfb-9df1-419859d83ba3" />

          # Étape 4 : Reshape : modifier la forme sans recopie
<img width="596" height="236" alt="Capture d’écran 2025-12-05 001848" src="https://github.com/user-attachments/assets/7f992694-d95d-43b8-a12f-c96a8746b6cc" />

          # Étape 5 : Exploration supplémentaire

<img width="613" height="439" alt="Capture d’écran 2025-12-05 002216" src="https://github.com/user-attachments/assets/fe3017ae-8d80-471a-ba2e-205b4a3ffeda" />

          #  Étape 6 : Evaluation / Questions de réflexion

Voici des réponses simples aux questions  :

1️⃣[0]*6 → liste Python, opérations élément par élément.
np.zeros(6) → tableau NumPy, opérations vectorisées et plus rapide.

2️⃣Parce que par défaut, `linspace` crée un intervalle fermé (borne initiale et finale incluses).
 3️⃣ Impossible car 4×3 = 12 ≠ 9 → ValueError.

4️⃣ Tableau ↔ liste Python / JSON :
Tableau → liste : arr.tolist()
Liste → JSON : json.dumps(liste)
JSON → liste → tableau : np.array(json.loads(json_str))

