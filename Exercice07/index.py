def square(n):
    # Vérifier si n est un int ou un float
    if isinstance(n, (int, float)):
        return n ** 2
    else:
        print("Le paramètre doit être un nombre !")
        return None

print(square(8))     # Devrait retourner 64
print(square(12.3))  # Devrait retourner 151.29
print(square("Z"))   # Devrait afficher un message d'erreur et retourner None