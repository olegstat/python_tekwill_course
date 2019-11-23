#1

from functools import reduce
a = [1,2,3,4,5,6]
b = reduce(lambda x, y : x+y, filter(lambda x: x % 2 == 0, a))
print(b)

#2

def my_generator(n):
    while n > 0:
        yield n*n
        n -= 1
a = []
for i in my_generator(10):
    a.append(i)
a.sort()
print(a)

#3

l = [1, 2, [3, 4, [5, 6]], 7, 8, [9, [10]]] 
output = [] 
def flatter(n): 
    for i in n: 
        if type(i) == list: 
            flatter(i) 
        else: 
            output.append(i) 
flatter(l) 
print(output) 

#4


