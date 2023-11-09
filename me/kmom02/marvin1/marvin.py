#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Marvin with a simple menu to start up with.
Marvin doesnt do anything, just presents a menu with some choices.
You should add functinoality to Marvin.
"""

marvin_image = r"""
         MMMMMMMM
        C  ?   %  D
        |    +    |
         \-- K --/
          \ __ /

"""


"""
Its an eternal loop, until q is pressed.
It should check the choice done by the user and call a appropriate
function.
"""
stop = False
while not stop:
    print(chr(27) + "[2J" + chr(27) + "[;H")
    print(marvin_image)
    print("Hi, I'm Shadow, what do you wish to do, master?")
    print("1) Present yourself to Shadow.")
    print("2) convert celcius to fahrenheight")
    print("3) point to grade converter")
    print("4) added and average nums")
    print("5) string extender")
    print("6) number comparing AI")
    print("7) personal number checker")
    print("8) rövarspråk converter")
    print("q) Quit.")
    print("a1) string compareing.")


    choice = input("--> ")

    if choice == "q":
        print("Bye, bye - and welcome back anytime!")
        stop = True

    elif choice == "1":
        name = input("What is your name? ")
        print("\nMarvin says:\n")
        print(f"Hello {name} - your awesomeness!")
        print("What can I do you for?!")

    elif choice =="2":
        degrees_cel = float(input("insert the degree in celcius you ant to convert into fahrenheight: "))
        degrees_fahr = (degrees_cel * 1.8000)+ 32.00
        rounded_fahr_value = round(degrees_fahr, 2)
        print(rounded_fahr_value)


    elif choice == "3":
        maximum_posible_points = float(input("please insert the max posible points you can get: "))
        points_obtained_by_user = float(input("insert the ammount of points you recieved: "))
        grade_to_points_percentage = points_obtained_by_user / maximum_posible_points
        if grade_to_points_percentage >= 0.9:
            print("score: A")
        elif grade_to_points_percentage >= 0.8:
            print("score: B")
        elif grade_to_points_percentage >= 0.7:
            print("score: C")
        elif grade_to_points_percentage >= 0.6:
            print("score: D")                        
        else:
            print("score: F")

    
    elif choice == "4":
        true_boolean = True
        added_numbers = 0.0
        input_calc = 0.0
        average_numbers = 0.0
        while true_boolean: 
            given_value = input("give me a number or say 'done': ")
            if given_value.isdigit():
                input_calc +=1
                added_numbers += float(given_value)
            elif given_value.replace(".", "").isdigit and given_value.count(".") ==1:
                input_calc +=1
                added_numbers += float(given_value)
            elif given_value == "done":
                if input_calc !=0:
                    average_numbers = added_numbers / input_calc
                    sum_is_string = "The sum of all numbers are "
                    and_is_str= " and the average is "
                    rounded_average_str= str(round(average_numbers,2))
                    rounded_added_num_str = str(round(added_numbers,2))
                    print(sum_is_string + rounded_added_num_str + and_is_str + rounded_average_str)
                else: print("no number was inserted, ")
                true_boolean = False
            else: 
                print("given value is undefined, please try again")



    elif choice =="5":
        to_extend_string = input("enter a strng to extend: ")
        extended_string = ""
        startng_zero_index = 1
        for letter in to_extend_string:          
            extended_string += letter*startng_zero_index + "-" 
            startng_zero_index += 1
        extended_string = extended_string.rstrip(extended_string[-1])
        print(extended_string)    

    elif choice == "6": # karma; need to fix !
        first_user_input = input("insert a number: ")
        num_com_bool = True
        big_small_equal = ""
        while num_com_bool:
            if first_user_input == "done":
                num_com_bool = False
                break
            secound_user_input = input ("insert another number: ")
            if first_user_input.isdigit():
                if secound_user_input.isdigit():
                    if float(first_user_input) < float(secound_user_input): #num 1 smaller than num2 print larger
                        big_small_equal = "larger!"
                    elif float(first_user_input) > float(secound_user_input): #num 1 larger than num2 print smaller
                        big_small_equal = "smaller!"
                    elif float(first_user_input) == float(secound_user_input):
                        big_small_equal ="same!" 
                    else:
                        big_small_equal = "an error has occured"
                    first_user_input = secound_user_input
                    print(big_small_equal)
            if first_user_input =="done":
                #print("program terminated")
                num_com_bool = False
                break
            elif first_user_input.isdigit() is False:
                big_small_equal ="not a number!"
                print(big_small_equal)
            if secound_user_input =="done":
                #print("program terminated....")
                num_com_bool = False
                break
            elif secound_user_input.isdigit() is False:
                big_small_equal ="not a number!"
                print(big_small_equal)




    elif choice =="7":
        personal_id = input("insert your personal number: ")
        validation_boolean_value = False
        sum_of_calculated_id = 0
        new_code_id = personal_id.replace("-","")
        new_code_id = new_code_id.replace(" ", "")


        new_multiplied_num = ""
        index_of_number = 0
        sum_of_id_multiplied_digits =0
        if len(new_code_id) == 10:
            for number in new_code_id:
                if index_of_number % 2 == 0:
                    new_multiplied_num += str(int(number)*2) 
                elif index_of_number % 2 ==1:
                    new_multiplied_num += str(int(number))
                index_of_number +=1
                
            for single_digit in new_multiplied_num:
                sum_of_id_multiplied_digits += int(single_digit)
            
            if sum_of_id_multiplied_digits % 10 == 0:
                validation_boolean_value = True
            else: print("Not valid")



        elif len(new_code_id) == 12:
            for number in new_code_id:
                if index_of_number % 2 == 0:
                    new_multiplied_num += str(int(number)*2) 
                elif index_of_number % 2 ==1:
                    new_multiplied_num += str( int(number))
            index_of_number += 1

            for single_digit in new_multiplied_num:
                sum_of_id_multiplied_digits += int(single_digit)
            
            if sum_of_id_multiplied_digits % 10 == 0:
                validation_boolean_value = True

            
        else:
            print("Not valid")
            validation_boolean_value = False

        if validation_boolean_value is True:
            print("Valid")
            for index_of_num, digit in enumerate(new_code_id):
                if index_of_num % 2 == 0: 
                    sum_of_calculated_id += int(digit)*2 
                elif index_of_num % 2 ==1:
                    sum_of_calculated_id += int(digit)
                else:
                    print("problem as occured, check your code: Karma ")


    elif choice =="8":
        consonantList = "bcdfghjklmnpqrstvwxz"
        normallang = input("enter sometihng to convert to rovarspråk: ")
        rovar_lang = ""
        for letter in normallang:
            if letter in consonantList:
                for i in letter:
                    rovar_lang += i+ "o" + i 
            else: rovar_lang += letter
        print(rovar_lang)

    elif choice == "a1": #compare letters, if first str contains letters in second str
        first_word = input("choose the first word: ")
        second_word = input("choose the second word: ")
        yes_no = False
        containsString = ""
        for letter in first_word:
            for letters_index, letter2 in enumerate(second_word):
                if letter2 == letter:
                    containsString += letter2
                    print("letter Found")
                else: 
                    print("not this letter")
        if second_word in containsString:
            yes_no = True
        print(yes_no)

    else:
        print("That is not a valid choice. You can only choose from the menu.")

    if not stop:
        input("\nPress enter to continue...")
