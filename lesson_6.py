#1

def maximum(a,b,c):
    return max(a,b,c)
print(maximum(1,2,3))

#2

b = [1, 2, 3]
def multiply(li):
    print(li)
    a = 1
    for var in li:
        a = a*var
    return a
print(multiply(b))

#3

a = input("Please introduse a text to proceed: ")
def check(a):
    maju = 0
    minu = 0
    for var in a:
        if (var.islower()):
            maju += 1
        elif (var.isupper()):
            minu += 1
    return("Majuscule: {}, Minuscule: {}".format(maju,minu))
print(check(a))

#4

a = [1,2,2,3]
def eliminate_dublicates(a):
    a = list(dict.fromkeys(a))
    return(a)
print(eliminate_dublicates(a))

#5

def prim(a):
    if a > 1:
        if a % 2 != 0:
            return("Numarul este prim!")
        elif a == 2:
            return("Numarul este prim!")
        else:
            return("Numarul nu este prim.")
    else:
        return("Numarul nu este prim.")
print(prim(2))

#6

def fibonacci(n):
    a, b = 0, 1
    result = []
    while len(result) < n:
        result.append(a)
        a, b = b, a+b
    return result
print(fibonacci(10))

#7

import re
def validator(a):
    if re.search(r'\w+[.|\w]\w+@\w+[.]\w+[.|\w+]\w+',a):
        return("OK")
    else:
        return("Nope")
print(validator("email@hi.com"))

#8

text = input("Please enter a text with a number: ")
def convert(a):
    while True:
        try:
            print("Converting was successful. Your number is: ", int(a))
            break
        except:
            a = input("Text has a letter. Please try again: ")
convert(text)

