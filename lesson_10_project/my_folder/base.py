import datetime
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
    @classmethod
    def db_count(cls):
        print("Total number of animals in the zoo is: ", len(cls.animal_list))