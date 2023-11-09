#!/usr/bin/env python3

"""
7e5bd49bf7a72feea420cdc2d5864e07
python
lab1
v4
kamt23
2023-08-30 13:15:06
v4.0.0 (2019-03-05)

Generated 2023-08-30 15:15:06 by dbwebb lab-utility v4.0.0 (2019-03-05).
https://github.com/dbwebb-se/lab
"""

from dbwebb import Dbwebb


# pylint: disable=invalid-name

dbwebb = Dbwebb()
dbwebb.ready_to_begin()



# ==========================================================================
# Lab 1 - python
#
# If you need to peek at examples or just want to know more, take a look at
# the [Python manual](https://docs.python.org/3/library/index.html).
#
# There you will find everything this lab will go through and much more.
#



# --------------------------------------------------------------------------
# Section 1. Integers, floats and basic arithmetics
#
# The foundation of numbers and basic arithmetic.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.1 (1 points)
#
# Create a variable called `num_one` and give it the value 13.
#
# Answer with the value of `num_one`.
#
# Write your code below and put the answer into the variable ANSWER.
#


num_one = 13


ANSWER = num_one

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.2 (1 points)
#
# Create another variable called `num_two` and give it the value 40. Create a
# third variable called `result` and assign to it the sum of the first two
# variables.
#
# Answer with the `result` variable.
#
# Write your code below and put the answer into the variable ANSWER.
#

num_two = 40

result = num_one + num_two


ANSWER = result

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.3 (1 points)
#
# Create a variable called `num_three` and give it the value 55.
#
# Create another variable called `num_four` and give it the value 81.
#
# Subtract `num_three` from `num_four` and add the `result` variable from
# above to result of the subtraction. Answer with the result.
#
# Write your code below and put the answer into the variable ANSWER.
#

num_three = 55

num_four = 81
result_of_sub = num_four - num_three
add_sub_ans = result_of_sub + result

ANSWER = add_sub_ans

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.3", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.4 (1 points)
#
# Answer with the result of a multiplication of `num_one` and `num_three`.
#
# Write your code below and put the answer into the variable ANSWER.
#

result_of_multi = num_one * num_three




ANSWER = result_of_multi


# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.4", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.5 (1 points)
#
# Create a variable called `float_one` and give it the value 88.68.
#
# Create another variable called `float_two` and give it the value 70.59.
#
# Sum the two values and answer with the result, rounded to two decimals. Use
# the function `round()` to round the number to two decimals.
#
# Write your code below and put the answer into the variable ANSWER.
#

float_one = 88.68
float_two = 70.59
sum_of_floats = float_one + float_two
rounded_sum_of_floats = round(sum_of_floats, 2)

ANSWER = rounded_sum_of_floats

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.5", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.6 (1 points)
#
# All variables used in the exercise below are defined above.
#
# Sum `num_three` with `num_one` and subtract `num_four`. Multiply the result
# by `num_two`, add `float_two` and subtract `float_one`. Use the function
# `round()` to round the number to two decimals.
#
# Answer with the result.
#
# Write your code below and put the answer into the variable ANSWER.
#

ver_num_calc = ((num_three + num_one - num_four) * num_two) + float_two - float_one 


ANSWER = round(ver_num_calc , 2 )

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.6", ANSWER, False)

# --------------------------------------------------------------------------
# Section 2. Strings and concatenation
#
#
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.1 (1 points)
#
# Concatenate (svenska: konkatenera) the two words 'computer' and 'vacation'
# and answer with the result.
#
# Write your code below and put the answer into the variable ANSWER.
#

the_word_is_computer = "computer"
the_word_is_vacation = "vacation"
sum_of_two_words = the_word_is_computer + the_word_is_vacation


ANSWER = sum_of_two_words

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.2 (1 points)
#
# Concatenate the word 'vacation' with the integer 13, with a space between
# the two values.
# Answer with the new string.
#
# Write your code below and put the answer into the variable ANSWER.
#

the_word_is_vacation = "vacation"
interger_with_value_13 = 13
sum_of_word_and_interger = the_word_is_vacation + " " + str(interger_with_value_13)


ANSWER = sum_of_word_and_interger

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.3 (1 points)
#
# Concatenate the integer 13 with the word 'computer' with a space between.
# To the resulting string concatenate the string ' and '. To this string
# concatenate integer 40 and the word 'vacation' with a space between between
# the two values.
#
# Write your code below and put the answer into the variable ANSWER.
#

first_string = str(interger_with_value_13) + " " + the_word_is_computer
and_string = " and "
interger_with_value_40 = 40 
secound_string = str(interger_with_value_40) + " " + the_word_is_vacation

multi_string_add = first_string + and_string + secound_string

ANSWER = multi_string_add

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.3", ANSWER, True)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.4 (1 points)
#
# Assign the string value '30' to a variable called `string_number` and
# assign the integer value 5 to a variable called `actual_number`.
#
# Use `int()` to change the type of `string_number` to an integer and divide
# the integer value with `actual_number`. Answer with an integer by using the
# function `round()`.
#
# Write your code below and put the answer into the variable ANSWER.
#
string_number = "30"
actual_number = 5
str_num_div = int(string_number) /actual_number
result = round( str_num_div, 2) 


ANSWER = result

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
# BTH is using a wind-turbine and solar panels to harvest energy from the
# wind and sun. On a windy and sunny day in September the sun shines for 10
# hours with an average output effect of the solar panels of 9345 W per hour.
# The wind turbine has an average output effect of 314 W per hour for all 24
# hours of the day.
#
# Calculate the total output energy i kWh from the wind turbine and the solar
# panels for the entire day.
#
# Energy i kWh is calculated as `energy = effect * hours / 1000`.
#
# Write your code below and put the answer into the variable ANSWER.
#

solar_watt_output_per_hour = 9345
wind_watt_output_per_hour = 314 

solar_energy = (solar_watt_output_per_hour * 10) / 1000
wind_energy=  (wind_watt_output_per_hour * 24) / 1000

total_energi_harvested = solar_energy + wind_energy

ANSWER = total_energi_harvested

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("3.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 3.2 (3 points)
#
# Peter has the phonenumber '0731415926' and Anna has the phonenumber
# '0727182818'. They call each other every sunday afternoon for 9 minutes.
#
# Calculate the number of hours that they talk with each other pr year
# (assume 52 sundays pr year). Use that number in a string concatenation with
# the following format:
#
# 'Peter calls from [#Peter's phonenumber] to Anna on [#Anna's phonenumber]
# for [#hours] hours every year.'
#
# Replace the content inside [#] with the corresponding values.
#
# Answer with the concatenated string.
#
# Write your code below and put the answer into the variable ANSWER.
#


peters_phone_num = "0731415926"
annas_phone_num = "0727182818"
average_call_period_on_sunday = 9
sundays_in_a_year = 52

call_time_in_minutes = average_call_period_on_sunday * sundays_in_a_year
call_time_in_hours = call_time_in_minutes / 60
phone_call_logs = "Peter calls from "+ peters_phone_num + " to Anna on " 
phone_call_logs += annas_phone_num +" for " + str(call_time_in_hours) + " hours every year."

ANSWER = phone_call_logs

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("3.2", ANSWER, False)


dbwebb.exit_with_summary()
