import time
import random
from abc import ABC, abstractmethod

# --- S: Single Responsibility ---
# Each class has a single job.

class Animal(ABC):
    """Base class for all animals."""
    @abstractmethod
    def eat(self):
        pass


class Lion(Animal):
    def eat(self):
        return "Lion devours the meat"


class Elephant(Animal):
    def eat(self):
        return "Elephant munches on leaves."


class Monkey(Animal):
    def eat(self):
        return "Monkey eats some bananas."

# --- O: Open/Closed ---
# You can easily add more animals by subclassing Animal.

class Giraffe(Animal):
    def eat(self):
        return "Giraffe eats leaves."


# --- L: Liskov Substitution ---
# ZooKeeper can interact with any Animal subclass safely.

class Zoo:
    """Manages animals in the zoo."""
    def __init__(self):
        self.animals = []

    def add_animal(self, animal: Animal):
        self.animals.append(animal)
        print(f"Added a {animal.__class__.__name__} to the zoo.")

    def get_animals(self):
        return self.animals


class ZooKeeper:
    """Feeds all animals in the zoo."""
    # def __init__(self, name):
    #     self.name = name

    def feed_animals(self, zoo: Zoo):
        animals = zoo.get_animals()
        if not animals:
            print("The zoo is empty. Nothing to feed!")
            return

        print(f"\nZookeeper starts feeding the animals...\n")
        for animal in animals:
            print(f"{animal.__class__.__name__}: {animal.eat()}")
        print("\nAll animals are fed!\n")


# --- Simulation / Interaction ---

def main():
    zoo = Zoo()
    keeper = ZooKeeper()

    while True:
        print("\n--- ZOO MENU ---")
        print("1. Add Lion")
        print("2. Add Elephant")
        print("3. Add Monkey")
        print("4. Add Giraffe")
        print("5. Feed all animals")
        print("6. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            zoo.add_animal(Lion())
        elif choice == "2":
            zoo.add_animal(Elephant())
        elif choice == "3":
            zoo.add_animal(Monkey())
        elif choice == "4":
            zoo.add_animal(Giraffe())
        elif choice == "5":
            keeper.feed_animals(zoo)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
