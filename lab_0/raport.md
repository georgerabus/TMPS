# 🧾 Zoo Feeding Simulation — SOLID Principles Report

## **S — Single Responsibility Principle**
Each class in the project has **one clear job**:
- `Animal` and its subclasses (`Lion`, `Elephant`, `Monkey`, `Giraffe`) describe how animals eat.  
- `Zoo` manages a collection of animals (adding and listing them).  
- `ZooKeeper` is responsible for feeding the animals.  

This separation keeps the code clean, easy to maintain, and reduces side effects.

```py
class Animal(ABC):
    """Base class for all animals."""
    @abstractmethod
    def eat(self):
        pass


class Lion(Animal):
    def eat(self):
        return "Lion devours the meat"

```

---

## **O — Open/Closed Principle**
The system is **open for extension but closed for modification**.  
To add a new animal, you just create a new subclass of `Animal` (e.g., `Tiger`) and implement the `eat()` method — no need to change existing code in `Zoo` or `ZooKeeper`.  

This allows the zoo to grow without breaking or rewriting older parts.

```py
class Monkey(Animal):
    def eat(self):
        return "Monkey eats some bananas."

class Giraffe(Animal):
    def eat(self):
        return "Giraffe eats leaves."
```

---

## **L — Liskov Substitution Principle**
All `Animal` subclasses can replace the `Animal` base class without breaking functionality.  
For example, the `ZooKeeper` doesn’t need to know what specific animal it’s feeding — it simply calls `eat()` on each.  

Any new animal class will work correctly as long as it follows the same interface.

```py
class Zoo:
    """Manages animals in the zoo."""
    def __init__(self):
        self.animals = []

    def add_animal(self, animal: Animal):
        self.animals.append(animal)
        print(f"Added a {animal.__class__.__name__} to the zoo.")

    def get_animals(self):
        return self.animals

...

    if choice == "1":
        zoo.add_animal(Lion())
    elif choice == "2":
        zoo.add_animal(Elephant())

```

---

## **Example Run (Result Output)**


## --- ZOO MENU ---

    Add Lion

    Add Elephant

    Add Monkey

    Add Giraffe

    Feed all animals

    Exit
    Choose an option: 1
     Added a Lion to the zoo.

Choose an option: 3
Added a Monkey to the zoo.

Choose an option: 5

Zookeeper starts feeding the animals...

Lion: Lion devours the meat ferociously!
Monkey: Monkey joyfully eats some bananas.

All animals are fed!
