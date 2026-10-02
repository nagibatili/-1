class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        return f"{self.name} ест."

    def sleep(self):
        return f"{self.name} спит."

    def __str__(self):
        return f"{type(self).__name__}: имя={self.name}, возраст={self.age}"


class Bird(Animal):
    def fly(self):
        return f"{self.name} летит."


class Fish(Animal):
    def swim(self):
        return f"{self.name} плывёт."


class Mammal(Animal):
    def walk(self):
        return f"{self.name} ходит."


if __name__ == "__main__":
    animals = [
        Bird("Ворона", 3),
        Fish("Карп", 1),
        Mammal("Слон", 12),
    ]

    for animal in animals:
        print(animal)
        print(animal.eat())
        print(animal.sleep())
        for method in ("fly", "swim", "walk"):
            if hasattr(animal, method):
                print(getattr(animal, method)())
        print("-" * 40)