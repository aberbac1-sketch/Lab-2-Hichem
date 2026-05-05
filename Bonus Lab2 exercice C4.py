# Fonction auxiliaire : calcule les fréquences
def count_characters(word):
    count = {}
    for ch in word:
        if ch in count:
            count[ch] += 1
        else:
            count[ch] = 1
    return count

# Fonction principale
def character_stats(word):
    count = count_characters(word)  # utilisation de la helper function
    
    max_count = max(count.values())
    most_chars = []
    
    for ch in count:
        if count[ch] == max_count:
            most_chars.append(ch)
    
    return count, most_chars, max_count


# Test
word = "internationalization"

freq_dict, most_chars, freq = character_stats(word)

print("Frequency dictionary:", freq_dict)
print("Most frequent characters:", most_chars)
print("Frequency:", freq)
print("Number of distinct characters:", len(freq_dict))