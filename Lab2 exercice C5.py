# Données
python_students = {"Sara", "Ali", "Mina", "Noah", "Liya"}
data_students = {"Ali", "Noah", "Yacine", "Mina", "Ruth"}

# 1. Étudiants dans les deux cours (intersection)
both = python_students & data_students

# 2. Étudiants seulement en Python (différence)
only_python = python_students - data_students

# 3. Tous les étudiants (union)
all_students = python_students | data_students

# Affichage
print("Both:", both)
print("Only Python:", only_python)
print("All students:", all_students)

# 4. Nombre total d'étudiants uniques
print("Total unique students:", len(all_students))

# 5. Vérifications
print("Is Sara in Python?", "Sara" in python_students)
print("Is Ruth in both courses?", "Ruth" in both)

# 6. Nouvelle liste avec doublons
new_names = ["Ali", "Ali", "Mina", "Liya", "Liya", "Omar", "Hichem", "Amir"]

# 7. Conversion en set (suppression des doublons)
new_set = set(new_names) # nouveau set

# 8. Noms nouveaux (pas dans python_students)
new_students = new_set - python_students

# 9. Noms déjà présents
already_present = new_set & python_students

# 10. Affichage
print("New set:", new_set)
print("New names:", new_students)
print("Already present:", already_present)