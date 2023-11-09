#!/usr/bin/env python3

"""
4fa123a136728f3ac514b245add7eef3
python
lab2
v4
kamt23
2023-08-31 17:24:02
v4.0.0 (2019-03-05)

Generated 2023-08-31 19:24:02 by dbwebb lab-utility v4.0.0 (2019-03-05).
https://github.com/dbwebb-se/lab
"""

from dbwebb import Dbwebb


# pylint: disable=invalid-name

dbwebb = Dbwebb()
dbwebb.ready_to_begin()



# ==========================================================================
# Lab 2 - python
#
# In this exercise we will look into flow-control. If-statements, for-loops
# and while-loops.
#



# --------------------------------------------------------------------------
# Section 1. Boolean operators and if-statements
#
# The basics of boolean operators and if-statements.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.1 (1 points)
#
# Create three variables representing dice values: `dice1` = 2, `dice2` = 5
# and `dice3` = 5.
#
# Answer with the boolean value of the expression '`dice1` is greater than
# `dice2`'.
#
# Write your code below and put the answer into the variable ANSWER.
#


dice1, dice2, dice3 =  2, 5, 5
dice_value_boolean = dice1 > dice2

ANSWER = dice_value_boolean

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.2 (1 points)
#
# Sum the three variables `dice1`, `dice2` and `dice3`.
#
# Use an if-statement to decide if the sum of the three variables i greater
# than 11. If the sum is greater than 11 answer with 'big' otherwise answer
# with 'small'.
#
# Write your code below and put the answer into the variable ANSWER.
#


sum_of_dices123 = dice1 + dice2 + dice3
big_or_small_string = ""
if sum_of_dices123 > 11:   
    big_or_small_string = "big"
else:   
    big_or_small_string = "small"

ANSWER = big_or_small_string

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.3 (1 points)
#
# Add the sum of `dice4` = 3 and `dice5` = 1 to the sum of the three other
# dices.
#
# Use an if, elseif, else statement to check the total value of the dices.
# Answer with 'small' if the sum is smaller than 11, 'intermediate' if the
# sum is greater than or equal to 11 but smaller than 21. If the sum is
# greater than or equal to 21 answer with 'big'.
#
# Write your code below and put the answer into the variable ANSWER.
#

dice4, dice5 = 3, 1
sum_of_dice_4_and_5 = dice4 + dice5
sum_of_dices_1_to_5 = sum_of_dices123 + sum_of_dice_4_and_5
if sum_of_dices_1_to_5 < 11:
    big_or_small_string = "small"
elif sum_of_dices_1_to_5 < 21:
    big_or_small_string = "intermediate"
else: 
    big_or_small_string = "big"

ANSWER = big_or_small_string

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.3", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.4 (1 points)
#
# Create a variable `summer_word` containing the word 'beach'.
#
# Answer with True if `summer_word` contains the letter 's' otherwise answer
# with False.
#
# Tip: Use the `in` operator.
#
# Write your code below and put the answer into the variable ANSWER.
#

summer_word = "beach"
var = "s" in summer_word


ANSWER = var

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.4", ANSWER, False)

# --------------------------------------------------------------------------
# Section 2. For-loops
#
# The basics of iteration and for-loops.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.1 (1 points)
#
# Loop through the numbers 0 to 10 (10 included) and concatenate a string
# with the numbers comma-separated. You should have a comma at the end of the
# string.
#
# Answer with the string.
#
# Write your code below and put the answer into the variable ANSWER.
#

string_of_num_1_to_10 = ""
for i in range(10 +1):
    string_of_num_1_to_10 += str(i) +","


ANSWER = string_of_num_1_to_10

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.2 (1 points)
#
# Loop through the letters of the variable `summer_word` from above.
# Concatenate the consonants from `summer_word` and answer with the new word.
#
# Tip: Create a string that contains consonants and check if each letter is
# in it.
#
# Write your code below and put the answer into the variable ANSWER.
#

string_of_constants_in_cap_letters = "BCDFGHJKLMNPQRSTVWXYZ"
string_of_constants_in_low_letters ="bcdfghjklmnpqrstvwxyz" 

new_word_of_summer_word_constants = ""
for letter in summer_word :
    if letter in string_of_constants_in_low_letters:
        new_word_of_summer_word_constants += letter
    elif letter in string_of_constants_in_cap_letters:
        new_word_of_summer_word_constants += letter


ANSWER = new_word_of_summer_word_constants

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.3 (1 points)
#
# Loop through all numbers from 50 to 84 both numbers included. Add all odd
# (udda) numbers together and answer with the result.
#
# Tip: Use the modulus % operator.
#
# Write your code below and put the answer into the variable ANSWER.
#

starting_value = 50
ending_value = 84
sum_of_odd_nums = 0
for i in range(starting_value, ending_value +1 ):
    if i % 2 == 1:  
        sum_of_odd_nums += i


ANSWER = sum_of_odd_nums

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.3", ANSWER, False)

# --------------------------------------------------------------------------
# Section 3. While-loops
#
# The basics of while-loops.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 3.1 (1 points)
#
# Create a while-loop that starts at value 3 and ends when the value is
# greater than 25, the value should be incremented by 3 for each iteration.
# Concatenate a string with the values comma-separated. You should have a
# comma at the end of the string.
#
# Answer with the string.
#
# Write your code below and put the answer into the variable ANSWER.
#

number_three = 3
while_loop_string = ""
while number_three < 25:
    while_loop_string += str(number_three) + ","
    # print(number_three)
    number_three += 3


ANSWER = while_loop_string

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("3.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 3.2 (1 points)
#
# Create a while-loop that subtracts 4 from 34, 28 times. Answer with the
# result.
#
# Write your code below and put the answer into the variable ANSWER.
#

loop_counter = 0
number_34 = 34

while loop_counter < 28:
    number_34 -= 4
    loop_counter += 1



ANSWER = number_34

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("3.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 3.3 (1 points)
#
# Create a while-loop that calculates the factorial number for 11, 11!. The
# factorial of a number is the number multiplied by all smaller integers
# greater than 1. The factorial of 11 is `11 * 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3
# * 2 * 1`. Answer with the result.
#
# Write your code below and put the answer into the variable ANSWER.
#

factoral_origin = 11
calculated_factural = 1

while factoral_origin > 0: 
    calculated_factural *= factoral_origin
    factoral_origin -=1

ANSWER = calculated_factural

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("3.3", ANSWER, False)

# --------------------------------------------------------------------------
# Section 4. Extra assignments
#
# These questions are worth 3 points each. Solve them for extra points.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 4.1 (3 points)
#
# Use a for-loop or a while-loop to reverse the word 'internationalization'.
#
# Answer with the reversed word.
#
# Write your code below and put the answer into the variable ANSWER.
#


the_word_is_internationalization = "internationalization"
internationalization_in_reverse = ""

for letter in the_word_is_internationalization:
    internationalization_in_reverse = letter + internationalization_in_reverse

ANSWER = internationalization_in_reverse 

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("4.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 4.2 (3 points)
#
# Swedish numberplates consist of three letters and three numbers (Not using
# new plates which can have more letters). The numbers range from 001 to 999.
# Using one of the four common rules of arithmetics (+, -, *, /), on how many
# of the numberplates can the two first numbers give the third number? We
# only care about the numbers, we ignore letters for this assignment.
#
# Do not count multiple times if more than one rule of arithmetics work.
#
# Examples:
# '123' can be combined to 1 + 2 = 3. So this numberplate is good. Since this
# matched on + operator, we don't continue checking with the other operators.
# '129' 1 and 2 cannot be combined to give 9 using the four rules of
# arithmetics, so this does not work.
#
#
# Answer with the number of numberplates.
#
# Write your code below and put the answer into the variable ANSWER.
#

swedish_letters_count = 29
plate_numbers_range = 999

possible_add_combinations = 0
possible_multi_combinations = 0
possible_div_combinations = 0
possible_sub_combinations = 0


for first_num in range(10):   
    for secound_num in range(10):
        for third_num in range(10):
            if third_num == (first_num + secound_num):
                possible_add_combinations += 1
            elif third_num == (first_num - secound_num):
                possible_sub_combinations += 1
            elif third_num == (first_num * secound_num):
                possible_multi_combinations +=1
            elif secound_num != 0:
                if third_num == (first_num / secound_num):
                    possible_div_combinations += 1
           # else: 
             #   print("not defined within range")

sum_of_possible_calc = 0
sum_of_possible_calc += (possible_add_combinations + possible_div_combinations)
sum_of_possible_calc += (possible_multi_combinations + possible_sub_combinations)
sum_of_possible_calc -= 1 # då ett lösnings alternativ försvinner (000) 
ANSWER = sum_of_possible_calc

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("4.2", ANSWER, False)


dbwebb.exit_with_summary()
