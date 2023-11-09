#!/usr/bin/env python3

"""
95d63f3af18e3acc344e85bd6c5e0900
python
lab6
v4
kamt23
2023-10-10 19:29:48
v4.0.0 (2019-03-05)

Generated 2023-10-10 21:29:48 by dbwebb lab-utility v4.0.0 (2019-03-05).
https://github.com/dbwebb-se/lab
"""

from dbwebb import Dbwebb


# pylint: disable=invalid-name

dbwebb = Dbwebb()
dbwebb.ready_to_begin()



# ==========================================================================
# Lab 6 - python
#
# During these exercises we train on reading, writing and appending data to
# text file's.
#



# --------------------------------------------------------------------------
# Section 1. Files
#
#
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.1 (1 points)
#
# Read the `quotes.txt` -file in UTF-8 encoding and store the content into a
# variable. Answer with the number of characters in the file.
#
# Write your code below and put the answer into the variable ANSWER.
#

quote_content = open("quotes.txt", "r")
quote_content_str = "".join(quote_content.readlines())
quote_content.close()



ANSWER = len(quote_content_str)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.2 (1 points)
#
# Use your variable from the exercise above and answer with the contents on
# line number 1.
#
# Write your code below and put the answer into the variable ANSWER.
#

end_of_line = quote_content_str.index("\n")
first_line = quote_content_str[:end_of_line]


ANSWER = first_line

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.3 (1 points)
#
# First, read the content inside of quotes.txt and remove the 5 last rows.
# Then replace line number 5 with the new string "I am replaced".
# Then, create a new file called `newQuotes.txt` where you save the new
# changes. Replace `newQuotes.txt` if it already exists.
#
# Answer with the new content inside `newQuotes.txt`. Don't have a "\n" on
# the last line.
#
# Write your code below and put the answer into the variable ANSWER.
#
try:
    with open("quotes.txt", "r") as fd:
        all_lines_list = fd.readlines()
        index_count = len(all_lines_list)
        all_lines_list = all_lines_list[:index_count-5]
        all_lines_list[4] = "I am replaced\n"
        try:
            with open("newQuotes.txt", "w") as new_file:
                all_lines_list_index_count = len(all_lines_list)-1
                all_lines_list[all_lines_list_index_count] = all_lines_list[all_lines_list_index_count].strip("\n")
                new_file.write("".join(all_lines_list))
        except FileNotFoundError as e:
            print("file2 not found: "+ str(e))
except FileNotFoundError as e:
    print("file1 not found: "+ str(e))

try:
    with open("newQuotes.txt", "r") as fd:
        strfied_content = "".join(fd.readlines())
except FileNotFoundError:
    print("file doesnt exist: ")

ANSWER = strfied_content

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.3", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.4 (1 points)
#
# Append the following sentence on a new line at the end of newQuotes.txt and
# answer with the content.
#
# *"All creativity is an extended form of a joke."*
#
# Write your code below and put the answer into the variable ANSWER.
#

with open("newQuotes.txt","a") as fd:
    fd.write("\nAll creativity is an extended form of a joke.")
with open("newQuotes.txt","r") as fr: 
    form_of_joke = "".join(fr.readlines())

ANSWER = form_of_joke

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.4", ANSWER, True)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.5 (1 points)
#
# Store the number of empty lines that `passwords.txt` has and create a new
# file called `newPasswords.txt` containing the lines that are not empty.
#
# Answer with the following:
#
# *passwords.txt has X empty lines and contains: Y*
#
# Replace `X` with the number of empty lines and `Y` with the new files
# content.
#
# Write your code below and put the answer into the variable ANSWER.
#

with open("passwords.txt", "r") as fd:
    lines_array = fd.readlines()
newstr =""
empty_line_count = 0
index_count = len(lines_array)
for i in range(index_count):
    if lines_array[i] =="\n":
        empty_line_count +=1  

with open("newPasswords.txt", "w") as fd:
    for line in lines_array:
        if line != "\n":
            fd.write(line)
with open("newPasswords.txt","r") as fd:
    strfied_content = "".join(fd.readlines())

ans = "passwords.txt has "+str(empty_line_count)+" empty lines and contains: "+ strfied_content
ANSWER = ans 

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.5", ANSWER, True)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.6 (3 points)
#
# Write the content of line numbers 1, 2 and 3 from `quotes.txt` to a new
# file that you create called `extraQuotes.txt`. Replace `extraQuotes.txt` if
# it already exists.
# Save the total number of characters and the 9 first characters of the
# second line into variables.
#
# Answer with the following string:
# "The file has X characters and the 9 first of the second row are: Y"
#
# **Example**:
# *"The file has 220 characters and the 9 first of the second row are: - Jon
# Doe"*
#
# Do not include newlines when you count the number of characters.
#
# Write your code below and put the answer into the variable ANSWER.
#
with open("quotes.txt","r") as fd:
    first_line_of_quotes = fd.readline()
    sec_line_of_quotes = fd.readline() 
    third_line_of_quotes = fd.readline() 
char_counter = len(first_line_of_quotes.rstrip() + sec_line_of_quotes.rstrip()+ third_line_of_quotes.rstrip())

with open("extraQuotes.txt", "w") as fd:
    fd.write(first_line_of_quotes+"\n"+sec_line_of_quotes+"\n"+third_line_of_quotes)

chars_list = sec_line_of_quotes[:9] # ska vara 8 så att man tar första 9 , då index börjar på 0 
char_counter_str = "The file has "+ str(char_counter)+" characters" 
first_9 = "the 9 first of the second row are: " + chars_list



ANSWER = char_counter_str+ " and " + first_9

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.6", ANSWER, True)


dbwebb.exit_with_summary()
