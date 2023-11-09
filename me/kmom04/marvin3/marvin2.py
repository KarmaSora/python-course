""" list of functions for marvin kmom03 """
import random 
def create_ssn(birthday): # upp 9, (upp1) marvin kmom03
    """
    takes in birth date and creates a valid personal ID.
    Parameter birthday: must by a six digit code
    returns: valid perosnal ID with 
    """
    birthday = birthday.replace(" /-", "")
    #print("filtered birthday is: " + birthday)

    if birthday.isdigit():
        if len(birthday) == 6:
            first_rand = random.randrange(10)
            sec_rand = random.randrange(10)
            third_rand = random.randrange(10)
            new_birthday=""
            new_birthday = str(birthday) + str(first_rand) 
            new_birthday += str(sec_rand) + str(third_rand)

            sum_of_birth_num = calculate_luhna_sum(new_birthday)
            #print(" sum of birth:  " + str(sum_of_birth_num))
            #rounded_to_ten = round(sum_of_birth_num, -1)
            rounded_to_ten = round_up_to_nearest_10(sum_of_birth_num)
            #print("closes rounded up num is " + str(rounded_to_ten))

            fourth_hidden_digit = int(rounded_to_ten) - int(sum_of_birth_num)
            if fourth_hidden_digit <0:
                fourth_hidden_digit *= -1
            new_birthday += str(fourth_hidden_digit)

        else: 
            print("password must contain exactly 6 digits")
    else: 
        print("password contains chars other than numbers")
    gen_per_id = str(birthday) + "-"+ str(first_rand) + str(sec_rand) + str(third_rand) + str(fourth_hidden_digit) 
    return gen_per_id

def round_up_to_nearest_10(number):
    """
    Rounds up numbers to the closes 10
    Parameter number (int): takes number type int
    return: the rounded up number to closest 10. 
    """
    remainder = int(number) % 10
    if int(remainder) == 0:
        return int(number)
    return int(number) + (10 - int(remainder))

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

def get_acronym(acro_string): 
    """
    process string and creates acronym
    Parameter acro_string (str): string to create acronym from
    return: acronym

    """
    acronym = ""
    for i in acro_string:
        if i.isupper():
            acronym += i
            #print("building acro ... : " + acronym )
    #print("full acro! : " +  acronym)
    print(acronym)
    return acronym

def randomize_string(to_randomize):
    """
    function takes in string and randomizes the order of the content
    Parameter:
    to_randomize (string): the string to randomize  
    return: returns randomized veriant of original string,
    the numbers are always in same order and placed at the end of stirng!! 
    """
    stirng_of_nums = ""
    string_of_letters =""
    does_have_num = False
    for i in to_randomize:
        if i.isdigit():
            stirng_of_nums += i
            does_have_num = True
        else: 
            string_of_letters += i
    relisted_word = list(string_of_letters)
    random.shuffle(relisted_word)
    rewritten_randomized_word = "".join(relisted_word)+ stirng_of_nums
    if does_have_num:
        ans = rewritten_randomized_word
    else:
        ans = to_randomize + " --> "+ rewritten_randomized_word
    print(ans)
    return ans

def find_all_indexes(str1, str2):
    """
    takes in two strings, prcesses the inputs and returns indexes where 
    str2 is located inside str1. 
    Parameter:
    str1: first string
    str2: secound string 
    return: indexes where str2 is inside str1
    """
    list_of_index = []
    str1_len = len(str1)
    str2_len = len(str2)
    final_check_start_index = str1_len - str2_len
    new_str = ""
    start_index = 0
    while start_index <= final_check_start_index:
        try:
            if str1[start_index:start_index+str2_len] == str2:
                list_of_index.append(start_index)
            start_index += 1
        except ValueError:
            print("catched valueError")
    #print(list_of_index)
    new_str = "".join(str(list_of_index))
    #new_str = new_str[:-1]
    new_str = new_str.replace("[", "").replace("]", "").replace(" ", "")
    print(new_str)

    return new_str
