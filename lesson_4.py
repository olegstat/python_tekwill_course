#1

sum = 0
for var in range(100):
  if var % 2 == 0:
    sum += var
print("Suma numerelor pare mai mici decit 100 este: {}".format(sum))

#2

print("Welcome to the temperature converter app.")
measures = ["C", "F"]
while type not in measures:
  type = input("Please, enter the temperature measure type (C/F): ")
  type = type.upper()
  if type not in measures:
    print("Incorrect input! You should type C for celcius, or F for Fahrenheit")
  else:
    break
if type == "C":
  while True:
    try:
      temp = float(input("You chose converting from Celsius to Fahrenheit. Please enter the number to convert: "))
      break
    except:
      print("You must enter a number! Please try again!")
  conv_temp = (temp*(9/5)+32)
else:
  while True:
    try:
        temp = float(input("You chose converting from Fahrenheit to Celsius. Please enter the number to convert: "))
        break
    except:
      print("You must enter a number! Please try again!")
  conv_temp = (temp-32)*(5/9)
print("{} F will be {} C".format(round(temp,1),round(conv_temp,1)))

#3

print("Welcome to the palindrome checker app!")
word = input("Please enter a word to check: ")
if word == word[::-1]:
  print("Yeah, the word {} is palindrome!".format(word))
else:
  print("Nope, the word {} is not palindrome".format(word))

#4

while True:
    try:
        a = int(input("Пожалуйста, введите число: "))
        break
    except:
        print("Вы должны ввести число, чтобы продолжить!")
answer = list()
for var in range(1, a+1):
    if a % var == 0:
        answer.append(var)
print("Делители числа {}: ".format(a), answer)

#5

a = 0
for i in range(1000,2301):
    if i % 5 == 0:
        a +=i
    elif i % 7 == 0:
        a +=i
    else:
        pass
print(a)

#6

while True:
    try:
        numb = int(input("Пожалуйста, введите целое число больше нуля: "))
        break
    except:
        print("Вы должны ввести число больше нуля!")
dict_num = dict({})
for i in range(1,numb+1):
    dict_num[i] = i**2
print(dict_num)

#7

text = str(input("Please, enter your text: "))
print(len(text) - text.count(" "))

#8

import re
password = input("Please enter your password: ")
if not re.match(r"[}{@'}]", password):
    print("Your password should not contain one of these chars: }{@'")
else:
    if re.match(r'[A-Za-z0-9!/#]{6,}', password):
        print("Your password is OK!")
    else:
        print("Your password should contain at least one a-z, one A-Z, one 0-9, one of ! or / or # and be at least 6 characters long to proceed!")

#9

sentence = input("Please enter your sentence: ")
word = input("Please enter the word to count: ")
sentence = sentence.lower()
result = sentence.split()
word = word.lower()
print("The number of word '{}' in the sentence is: {}".format(word,sentence.count(word)))

#10

sentence = input("Please enter your sentence: ")
splitting = sentence.split()
splitting = list(dict.fromkeys(splitting))
print(" ".join(splitting))