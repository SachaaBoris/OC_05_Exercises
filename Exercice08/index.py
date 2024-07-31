def log_decorator(func):
    """
    Affiche un message avant et après l'exécution de la fonction décorée.
    
    Parameters:
    func (function): La fonction à décorer.
    
    Returns:
    function: La fonction décorée avec le comportement supplémentaire.
    """
    def wrapper():
        print("Avant l'exécution de la fonction.")
        func()
        print("Après l'exécution de la fonction.")
    return wrapper

@log_decorator
def function_test():
    print("Cette fonction ne prend pas d'arguments.")

function_test()
