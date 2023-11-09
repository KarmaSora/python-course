""" list of functions for marvin kmom03 """
def greet(): # upp1
    """
    this function asks for a name and greets the name/user
    Parameters: None, can make name as param instead of recieving by input
    return: none, function only prints, doesnt renturn an values
    """
    name = input("What is your name? ")
    print("\nMarvin says:\n")
    print(f"Hello {name} - your awesomeness!")
    print("What can I do you for?!")

def celcius_to_fahrenheit():# upp2
    """
    this function asks for input, grades in celcius, and converts it to fahrenheight
    Parameters: None, can make grade as param instead of recieving by input
    return: none, function only prints, doesnt renturn an values, can change to return fahr instead of print
    """
    degrees_cel = float(input("insert the degree in celcius you ant to convert into fahrenheight: "))
    degrees_fahr = (degrees_cel * 1.8000)+ 32.00
    rounded_fahr_value = round(degrees_fahr, 2)
    print(rounded_fahr_value)

def points_to_grade():# upp3
    """
    this function asks for input, max point and gained points, processes the data 
    and prints out a grade based on the calcuations result 
    Parameters: None, can make funtion take two param instead of recieving by input
    return: none, function only prints, doesnt renturn an values
    """
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

def sum_and_average(): # upp4
    """
    this function asks for input and process it. if input is a number calculate
    and prints out the sum of all numbers
    program terminates when 'done' is written
    Parameters: None, can make name as param instead of recieving by input
    return: none, function only prints, doesnt renturn an values
    """
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

def hyphen_string(): # upp5
    """
    this function asks for user input, string, and extends it
    Parameters: None, can make name as param instead of recieving by input
    return: none, function only prints, doesnt renturn an values
    """
    to_extend_string = input("enter a strng to extend: ")
    extended_string = ""
    startng_zero_index = 1
    for letter in to_extend_string:          
        extended_string += letter*startng_zero_index + "-" 
        startng_zero_index += 1
    extended_string = extended_string.rstrip(extended_string[-1])
    print(extended_string) 

def compare_numbers():# upp6
    """
    this function asks for user input and greets the name/user
    Parameters: None, can make name as param instead of recieving by input
    return: none, function only prints, doesnt renturn an values
    """
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

def validate_ssn(): #upp7
    """
    this function asks for a personal ID runs validation tests
    Parameters: None, can make name as param instead of recieving by input
    return: none, function only prints, doesnt renturn an values
    """
    personal_id = input("insert your personal number: ")
    validation_boolean_value = False
    #sum_of_calculated_id = 0
    new_code_id = personal_id.replace("-","")
    new_code_id = new_code_id.replace(" ", "")

    if len(new_code_id) == 10 or len(new_code_id) ==12:
        sum_of_id_multiplied_digits = calculate_luhna_sum(new_code_id)
        if sum_of_id_multiplied_digits != 0:
            if sum_of_id_multiplied_digits % 10 == 0:
                validation_boolean_value = True
            else: print("Not valid")
    else:
        print("Not valid")
        validation_boolean_value = False

    if validation_boolean_value is True:
        print("Valid")
        """
        for index_of_num, digit in enumerate(new_code_id):
            if index_of_num % 2 == 0: 
                sum_of_calculated_id += int(digit)*2 
            elif index_of_num % 2 ==1:
                sum_of_calculated_id += int(digit)
            else:
                print("problem as occured, check your code: Karma ")        
        """

def robber_language(): # upp8
    """
    this function asks for input, string, process it and prints out 
    the input using robber lang
    Parameters: None, can make name as param instead of recieving by input
    return: none, function only prints, doesnt renturn an values
    """
    consonant_list = "bcdfghjklmnpqrstvwxz"
    normallang = input("enter sometihng to convert to rovarspråk: ")
    rovar_lang = ""
    for letter in normallang:
        if letter in consonant_list:
            for i in letter:
                rovar_lang += i+ "o" + i 
        else: rovar_lang += letter
    print(rovar_lang)

def word_in_another(): # upp a1 extra, marvin kmom02 
    """
    this function asks for inputs 
    Parameters: None, can make name as param instead of recieving by input
    return: none, function only prints, doesnt renturn an values
    """
    first_word = input("choose the first word: ")
    second_word = input("choose the second word: ")
    yes_no = False
    contains_string = ""
    for letter in first_word:
        for letter2 in enumerate(second_word):
            if letter2 == letter:
                contains_string += letter2
                #print("letter Found")
                yes_no = True

            else: 
                #print("not this letter")
                yes_no = False
    if second_word in contains_string :
        yes_no = len(contains_string) <= len(second_word)
    print(yes_no)

def calculate_luhna_sum(new_birthday):
    """
    process numbers and calulates using luhna and returns the summed value of the calculated
    Parameter new_birthday (int): intergers/string of numbers. 
    return: the sum of lunhna calcluation
    """
    multiplied_birth_string = ""
    numlet_index = 0
    sum_of_birth_num = 0
    for numlet in new_birthday:
        if numlet_index % 2 == 0:
            multiplied_birth_string += str(int(numlet)*2) 
        else: 
            multiplied_birth_string += str(int(numlet))
        # print(multiplied_birth_string)
        numlet_index +=1
    for single_digit in multiplied_birth_string:
        # print(single_digit, sum_of_birth_num)
        sum_of_birth_num += int(single_digit)

    return sum_of_birth_num
