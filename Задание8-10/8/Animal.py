class Animal:
    def __init__(self, name, birth_date):
        self.name = name
        self.birth_date = birth_date
    
    def make_sound(self):
        pass 
class Pet(Animal):
    def __init__(self, name, birth_date, owner_name):
        super().__init__(name, birth_date)
        self.owner_name = owner_name
        self.trained_commands = []
    
    def perform_trick(self):
        pass 
    
class PackAnimal(Animal):
    def __init__(self, name, birth_date, load_capacity):
        super().__init__(name, birth_date)
        self.load_capacity = load_capacity
        self.distance_covered = 0
    
    def carry_load(self):
        pass
    
class Dog(Pet):
    def __init__(self, name, birth_date, owner_name, breed, favorite_toy):
        super().__init__(name, birth_date, owner_name)
        self.breed = breed
        self.favorite_toy = favorite_toy
    
    def make_sound(self):
        print("Woof!")
        
class Cat(Pet):
    def __init__(self, name, birth_date, owner_name, fur_color, indoor):
        super().__init__(name, birth_date, owner_name)
        self.fur_color = fur_color
        self.indoor = indoor
    
    def make_sound(self):
        print("Meow!")
        
class Hamster(Pet):
    def __init__(self, name, birth_date, owner_name, wheel_size, favorite_food):
        super().__init__(name, birth_date, owner_name)
        self.wheel_size = wheel_size
        self.favorite_food = favorite_food
    
    def make_sound(self):
        print("Squeak!")
        
class Equine(PackAnimal):
    def __init__(self, name, birth_date, load_capacity, breed, shoe_size):
        super().__init__(name, birth_date, load_capacity)
        self.breed = breed
        self.shoe_size = shoe_size
    
    def make_sound(self):
        print("Neigh!")
        
# Создание экземпляра собаки
my_dog = Dog("Buddy", "2018-03-20", "Alice", "Golden Retriever", "Ball")

# Вызов метода make_sound для собаки
my_dog.make_sound()  # Выведет "Woof!"

# Создание экземпляра кошки
my_cat = Cat("Whiskers", "2019-01-10", "Bob", "Gray", True)

# Вызов метода make_sound для кошки
my_cat.make_sound()  # Выведет "Meow!"

# Создание экземпляра лошади
my_horse = Equine("Thunder", "2015-07-05", 500, "Thoroughbred", 4.5)

# Вызов метода make_sound для лошади
my_horse.make_sound()  # Выведет "Neigh!"
