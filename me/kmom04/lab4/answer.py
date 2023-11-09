#!/usr/bin/env python3

"""
aa69bd2b249203be8f53d08a69476034
python
lab4
v4
kamt23
2023-09-25 17:36:51
v4.0.0 (2019-03-05)

Generated 2023-09-25 19:36:51 by dbwebb lab-utility v4.0.0 (2019-03-05).
https://github.com/dbwebb-se/lab
"""

from dbwebb import Dbwebb


# pylint: disable=invalid-name

dbwebb = Dbwebb()
dbwebb.ready_to_begin()



# ==========================================================================
# Lab 4 - python
#
# "In these exercises we will take a look into lists."
#



# --------------------------------------------------------------------------
# Section 1. List basics
#
#
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.1 (1 points)
#
# Concatenate the two lists [table, lion] and [desk, wall].
#
# Answer with your list.
#
# Write your code below and put the answer into the variable ANSWER.
#


tab_lion_list = ["table", "lion"]
desk_wall_lsit = ["desk", "wall"]
tldw_list = tab_lion_list + desk_wall_lsit




ANSWER = tldw_list

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.2 (1 points)
#
# Use the list [Dafoe, Sheen, Berenger, Depp, Whitaker].
#
# Add the words 'icecream' and 'donkey' as the second and third element.
#
# Answer with the modified list.
#
# Write your code below and put the answer into the variable ANSWER.
#

name_list = ["Dafoe", "Sheen", "Berenger", "Depp", "Whitaker"]
name_list.insert(1, "icecream")
name_list.insert(2, "donkey")





ANSWER = name_list

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.3 (1 points)
#
# Use the list [Dafoe, Sheen, Berenger, Depp, Whitaker].
#
# Replace the third word with: 'potato'.
#
# Answer with the modified list.
#
# Write your code below and put the answer into the variable ANSWER.
#
name_list = ["Dafoe", "Sheen", "Berenger", "Depp", "Whitaker"]
name_list[2]= "potato"





ANSWER = name_list

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.3", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.4 (1 points)
#
# Sort the list
#
# > [table, wall, desk, chair, floor]
#
# in descending alphabetical order. Answer with the sorted list.
#
# Write your code below and put the answer into the variable ANSWER.
#

to_sort_list = ["table", "wall", "desk", "chair", "floor"]
to_sort_list.sort(reverse=True)

ANSWER = to_sort_list

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.4", ANSWER, True)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.5 (1 points)
#
# Use `remove()` to delete the word:
#
# > 'chair'
#
# from the list:
#
# > [table, wall, desk, chair, floor]
#
# Answer with the modified list.
#
# Write your code below and put the answer into the variable ANSWER.
#


furn_list = ["table", "wall", "desk", "chair", "floor"]
furn_list.remove("chair")



ANSWER = furn_list

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.5", ANSWER, False)

# --------------------------------------------------------------------------
# Section 2. Built-in list functions
#
# Some basic built-in functions.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.1 (1 points)
#
# Use a built-in function to sum all numbers in the list:
#
# > [567, 23, 12, 36, 7]
#
# Answer with the result as an integer.
#
# Write your code below and put the answer into the variable ANSWER.
#

numbers_list = [567, 23, 12, 36, 7]

numlist_sum = sum(numbers_list)


ANSWER = numlist_sum

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.2 (1 points)
#
# Use built-in functions, such as `sum` and `len` to get the average value of
# the list:
#
# > [567, 23, 12, 36, 7]
#
# Answer with the result as a float with at most one decimal.
#
# Write your code below and put the answer into the variable ANSWER.
#

numlist_avrg = numlist_sum /len(numbers_list) 


ANSWER = numlist_avrg

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.3 (1 points)
#
# Use the built-in functions `split()` and `join()` to fix this string:
#
# > "The?snow?is?falling"
#
# into a real sentence, (without '?').
#
# Answer with the fixed string.
#
# Write your code below and put the answer into the variable ANSWER.
#

annoying_string = "The?snow?is?falling"
sub_annoy = annoying_string.split("?")
fixed_str = " ".join(sub_annoy)

print(fixed_str)

ANSWER = str(fixed_str)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.3", ANSWER, True)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.4 (1 points)
#
# Use slice on the list
#
# > [reggae, rock, blues, jazz, opera]
#
# and replace the second and third element with
#
# > "book, candle"
#
# Answer with the modified list.
#
# Write your code below and put the answer into the variable ANSWER.
#

music_types_list = ["reggae", "rock", "blues", "jazz", "opera"]

music_types_list [1:3] = ["book", "candle"]

ANSWER = music_types_list

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.4", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.5 (1 points)
#
# Assign the list
#
# > [b, a, e, d, c]
#
# to a variable called 'list1'.
#
# Assign the list again, but to another variable called 'list2'.
#
# Answer with the result of 'list1 is list2'.
#
# Write your code below and put the answer into the variable ANSWER.
#
list1 = ["b", "a", "e", "d", "c"]
list2 = ["b", "a", "e", "d", "c"]


ANSWER = list1 is list2

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.5", ANSWER, True)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.6 (1 points)
#
# Use your lists from the last exercise. Assign 'list1' to another variable
# called 'list3' like this:
#
# > list3 = list1
#
# Answer with the result of 'list1 is list3'.
#
# Write your code below and put the answer into the variable ANSWER.
#

list3 = list1




ANSWER = list1 is list3

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.6", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.7 (1 points)
#
# Use your lists from the last exercise. Change the first element in 'list1'
# to
#
# > "s"
#
# Answer with 'list3'.
#
# Write your code below and put the answer into the variable ANSWER.
#

list1[0]= "s"
list3 = list1

ANSWER = list3

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.7", ANSWER, False)

# --------------------------------------------------------------------------
# Section 3. Extra assignments
#
# These questions are worth 3 points each. Solve them for extra points.
#

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 3.1 (3 points)
#
# Create a function that returns the list passed as argument sorted in
# numerical and ascending order. Also multiply all values with 10.
#
# Use the list:
#
# > [45, 22, 2, 498, 78]
#
# and the built-in method `sort()`.
#
# Answer with the sorted list.
#
# Write your code below and put the answer into the variable ANSWER.
#

def list_sorter(list_in):
    """
    takes list and sorts it, multiplies values with 10
    Parameter:
    list_in: a list
    return: new list
    """
    list_in.sort()
    sorted_list = []
    multi = 0 
    for e in list_in:
        multi = e * 10
        sorted_list.append(multi)
    return sorted_list


ANSWER = list_sorter([45, 22, 2, 498, 78])

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("3.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 3.2 (3 points)
#
# Create a function that takes the list:
#
# > [567, 23, 12, 36, 7]
#
# as argument.
#
# The function should multiply all even numbers by 2 and add 7 to all odd
# numbers.
#
# Answer with the modified list sorted in numerical order, descending.
#
# Write your code below and put the answer into the variable ANSWER.
#

""" alt solution, omvalnda index innehåll till str och slica, få sista int och kör mod 2
solution, kräver mer tid och kod, men kan fungera!! -Karma
ka = "abcdefghijklmnopqrtuvwxyz"
kalen = len(ka)
print(ka[kalen-1:kalen])  - skriver ut sista char i str -karma

"""

def even__odd_list_calc(num_list):
    """
    takes list, proccess it, multiply evens by 2 and adds 7 to odds
    """
    num_list.sort(reverse =True)
    multi_add_list = []
    multi = 0
    add = 0
    for e in num_list:

        if (e % 10) % 2 == 0:
            multi = e * 2
            multi_add_list.append(multi)
        else:
            add = e + 7
            multi_add_list.append(add)
    return multi_add_list



ANSWER = even__odd_list_calc([567, 23, 12, 36, 7])


# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("3.2", ANSWER, False)


dbwebb.exit_with_summary()
