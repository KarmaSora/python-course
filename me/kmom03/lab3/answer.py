#!/usr/bin/env python3

"""
67d9648a7f5d06b7c2b3d85320b9d6ed
python
lab3
v4
kamt23
2023-09-13 18:40:56
v4.0.0 (2019-03-05)

Generated 2023-09-13 20:40:56 by dbwebb lab-utility v4.0.0 (2019-03-05).
https://github.com/dbwebb-se/lab
"""

from dbwebb import Dbwebb
import labfunctions as labf



# pylint: disable=invalid-name

dbwebb = Dbwebb()
dbwebb.ready_to_begin()



# ==========================================================================
# Lab 3 - python
#
# In this lab we take another look at functions and we use modules to
# structure our code.
#



# --------------------------------------------------------------------------
# Section 1. Functions
#
#
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.1 (1 points)
#
# Create a function `valid_password` that takes one string argument. Check
# whether the argument is a valid password according to the following rules:
#
# * 8 characters or longer
# * Contains upper and lowercase letters
# * Contains a number
#
# The function should return True or False depending on whether the password
# is valid.
#
# Answer with the return value of the function when called with the string
# 'mYsecretpassw0rd'.
#
# Tip: Use built-in character functions `isupper()`, `islower()`,
# `isdigit()`.
#
# Write your code below and put the answer into the variable ANSWER.
#

password = "mYsecretpassw0rd" #input("Enter your password for validation: ")

def valid_password(pwd):

    """
    This function proccess and validates a given string/password!
    Parameters:
        pwd (string) is the string/passowrd that will be validated
    return: returns True or False

    """ 

    lowercase_check = False
    uppercase_pass_check = False
    num_check = False

    if len(pwd) >= 8:
        for letter in pwd:
            if letter.islower():
                lowercase_check = True
            elif letter.isupper():
                uppercase_pass_check = True
            elif letter.isdigit():
                num_check = True
            else: 
                print("pwd contains forbidden characters")
    else: 
        print("pass too short")
    if lowercase_check is True and uppercase_pass_check is True and num_check is True:
        return True
    
    return False
    
    
valid_password(password)
print(valid_password(password))


ANSWER = valid_password(password)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.2 (1 points)
#
# Using the function `valid_password` answer with the return value of the
# function when called with the string 'test'.
#
# Write your code below and put the answer into the variable ANSWER.
#






ANSWER = valid_password("test")

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.3 (1 points)
#
# Create a function `number_of_vowels` that takes one argument. The function
# returns the number of vowels (vokaler) in the given argument. The following
# letters is used as vowels in this exercise: aeiouy. Your solution should be
# case-insensitive.
#
# Answer with the number of vowels in the following text:
#
# 'How brief our moment of life is. How to be steadfast, and strong, and in
# control of yourself.'
#
# Write your code below and put the answer into the variable ANSWER.
#

def number_of_vowels(string):

    
    """
    This function processes the provided string and returns vowl count
    Parameters:
        string: The string to be processed.
    Returns:
        vowl_num: The processed passwords vowl counter.
    """
    vowl_num = 0
    vowls = "aeiouy"
    cap_vowls = "AEIOUY"
    for letter in string:
        if letter in vowls:
            vowl_num +=1
        elif letter in cap_vowls:
            vowl_num +=1
    return vowl_num
message = 'How brief our moment of life is. How to be steadfast, and strong, and in control of yourself.'




ANSWER = number_of_vowels(message)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.3", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.4 (1 points)
#
# Create a function `analyze_password` that uses `valid_password` and
# `number_of_vowels`. The function should return whether or not a password is
# valid and how many vowels the given password contains concatenated to a
# string.
#
# Example: With the input value Se3ret the function should return the
# following string: 'Se3ret is not a valid password and contains 2 vowels.'.
#
# With the input value anoth3ePw0Rd the function should return the following
# string: 'anoth3ePw0Rd is a valid password and contains 3 vowels.'.
#
# Answer with the return value of the function `analyze_password` called with
# the following argument: AP4ssword.
#
# Write your code below and put the answer into the variable ANSWER.
#

def analyze_password(pwd):

    """
    This function processes the provided password.
    Parameters:
        pwd (str): The password to be processed.
    Returns:
        str: The processed password.
    """
    pwd_validationR = valid_password(pwd)
    pwd_vowlC = number_of_vowels(pwd)

    pwdValRes = ""
    if pwd_validationR:
        pwdValRes += pwd +" is a valid password and contains "
    else:
        pwdValRes += pwd +" is not a valid password and contains "
    
    ans =  str(pwdValRes) + str(pwd_vowlC) + " vowels."
    return str(ans)

ANSWER = analyze_password("AP4ssword")

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.4", ANSWER, False)

# --------------------------------------------------------------------------
# Section 2. Modules
#
# In this section we will look into modules and how we can structure our
# code.
#


# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.1 (1 points)
#
# Create a new Python file called `functions.py`. Import your new file/module
# in `answer.py` using the import statement: `import functions`
#
# In your new module, create a function called `multiplication` that takes
# two arguments. The function should return the product of the two arguments.
#
# Answer with the return value from a call to the function with the two
# arguments 89 and 44.
#
# Write your code below and put the answer into the variable ANSWER.
#


mult = labf.multiplication(89,44)

ANSWER = mult

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.1", ANSWER, True)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.2 (1 points)
#
# In your new module, create a function called `funny_word` that takes one
# argument and prepends it to the string ' is a funny word'. **EXAMPLE:** If
# the argument is 'water', the function should return: `"water is a funny
# word"`.
#
# Use the argument 'barbeque' and answer with a call to the function.
#
# Write your code below and put the answer into the variable ANSWER.
#


ANSWER = labf.funny_word("barbeque")

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.3 (1 points)
#
# In your new module, create a function called `decider`. The function takes
# one argument. If the argument is a string return a call to `funny_word()`,
# if the argument is an integer return the square of the argument by using
# the `multiplication` function.
#
# Answer with a call to the function `decider` with the value `filibuster` as
# argument.
#
# Write your code below and put the answer into the variable ANSWER.
#


ANSWER = labf.decider("filibuster")

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.3", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.4 (1 points)
#
# In your new module, create a function called `double_decider`. The function
# takes two arguments. For each argument call the `decider` function.
# Concatenate the returned values in a string.
#
# Separate the two values by ' and the square is '.
#
# Answer with a call to the function `double_decider` with the values:
# 'hemidemisemiquaver' and 53 as arguments.
#
# Write your code below and put the answer into the variable ANSWER.
#



ANSWER = labf.double_decider("hemidemisemiquaver", 53) 

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.4", ANSWER, True)


dbwebb.exit_with_summary()
