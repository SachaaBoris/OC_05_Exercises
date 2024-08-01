def square(n):
    """
    Renvoie le carré du nombre donné.
    
    Parameters:
    n (int or float): Le nombre à élever au carré.
    
    Returns:
    int or float: Le carré du nombre si n est un int ou float, sinon None.
    """
    try:
        return n ** 2
    except TypeError:
        return None

print(square(8))     # Devrait retourner 64
print(square(12.3))  # Devrait retourner 151.29
print(square("Z"))   # Devrait afficher un message d'erreur et retourner None
