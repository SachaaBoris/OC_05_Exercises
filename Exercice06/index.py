# Fonction calculate_average
def calculate_average(numbers):
    count = len(numbers)
    if count > 0:
        total = sum(numbers)
        average = total / count
    else:
        return 0
    return average

# Exemple d'utilisation de la fonction
numbers = [10, 20, 30, 40, 50]
average = calculate_average(numbers)
print("La moyenne est :", average)