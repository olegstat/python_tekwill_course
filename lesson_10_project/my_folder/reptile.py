from my_folder import base

class Reptile(base.Zoo):
    def __init__(self, name, age, tail, color, a_class="Reptile", food="Insects"):
        super().__init__(name, age, a_class, food)
        self.tail = tail
        self.color = color
    def change_color(self,new_color):
        self.color = new_color
    def change_tail(self, new_tail):
        self.tail = new_tail