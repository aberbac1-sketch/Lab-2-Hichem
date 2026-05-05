def analyze_scores(scores):
    # Calcul du minimum et du maximum
    lowest = min(scores) # Minimum
    highest = max(scores) # Maximum
    
    # Initialisation
    total = 0
    passed = 0
    
    # Parcours de la liste
    for score in scores:
        total += score
        if score >= 50:
            passed += 1 # Nombre d’admis
    
    # Calcul de la moyenne
    avg = total / len(scores) # Moyenne
    
    # Retour des résultats
    return lowest, highest, avg, passed


# Programme principal
scores = [45, 67, 82, 90, 39, 76, 35, 49, 50, 10]

# Appel de la fonction
lowest, highest, avg, passed = analyze_scores(scores)

# Affichage des résultats
print("Lowest:", lowest) # Minimum
print("Highest:", highest) # Maximum
print("Average:", avg) # Moyenne
print("Passed:", passed) # Nombre d’admis