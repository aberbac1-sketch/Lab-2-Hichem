# Liste donnée
numbers = [12, -3, 7, 0, 25, -8, 14, 7, 19, -1, 8, 36, -15, 29, 1, 66, -7]

# Listes vides
positives = [] # nombres positifs
odds = [] # nombres impairs

# Étape 1 : filtrer les nombres positifs et impairs
for n in numbers:
    if n > 0:
        positives.append(n)
    if n % 2 != 0:
        odds.append(n)

# Étape 2 : carrés des nombres positifs
squares = []
for n in positives:
    squares.append(n ** 2)

# Étape 3 : trier les positifs en ordre décroissant
positives_sorted = sorted(positives, reverse=True)

# Étape 4 : deuxième plus grand nombre positif
second_largest = positives_sorted[1]

# Affichage des résultats
print("Positive numbers:", positives) # nombres positifs
print("Odd numbers:", odds) # nombres impairs
print("Squares of positives:", squares) # carrés des nombres positifs
print("Sorted positives (desc):", positives_sorted) # trier les nombres positifs par ordre décroissant
print("Second largest positive:", second_largest) # afficher le deuxième plus grand nombre positif

# Étape 5 : classement (version forte)
print("\nRanking:")
for i, value in enumerate(positives_sorted, start=1):
    print(f"Rank {i}: {value}") # classement