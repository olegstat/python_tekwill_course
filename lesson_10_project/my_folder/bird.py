from my_folder import base

class Bird(base.Zoo):
    def __init__(self, name, age, a_class="Bird", food="Seeds"):
        super().__init__(name, age, a_class, food)