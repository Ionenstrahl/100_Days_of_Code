import random
import pandas
import csv


# 234
# hard way
numbers = [1,2,3]
new_list = []
for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)

# list comprehension way
new_list = [n + 1 for n in numbers]

# strings
name = "Angela"
new_list = [letter for letter in name]

# conditional comprehension
names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
caps_names = [name.upper() for name in names if len(name) >= 5]

# 237
# code challenge - find same ints from files
#with open("file1.txt") as f:
#    list1 = f.read().splitlines()
#with open("file2.txt") as f:
#    list2 = f.readlines()
#result = [int(num) for num in list1 if num in list2]

# 239
student_grades = {student: random.randint(0, 100) for student in names}
passed_students = {student: grade for (student, grade) in student_grades.items() if grade > 60}

# 240
# code challenge count letters
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
words = {word: len(word) for word in sentence.split()}

# 241
# code challenge
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
weather_f = {day: (temp_c * 9/5) + 32 for (day, temp_c) in weather_c.items()}

# 242
student_dict = {
    "student": ["Leo", "Olli", "Jonas"],
    "score": [52, 76, 53]
}
student_df = pandas.DataFrame(student_dict)
#Loop through rows of a data frame
for (index, row) in student_df.iterrows():
    pass
#Looping through dictionaries:
for (key, value) in student_dict.items():
    pass

# 244
# challenge
#with open("nato_phonetic_alphabet.csv") as f:
#    #data = csv.reader(f)
#    data = f.readlines()
df = pandas.read_csv("nato_phonetic_alphabet.csv")
#nato_alphabet = {}
#for (index, row) in df.iterrows():
#    nato_alphabet[row.letter] = row.code
nato_alphabet = {row.letter: row.code for (index, row) in df.iterrows()}


def generate_phoenetic():
    inp = input("Tell me your name, so I'll spell it like the nato! ")
    try:
        out = [nato_alphabet[letter.capitalize()] for letter in inp]
    except KeyError:
        print("Sorry, only letters in the alphabet please. ")
        generate_phoenetic()
    else:
        print(out)


generate_phoenetic()
