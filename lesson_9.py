#1

from datetime import date
class Car:
    def __init__(self, year, fuel, c_type, color):
        self.year = year
        self.fuel = fuel
        self.type = c_type
        self.color = color
    def fuel_type(self):
        return self.fuel
    def car_age(self):
        return date.today().year - self.year
    def set_color(self, new_color):
        self.color = new_color

#2

class Student():
    count = 0
    total = 0
    def __init__(self, grade):
        self.grade = grade
        Student.count +=1
        Student.total += grade
    @classmethod
    def get_count(cls):
        return f"Average grade for all students is: {cls.total / cls.count}"

#3

class Car():
    diesel_count = 0
    electric_count = 0
    def __init__(self, color, age, fuel="N/A"):
        self.color = color
        self.age = age
        self.fuel = fuel
    @classmethod
    def show_diesel(cls):
        return cls.diesel_count
    @classmethod
    def show_electric(cls):
        return cls.electric_count
class DieselCar(Car):
    def __init__(self, fuel = "diesel"):
        super().__init__(color)
        super().__init__(age)
        self.fuel = fuel
        Car.diesel_count +=1
class ElectricCar(Car):
    def __init__(self, fuel="li-ion battery"):
        super().__init__(color)
        super().__init__(age)
        self.fuel = fuel
        Car.electric_count +=1

#5 Project

import datetime

#Zoo classes
class Zoo():
    animal_list = []
    def __init__(self, name, age, a_class, food):
        self.name = name
        self.age = age
        self.a_class = a_class
        self.food = food
        self.animal_list.append(self.__dict__)
        print(f"Animal {self.name} added to the list")
    def fav_food(self):
        return f"Favourite food is: {self.food}"
    @classmethod
    def age_by_date(cls, date):
        cls.age = datetime.datetime.now() - date
    @classmethod
    def db_search(cls, i):
        result = []
        for var in cls.animal_list:
            if var['a_class'] == i:
                result.append(var)
        if result != []:
            print(f"The list of {var['a_class']}s is:", result)
        else:
            print(f'There are no animals of  type {i} in the list!')
class Mammal(Zoo):
    def __init__(self, name, age, food="Grass", a_class="Mammal"):
        super().__init__(name, age, a_class, food)
class Bird(Zoo):
    def __init__(self, name, age, a_class="Bird", food="Seeds"):
        super().__init__(name, age, a_class, food)
class Fish(Zoo):
    def __init__(self, name, age, a_class="Fish", food="Worms"):
        super().__init__(name, age, a_class, food)
class Reptile(Zoo):
    def __init__(self, name, age, tail, color, a_class="Reptile", food="Insects"):
        super().__init__(name, age, a_class, food)
        self.tail = tail
        self.color = color
    def change_color(self,new_color):
        self.color = new_color
    def change_tail(self, new_tail):
        self.tail = new_tail

#Creating animal objects and adding them in list
animal_1 = Mammal("Foxie", 7)
animal_2 = Reptile("Felix", 2, 13, 'green')
animal_3 = Mammal("Harlie", 16)

#Searching of all the animals of a class
Zoo.db_search("Mammal")