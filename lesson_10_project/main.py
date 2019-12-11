from my_folder import base, bird, fish, mammal, reptile

#Creating animal objects and adding them in list
animal_1 = mammal.Mammal("Foxie", 7)
animal_2 = reptile.Reptile("Felix", 2, 13, 'green')
animal_3 = mammal.Mammal("Harlie", 16)
#Searching of all the animals of a class
base.Zoo.db_search("Mammal")
base.Zoo.db_count()