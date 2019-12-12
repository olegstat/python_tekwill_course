#1

import datetime
d = datetime.date(2019,10,29)
end_date = d + datetime.timedelta(weeks=15) + datetime.timedelta(days=8)
print(end_date)

#2

import random

number = random.randint(1, 100)
count = 0
while number != answer:
  while True:
    try:
      answer = int(input("Guess the number from 1 to 100: "))
      count +=1
      break
    except:
      print("Your input should be a number!")
  if number > answer:
    print("Wrong! Correct number is bigger.")
  elif number < answer:
    print("Wrong! Correct number is smaller.")
  else:
    print("Correct! You tried {} times.".format(count))

#3

from urllib.request import urlopen

response = urlopen("https://999.md/ru/")
for line in response:
  content = (line.decode("utf-8"), '\n')
content = str(content)
print(content.count('Apple'))
