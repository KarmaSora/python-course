#!/usr/bin/env python3

"""
f60f1c9ce548d1bec995e3ff5b92a0cc
python
lab5
v4
kamt23
2023-09-28 13:15:16
v4.0.0 (2019-03-05)

Generated 2023-09-28 15:15:16 by dbwebb lab-utility v4.0.0 (2019-03-05).
https://github.com/dbwebb-se/lab
"""

from dbwebb import Dbwebb


# pylint: disable=invalid-name

dbwebb = Dbwebb()
dbwebb.ready_to_begin()



# ==========================================================================
# Lab 5 - python
#
# A look into dictionaries and tuples.
#



# --------------------------------------------------------------------------
# Section 1. Dictionaries
#
# Some basics with dictionaries.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.1 (1 points)
#
# Create a small phonebook using a dictionary. Use the names as keys and
# numbers as values.
#
# Use
#
# > Baggins, Aragorn, Smaug
#
# and corresponding numbers
#
# > 55523412, 55564222, 55567894
#
# Add the phonenumbers as integers. Answer with the resulting dictionary.
#
# Write your code below and put the answer into the variable ANSWER.
#
phonebook ={"Baggins": 55523412, "Aragorn": 55564222, "Smaug" : 55567894}

ANSWER = phonebook

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.1", ANSWER, True)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.2 (1 points)
#
# How many items are there in the phonebook dictionary?
#
# Write your code below and put the answer into the variable ANSWER.
#
count=0
for i in enumerate(phonebook):
    count+=1




ANSWER = count

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.3 (1 points)
#
# Use the `get()` method on your phonebook and answer with the phonenumber of
# 'Baggins'.
#
# Write your code below and put the answer into the variable ANSWER.
#






ANSWER = phonebook.get('Baggins')

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.3", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.4 (1 points)
#
# Get all keys from the phonebook dictionary and return them in a sorted
# list.
#
# Write your code below and put the answer into the variable ANSWER.
#

phone_list = []
for i in phonebook:
    phone_list.append(i)
    #print(i)
phone_list.sort()

ANSWER = phone_list

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.4", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.5 (1 points)
#
# Get all values from the phonebook dictionary and return them in a sorted
# list.
#
# Write your code below and put the answer into the variable ANSWER.
#

all_contacts = []
for i in phonebook.values():
    all_contacts.append(i)




ANSWER = all_contacts

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.5", ANSWER, True)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.6 (1 points)
#
# Use the in-operator to test if the name 'Baggins' exists in the phonebook
# dictionary. Answer with the return boolean value.
#
# Write your code below and put the answer into the variable ANSWER.
#



ANSWER = "Baggins" in phonebook

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.6", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.7 (1 points)
#
# Create a copy of the phonebook dictionary.
# Get and remove the item 'Baggins' from the copied phonebook (use pop()).
# Answer with the resulting dictionary.
#
# Write your code below and put the answer into the variable ANSWER.
#



phonebook_copy = phonebook.copy()
phonebook_copy.pop("Baggins")


ANSWER = phonebook_copy


# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.7", ANSWER, False)

# --------------------------------------------------------------------------
# Section 2. Tuples
#
# Some basics with tuples.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.1 (1 points)
#
# Create a tuple with 'frog, 54, 4.77, fridge, 2'. Answer with the length of
# the tuple as an integer.
#
# Write your code below and put the answer into the variable ANSWER.
#

randtuple = ("frog", 54, 4.77, "fridge", 2)
randtuple_len = len(randtuple)




ANSWER =randtuple_len

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.2 (1 points)
#
# Create a tuple out of:
#
# > (frog, 54, 4.77, fridge, 2).
#
# Assign each value in the tuple to different variables:
#
# > 'a','b','c','d','e'.
#
# Answer with the variable: 'd'.
#
# Write your code below and put the answer into the variable ANSWER.
#


frog_fridge_tuple= ("frog", 54, 4.77, "fridge", 2)

a,b,c,d,e = frog_fridge_tuple


ANSWER = d

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.3 (1 points)
#
# Use the list
#
# > [123, 4, 125, 69, 155]
#
# Assign the first two elements to a tuple with a slice on the list.
#
# Answer with the first element in the tuple as an integer.
#
# Write your code below and put the answer into the variable ANSWER.
#

int_list= [123, 4, 125, 69, 155]

lis_tup = (int_list[0],int_list[2])

ANSWER = lis_tup[0]

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.3", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.4 (1 points)
#
# Create a tuple with
#
# > (123, 4, 125, 69, 155)
#
# Convert it to a list and replace the second element with:
#
# > 3741
#
# Convert it back to a tuple and answer with the first three elements in a
# comma-separated string,  without an ending `,`.
#
# Write your code below and put the answer into the variable ANSWER.
#



int_tup = (123, 4, 125, 69, 155)
tup_to_list = []
for i in int_list:
    tup_to_list.append(i)
tup_to_list[1] = 3741
list_to_tup = (tup_to_list)

content_str = ""
count = 0
for i in list_to_tup:
    if count != 3:
        content_str += str(i) +","
        count +=1
content_fixed = content_str[:-1]

ANSWER = content_fixed

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.4", ANSWER, False)

# --------------------------------------------------------------------------
# Section 3. Extra assignments
#
# These questions are worth 3 points each. Solve them for extra points.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 3.1 (3 points)
#
# Use a for-loop to walk through the original phonebook dictionary and create
# a string representing it. Each name and number should be on its own row,
# separated by a space. The names must come in alphabetical order. Note that
# every row should end with a newline character, `\n`.
#
# Answer with the resulting string.
#
# Write your code below and put the answer into the variable ANSWER.
#

row_count = 0
stringfied_phonebook_row =""
phone_list = []
"""
for names in phonebook:
        stringfied_phonebook = names +" " + str(phonebook.get(names)) + "\n"
        stringfied_phonebook_row += stringfied_phonebook
        #print(stringfied_phonebook)
        row_count+=1
""" 

for names in phonebook:
    stringfied_phonebook = names +" " + str(phonebook.get(names)) + "\n"
    #stringfied_phonebook_row += stringfied_phonebook
    phone_list.append(stringfied_phonebook)
    #print(phone_list)
    row_count+=1
phone_list.sort()
stringfied_phonebook_row += "".join(phone_list)

ANSWER = stringfied_phonebook_row

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("3.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 3.2 (3 points)
#
# Convert the phonenumber to a string and add the prefix '+1-', representing
# the language code, to each phone-number.
#
# Answer with the resulting dictionary.
#
# Write your code below and put the answer into the variable ANSWER.
#

for i in phonebook:
    number = phonebook.get(i)
    phonebook.update({i: "+1-"+str(number)})

ANSWER = phonebook

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("3.2", ANSWER, False)


dbwebb.exit_with_summary()
