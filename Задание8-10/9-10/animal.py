class Animal:
    count = 0  # общий счетчик всех животных
    
    def __init__(self, name, birth_date):
        self.name = name
        self.birth_date = birth_date
        self.commands = []
        Animal.count += 1

    def add_command(self, command):
        self.commands.append(command)

    def get_commands(self):
        return self.commands

    @staticmethod
    def get_total_count():
        return Animal.count

class Dog(Animal):
    pass

class Cat(Animal):
    pass

class Hamster(Animal):
    pass
