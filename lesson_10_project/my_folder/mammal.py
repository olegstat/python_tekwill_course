from my_folder import base

class Mammal(base.Zoo):
    def __init__(self, name, age, food="Grass", a_class="Mammal"):
        super().__init__(name, age, a_class, food)