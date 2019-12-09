a = ['a', 'b', 'c', 'd']
#1
print(int('3'*2)//11) # =3

#2
a.insert(0, 'x')

#3
a = a[:-2]

#4
a.sort(reverse=True)

#5
b = a[2:]

#6

a = ['apples', 'bananas', 'oranges']
a.insert(-1, 'and')
b = ', '.join(a)
b = b.replace('and,', 'and')

#7

a = {'scaune': 2, 'mese': 5}
print(f"Items: {', '.join(a.keys())}")
print(f'Suma: {sum(a.values())}')

