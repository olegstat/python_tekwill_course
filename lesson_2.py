#homework Statnii Oleg

#1.
a_1 = "12"
print("Answer for 1st question is: {}".format(a_1))

#2.
a_2 = "In padurea cu alune aveau casa" + " " + str(2) + " " + "pitici"
print("Answer for 2nd question is: {}".format(a_2))

#3.
print("Please enter the input for the 3rd question below.")
nume = input("Please enter the name: ")
prenume = input("Please enter the surname: ")
virsta = input("Please enter the age: ")
ocupatia = input("Please enter the activity: ")
print("This is tne answer for 3rd question: My name is {} {}. I'm {}. My ocupation is: {}.".format(nume,prenume,virsta,ocupatia))

#4.
a_4 = 10
print("The answer for 4th question is: {}".format(a_4))

#5.
a_5 = input("Enter the input for 5th question (any string): ")
a_5 += str(1)
print("The answer for 5th question is: {}".format(a_5))

#6.
def cerc():
    """ Aceasta functie acceapta raza unui cerc si calculeaza area lui"""
    pi = 3.1415
    a_6 = int(input("Introduceti raza cercului (Pentru intrebarea 6-a): "))
    a_6 =  pi*(a_6**2)
    print("Aceasta este raspuns pentru intrebarea a 6-a. Area cercului este: {}".format(a_6))
cerc()

#7.
a_7 = input("Please introduce the file name for 7th question: ")
a_7 = a_7.split(".")
print("This is the answer for question 7. The file type of the input you introduced is: {}".format(a_7[1]))