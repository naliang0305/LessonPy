class Pokemon:
    def __init__(self, name, weight, height, food, cp):
        self.__name = name
        self.__weight = weight
        self.__height = height
        self.__food = food
        self.__cp = cp

    def eat(self):
        print(f'The pokemon is eating {self.__food}.')
    def make_noice(self):
        print('The pokemon wow wow wow!')

    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name

    def get_weight(self):
        return self.__weight
    def set_weight(self, weight):
        self.__weight = weight

    def get_height(self):
        return self.__height
    def set_height(self, height):
        self.__height = height

    def get_food(self):
        return self.__food
    def set_food(self, food):
        self.__food = food

class Pikachu(Pokemon):

    def __init__(self, name, weight, height, food, cp):
        super().__init__(name, weight, height, food, cp)

    def eat(self):
        print(f'{self.get_name()} is eating {self.get_food()}. pika')
        """不能直接用name，因為父類別已經private，需透過get"""
    def make_noice(self):
        print(f'{self.get_name()} pika pika chu!')

class Squirtle(Pokemon):

    def __init__(self, name, weight, height, food, cp):
        super().__init__(name, weight, height, food, cp)

    def eat(self):
        print(f'{self.get_name()} is eating {self.get_food()}. jenny jenny!')
    def make_noice(self):
        print(f'{self.get_name()} jenny jenny!')

poke1 = Pokemon('papa', 50, 100, 'apple', 109)
poke2 = Pikachu('PIKA', 48, 90, 'pokefood', 140)
poke3 = Squirtle('JNI',34,79,'pp',129)


ls = [poke1, poke2, poke3]

for item in ls :
    item.make_noice()
