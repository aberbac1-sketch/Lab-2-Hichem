# Donnée
word = "internationalization"

# 1. Construire le dictionnaire des fréquences
count = {}

for ch in word:
    if ch in count:
        count[ch] += 1
    else:
        count[ch] = 1

# 2. Afficher le dictionnaire
print("Frequency dictionary:", count)

# 3. Trouver le caractère le plus fréquent
max_count = max(count.values())
most_chars = []

for ch in count:
    if count[ch] == max_count:
        most_chars.append(ch)

print("Most frequent characters:", most_chars)
print("Frequency:", max_count)

# 4. Nombre de caractères différents
print("Number of distinct characters:", len(count))