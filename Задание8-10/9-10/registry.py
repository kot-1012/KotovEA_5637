from animal import Dog, Cat, Hamster

class AnimalRegistry:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def get_animals_by_birth_date(self):
        return sorted(self.animals, key=lambda x: x.birth_date)
