import os

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __repr__(self):
        return f'"{self.title}" par {self.author} ({self.year})'


class Library:
    def __init__(self):
        self.books = []
        self.borrowed_books = []

    def add_book(self, book):
        """Ajoute un livre à la bibliothèque"""
        self.books.append(book)

    def remove_book(self, book_title):
        """Supprime un livre de la bibliothèque"""
        for book in self.books:
            if book.title == book_title:
                self.books.remove(book)
                return True
        return False

    def borrow_book(self, book_title):
        """Emprunte un livre de la bibliothèque"""
        for book in self.books:
            if book.title == book_title:
                self.books.remove(book)
                self.borrowed_books.append(book)
                return True
        return False

    def return_book(self, book_title):
        """Rend un livre emprunté à la bibliothèque"""
        for book in self.borrowed_books:
            if book.title == book_title:
                self.borrowed_books.remove(book)
                self.books.append(book)
                return True
        return False

    def available_books(self):
        """Renvoie une liste des livres disponibles"""
        return [book.title for book in self.books]

    def borrowed_books_list(self):
        """Renvoie une liste des livres empruntés"""
        return [book.title for book in self.borrowed_books]

    def display_books(self):
        """Affiche les livres disponibles"""
        if self.books:
            print("Livres disponibles :")
            for i, book in enumerate(self.books):
                print(f"{i}. {book}")
        else:
            print("Aucun livre disponible.")

    def display_borrowed_books(self):
        """Affiche les livres empruntés"""
        if self.borrowed_books:
            print("Livres empruntés :")
            for i, book in enumerate(self.borrowed_books):
                print(f"{i}. {book}")
        else:
            print("Aucun livre emprunté.")


def clearscreen():
    os.system('cls' if os.name == 'nt' else 'clear')

initial_books = [
    ("Les Misérables", "Victor Hugo", 1862),
    ("Le Petit Prince", "Antoine de Saint-Exupéry", 1943),
    ("Germinal", "Émile Zola", 1885),
    ("Vingt mille lieues sous les mers", "Jules Verne", 1870),
    ("Les Trois Mousquetaires", "Alexandre Dumas", 1844),
    ("Le Meilleur des Mondes", "Aldous Huxley", 1932),
    ("Fahrenheit 451", "Ray Bradbury", 1953),
    ("Dune", "Frank Herbert", 1965),
    ("Foundation", "Isaac Asimov", 1951),
    ("Les Fleurs du Mal", "Charles Baudelaire", 1857),
    ("Le Lion", "Joseph Kessel", 1958),
    ("Les Fourmis", "Bernard Werber", 1991),
    ("Robinson Crusoé", "Daniel Defoe", 1719),
    ("1984", "George Orwell", 1943),
    ("Croc-Blanc", "Jack London", 1906),
    ("Le Guide du voyageur galactique", "Douglas Adams", 1981)
]

# Création de la bibliothèque
library = Library()

for title, author, year in initial_books:
    library.add_book(Book(title, author, year))

def book_take():
    clearscreen()
    library.display_books()
    book_index = int(input("Entrez le numéro du livre à emprunter : ").strip())
    if 0 <= book_index < len(library.books):
        clearscreen()
        book_title = library.books[book_index].title
        if library.borrow_book(book_title):
            print(f"Le livre '{book_title}' a été emprunté.")
        else:
            print("Le livre n'a pas pu être emprunté.")
        input("Entrée pour continuer ").strip()
    else:
        print("Index du livre invalide.")
        input("Entrée pour continuer ").strip()

def book_back():
    clearscreen()
    library.display_borrowed_books()
    book_index = int(input("Entrez le numéro du livre à rendre : ").strip())
    if 0 <= book_index < len(library.borrowed_books):
        clearscreen()
        book_title = library.borrowed_books[book_index].title
        if library.return_book(book_title):
            print(f"Le livre '{book_title}' a été rendu.")
        else:
            print("Le livre n'a pas pu être rendu.")
        input("Entrée pour continuer ").strip()
    else:
        print("Index de livre invalide.")
        input("Entrée pour continuer ").strip()

while True:
    clearscreen()
    print("Options de la Bibliothèque :")
    print("1. Afficher les livres disponibles")
    print("2. Afficher les livres empruntés")
    print("3. Emprunter un livre")
    print("4. Rendre un livre")
    print("5. Quitter")
    
    choice = input("Choisissez une option (1-5) : ").strip()

    if choice == "1":
        clearscreen()
        library.display_books()
        input("Entrée pour continuer ").strip()
    elif choice == "2":
        clearscreen()
        library.display_borrowed_books()
        input("Entrée pour continuer ").strip()
    elif choice == "3":
        book_take()
    elif choice == "4":
        book_back()
    elif choice == "5":
        break
    else:
        print("Option invalide. Veuillez choisir un numéro entre 1 et 5.")
        input("Entrée pour continuer ").strip()
