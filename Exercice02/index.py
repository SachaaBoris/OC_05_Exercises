students = {
    'Alice': {
         'Mathematiques': 90,
         'Francais': 80,
         'Histoire': 95
    },
    'Bob': {
         'Mathematiques': 75,
         'Francais': 85,
         'Histoire': 70
    },
     'Charlie': {
         'Mathematiques': 88,
         'Francais': 92,
         'Histoire': 78
     }
}

name = input("Entrez le nom de l'étudiant : ")

if name in students:
    # Afficher les notes de l'étudiant
    print(f"Notes de {name} :")
    total_notes = 0
    nombre_matieres = 0
    for matiere, note in students[name].items():
        print(f"{matiere} : {note}")
        total_notes += note
        nombre_matieres += 1

    # Calculer de la moyenne des notes
    moyenne = total_notes / nombre_matieres
    print(f"Moyenne de {name} : {moyenne:.2f}")  # float à 2 chiffres après la virgule
else:
    # L'étudiant n'existe pas
    print(f"L'étudiant {name} n'existe pas dans la liste.")
