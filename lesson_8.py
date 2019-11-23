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

#exercises part 2 (file i/o)

import os

os.mkdir('my_new_folder')
os.chdir('my_new_folder')

with open('exercise.txt', 'w+') as f:
    #age = input("Please enter your age: ")
    f.write(f'Age: {input("Please enter your age: ")}\n')
    f.write(f'Occupation: {input("Please enter your occupation: ")}\n')
    f.write(f'Height: {input("Please enter your height: ")}\n')
    f.close()
with open('exercise.txt') as f:
    content = f.read()
    f.close()
with open('exercise_copy.txt', 'w') as f:
    f.write(content)
    f.close()

