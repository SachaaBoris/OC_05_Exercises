class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        """Affiche les détails de la personne (nom et âge)."""
        print(f"Nom : {self.name}")
        print(f"Âge : {self.age}")


class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)  # Appelle le constructeur de la classe Person
        self.salary = salary

    def show_details(self):
        """Affiche les détails de l'employé (nom, âge et salaire)."""
        super().show_details()  # Appelle la méthode show_details de Person
        print(f"salary : {self.salary}")


# Test des classes
people = [("Alice", 30), ("Denis", 24), ("Marc", 41), ("Christopher", 19)]
employees = [("Bob", 40, 50000), ("Paul", 38, 48000), ("Vincent", 43, 52000)]

for persona in people:
    person = Person(*persona)
    person.show_details()
    print()

for persona in employees:
    employee = Employee(*persona)
    employee.show_details()
    print()