#1

import os

path = '.'
files = os.scandir(path)
total_size = 0
for f in files:
    filename, extension = os.path.splitext(f)
    if  extension == '.py':
        info = f.stat()
        total_size += info.st_size
        total_size = (total_size / 1024) / 1024
    else:
        continue
print('Size in MB:', round(total_size, 5))

#2

import os

path = '.'
files = os.scandir(path)
last_time = {}

for f in files:
    info = f.stat()
    last_time.update({f.name : info.st_mtime})
maximum = max(last_time.values())
for x,y in last_time.items():
    if y == maximum:
        print('Last Modified File:', x)

#3

import os

path = '.'
files = os.scandir(path)
last_time = {}

for f in files:
    info = f.stat()
    last_time.update({f.name : info.st_atime})
maximum = max(last_time.values())
for x,y in last_time.items():
    if y == maximum:
        print('Last Accessed File:', x)

#4,5,6,7

import os

os.mkdir('my_new_folder')
os.chdir('my_new_folder')

with open('exercise.txt', 'w+') as f:
    f.write(f'Age: {input("Please enter your age: ")}\n')
    f.write(f'Occupation: {input("Please enter your occupation: ")}\n')
    f.write(f'Height: {input("Please enter your height: ")}\n')
    f.close()
with open('exercise.txt') as f:
    content = f.read()
    f.close()
with open('exercise_copy.txt', 'w+') as f:
    f.write(content)
    f.close()

    #8

def line_count(file):
    lines = 0
    with open(file, 'r') as f:
        for a in enumerate(f):
            lines += 1
        f.close()
    return lines
output = line_count('test.txt')
print(output)

#9

def word_count(file, word):
    with open(file, 'r') as f:
        text = f.read()
        counting = text.count(word)
        return counting
        f.close()
output = word_count('test.txt', 'line')
print(output)

#10

def add_content(file, content):
    with open(file, 'a') as f:
        f.seek(0, 2)
        content = content + '\n'
        f.write(content)
        f.close()
add_content('test2.txt', 'newline')

#11

def del_file(file, content):
    with open(file, 'r+') as f:
        lines = f.readlines()
        f.seek(0)
        f.close()
    with open(file, 'w') as f:
        content = content + '\n'
        for var in lines:
            if var != content:
                f.write(var)
        f.close()
del_file('test2.txt', 'newline3')

#12_project

def game():
    import random
    c_list = []
    with open('countries.txt', 'r', encoding='utf8') as f:
        for i in f:
            c_list.append(i[:-1])
        f.close()
    c_list[0] = c_list[0][1:]

    c_list_split = []
    for i in c_list:
        c_list_split.append(i.split(','))

    c_dict = dict(c_list_split)

    c_country, c_city = random.choice(list(c_dict.items()))
    capitals = []
    capitals.append(c_city)
    count = 0
    while count < 3:
        capitals.append(random.choice(list(c_dict.values())))
        count +=1
    random.shuffle(capitals)

    print("Guess the capital of {}:\n1. {}\n2. {}\n3. {}\n4. {}".format(c_country,capitals[0],capitals[1],capitals[2],capitals[3]))
    answer = input("Your answer is: ")

    while answer not in capitals:
        answer = input("You should type one of the given answers. Please type EXIT for exit the game, or try again: ")
        if answer == "EXIT":
            break
    if answer == c_city:
        print("Correct!")
    else:
        if answer == "EXIT":
            exit()
        else:
            print("Wrong answer. The correct answer is {}.".format(c_city))

new_game = "YES"
while new_game == "YES":
    game()
    new_game = input("Do you want to start a new game? Type YES. (or anything other to exit the game): ")