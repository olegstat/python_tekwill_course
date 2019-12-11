from my_folder import base

class Fish(base.Zoo):
    def __init__(self, name, age, a_class="Fish", food="Worms"):
        super().__init__(name, age, a_class, food)