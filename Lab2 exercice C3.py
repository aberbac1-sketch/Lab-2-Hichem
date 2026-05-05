# Données
students = [
    {"name": "Sara", "track": "Python", "score": 85},
    {"name": "Ali", "track": "Data", "score": 72},
    {"name": "Mina", "track": "Python", "score": 91},
    {"name": "Noah", "track": "Web", "score": 64},
    {"name": "Liya", "track": "Python", "score": 78},
    {"name": "Amir", "track": "Web", "score": 99},
    {"name": "Amira", "track": "Python", "score": 88},
    {"name": "Hichem", "track": "Web", "score": 68}
]

# 1. Noms des étudiants en Python
print("Students in Python track:") # noms des étudiants inscrits dans la filière Python
for student in students:
    if student["track"] == "Python":
        print(student["name"])

# 2. Moyenne des scores
total = 0
for student in students:
    total += student["score"]

average = total / len(students)
print("\nAverage score:", average)

# 3. Étudiant avec le meilleur score
best_student = students[0]

for student in students:
    if student["score"] > best_student["score"]:
        best_student = student

print("\nTop student:", best_student["name"], "-", best_student["score"])

# 4. Comptage par filière (track)
track_count = {}

for student in students:
    track = student["track"]
    if track in track_count:
        track_count[track] += 1
    else:
        track_count[track] = 1

print("\nStudents per track:", track_count)