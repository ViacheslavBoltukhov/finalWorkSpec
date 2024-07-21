class Animals:
    def __init__(self, name, commands=[]):
        self.name = name
        self.commands = commands

    def __str__(self):
        return f'''Меня зовут: {self.name}\nЯ умею: {self.commands}\n'''

    def add_command(self, new_command):
        self.commands.append(new_command)


class PackAnimals(Animals):
    def __init__(self, name, command):
        super().__init__(name, command)


class Horse(PackAnimals):
    def __init__(self, name, command):
        super().__init__(name, command)


class Camel(PackAnimals):
    def __init__(self, name, command):
        super().__init__(name, command)


class Donkey(PackAnimals):
    def __init__(self, name, command):
        super().__init__(name, command)


class Pets(Animals):
    def __init__(self, name, command):
        super().__init__(name, command)


class Dog(Pets):
    def __init__(self, name, command):
        super().__init__(name, command)


class Cat(Pets):
    def __init__(self, name, command):
        super().__init__(name, command)


class Hamster(Pets):
    def __init__(self, name, command):
        super().__init__(name, command)


pet_registry = []


def start():
    while True:
        print(f'''1. Add new animal\n2. Teach command\n3. Get commands\n4. Print the number of animals.\n5. Exit''')
        try:
            n = int(input('Enter number comand: '))
        except Exception as e:
            print('Invalid command number entered')
            continue
        if n == 1:
            print('''Enter animal type:\n1. Dog\n2. Cat\n3. Hamster\n4. Horse\n5. Camel\n6. Donkey''')
            try:
                type_animal = int(input('Enter number type animal: '))
            except Exception as e:
                print('Invalid command number type entered')
                continue
            name = input('Enter animal name: ')
            commands = input('Enter list command separated by a space: ').split()
            if type_animal == 1:
                animal = Dog(name, commands)
            elif type_animal == 2:
                animal = Cat(name, commands)
            elif type_animal == 3:
                animal = Hamster(name, commands)
            elif type_animal == 4:
                animal = Horse(name, commands)
            elif type_animal == 5:
                animal = Camel(name, commands)
            elif type_animal == 2:
                animal = Donkey(name, commands)
            else:
                print('An unacceptable type of animal!')
                continue
            pet_registry.append(animal)
        elif n == 2:
            animal_name = input("Enter animal name: ")
            new_command = input('Enter new command: ')
            for animal in pet_registry:
                if animal.name == animal_name:
                    animal.add_command(new_command)
                    break
            else:
                print("No such animal")
        elif n == 3:
            animal_name = input("Enter animal name: ")
            for animal in pet_registry:
                if animal.name == animal_name:
                    print(animal.commands)
            else:
                print("No such animal")
        elif n == 4:
            print(f'Created by animals: {len(pet_registry)}')
            print('View created animals:\n1. Yes\n2. No')
            look_animals = int(input())
            if look_animals == 1:
                for animal in pet_registry:
                    print(animal)
        elif n == 5:
            break
        else:
            print('The team does not exist')
            continue


start()
