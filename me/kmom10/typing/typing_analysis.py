"""
module for typing test
"""

import os 
import time
import random
import extra_analysis_fun as extra_fun

def read_file(file):
    """
    reads file and returns content as stirng
    """
    try:
        with open(file, "r") as fd:
            file_content_as_list= fd.read()
    except FileNotFoundError:
        with open(file, "w") as fd:
            file_content_as_list= fd.read()
    return file_content_as_list

def read_score_as_list():
    """reads txt file as list and strips newline"""
    all_scores = []
    file_name = "score.txt"
    try:
        with open(file_name, "r") as fd:
            for line in fd:
                all_scores.append(line.strip()) # add .replace("%","") to 
    except FileNotFoundError:
        with open(file_name, "w") as fd:
            fd.write("")
    return all_scores

def append_score(to_append):
    """overwrites the score.txt with orederd verison of new data"""
    data = read_score_as_list()
    #print(data)
    data.extend(to_append)
    #print(data)
    #tuplified_list =list_toof_tuples(data) #not usefull but looks better
    tuplified_list =list_toof_tuples(data) #not usefull but looks better

    sortedlist = sorted(tuplified_list, key=lambda x: (x[2], x[1]), reverse=True)
    #print(sortedlist)

    #overwrites the content of score and with the new sorted text 
    rewritefile=""    
    for i in sortedlist:
        name = i[0]
        score = i[1]
        deff_level = i[2]
        new_score= f"{name}   {score}   {deff_level}"  #consider using \t for tab spaces  
        rewritefile +=new_score +"\n"
    #print(rewritefile)
    with open("score.txt", "w") as fd: 
        fd.write(rewritefile)


def list_toof_tuples(list_to_convert): #ser finare ut
    """takes list and coverts the elements iside to tuples"""
    newlist = []
    for i in list_to_convert:
        content_listified = i.split()
        #print(content_listified)
        to_append = (content_listified[0],content_listified[1],content_listified[2])
        newlist.append(to_append)
        #print(newlist)
    return newlist

def dic_to_list(dic):
    """takes a dictionary and returns list with string containg keys and values"""
    to_list=[]
    for key in dic.keys():
        value = dic.get(key)
        to_list.append(f"{key}: {value}")
    return to_list


def char_list_maker(string):
    """
    procsesses a string and returns a charlist 
    """
    char_list = []
    for i in string:
        char_list.append(i)
    return char_list

def char_dic_maker(string): 
    """
    takes string and returns a dict of chars as key and count of each chars as value
    """
    char_dic = {}
    for i in string:
        if i in char_dic:
            char_dic[i] +=1
        else:
            char_dic[i] =1
    return char_dic

def word_list_maker(string):
    """
    splits string into lists of words. 
    """
    word_list = string.split()
    return word_list

def wrinting_test(filename): # calculates for words, not chars
    """ 
    # returns orginal text file, wrong written words, calculated word precentage
    splits filecontent and prints lines by line.
    takes user input and preforms calculations and returns result
    """
    text = read_file(filename)

    tot_word_count = len(text.split())
    splitetd_text = text.split("\n") #splits text into lines
    point_counter = 0
    wrong_list = []
    clear_comp_txt() #clears prevoius content in compare.txt

    start_time = time.time()
    for i in splitetd_text: #splits txt file into lines and preforms calculations
        os.system('clear')
        print(i)
        users_input = input("")
        append_user_text(users_input)

        orginal_line_list = word_list_maker(i)
        users_line_list = word_list_maker(users_input)


        # loop through elemtns in both lists as tuples
        for og_txt_line,user_txt_line in zip(orginal_line_list,users_line_list): 
            if user_txt_line== og_txt_line:
                point_counter +=1
            else:
                # tuple list with, (orginal word, user inp) 
                wrong_list.append((og_txt_line,user_txt_line)) 
        
        #extra words calc
        user_len = len(users_line_list) 
        line_len= len(orginal_line_list)
        #removes extra words from the calculations
        if user_len > line_len: 
            point_counter = point_counter - (user_len - line_len)
    #calculating time in seconds
    end_time = time.time()
    print(f"startingTime: {start_time}")
    print(f"endTIme: {end_time}")

    time_in_sec = (start_time -end_time)* -1 
    print(f"totatl time it took: {time_in_sec}")

    

    calc_precent= round((point_counter / tot_word_count *100),2) #removed %
    name_of_user = input("enter your name to save the result: ")
    name_of_user = name_of_user.replace(" ","_")# för att inte påverka score.txt
    return wrong_list, calc_precent, name_of_user,time_in_sec 


def char_comp(file_name):
    """calcuates char accurcy"""

    #reads and converts texts to lists devided line by line 
    #Note: line count is identical in both texts 
    original_text = read_file(file_name)
    original_line = original_text.split("\n")
    
    user_inp = read_file("compare.txt")
    user_inp_line = user_inp.split("\n")

    #Declare veriables to use later
    tot_extra_char = 0
    correctly_spelled = []
    spelled_incorrectly = []
    list_of_extra_chars = []
    char_acc_precent = 0
    correct_count= 0
    #to count how many times each loop ran
    first_loop_run_count = 0
    sec_loop_run_count = 0
    third_loop_run_count = 0



    #first loop, Go trough list of lines
    #Note: The list two lists, original_line and user_inp_line have same num of elements
    for index, og_txt_line in enumerate(original_line): 

        #increase the count of first loop veriable by one
        first_loop_run_count+=1

        # gets the element from user line list with same index as original line list 
        user_txt_line = user_inp_line[index]
        

        if  user_txt_line =="":
            cleaned_og_text = og_txt_line.replace(" ","")
            spelled_incorrectly.extend(cleaned_og_text)
            continue 
        #calculates the length of the enitre line, without spaces, 

        #Converts each the line into a list of words
        og_words_list = word_list_maker(og_txt_line)
        user_words_list = word_list_maker(user_txt_line)

        #extra words
        if len(user_words_list) > len(og_words_list):
            extra_words_list = user_words_list[len(og_words_list):] 
            for i in extra_words_list:
                list_of_extra_chars.extend(i)

            #missing words # could cause index error, check the try catch block
        elif len(user_words_list) < len(og_words_list):
            to_append = og_words_list[len(user_words_list):]

            for each_stirng in to_append:
                spelled_incorrectly.extend(each_stirng)


        #Loop through each word. may cause IndexError
        try:
            sec_loop_run_count = 0 #reset the count                 
            #Loop through each word in the lists, COnsider changig from loop through og list to user list
            for og_word_index,original_word in enumerate(og_words_list): 
                #changing this from enumerate og_word_list to user_words_list # fix here karma

                #increase runcount 
                sec_loop_run_count+=1
                #shows each word
                

                # original_word = user_words_list[user_word_index]

                users_word = user_words_list[og_word_index]
                user_word_char_count = len(users_word)
                original_word_char_count = len(original_word)

                #missing chars
                if user_word_char_count < original_word_char_count:
                    to_append = original_word[user_word_char_count:]
                    spelled_incorrectly.extend(to_append)


                elif user_word_char_count > original_word_char_count:
                    add_to_dic = users_word[len(original_word):] # extra tecken lagras som str i add to dic #works
                    list_of_extra_chars.extend(add_to_dic)



                # In case and index error occures for the chars.
            

                third_loop_run_count = 0 #reset the count
                #Loop through each char in the words starting as from users word
                for char_index, user_char in enumerate(user_words_list[og_word_index]):  

                    #increase runcount
                    third_loop_run_count+=1

                    #get the char from original word that contains same index
                    original_char =original_word[char_index]

                    #compares the chars and increases count of correct chars. 
                    # Works well!
                    if original_char == user_char:
                        correct_count += 1
                        correctly_spelled.extend(original_char)
                    else:
                        #if chars not identical  adds them to dic
                        spelled_incorrectly.extend(original_char)


        #if index error caught, could be caused by missing words or chars
        # is currently handeled in the try catch to
        except IndexError :
            continue



    #After the calculations are done Section

    # preparing the veriables for calcuation 
    tot_chars = len_of_chars(file_name)

    tot_extra_char = len(list_of_extra_chars)

    #The Calculation, Correct Formula
    char_acc_precent = round( (((correct_count - tot_extra_char) / tot_chars )*100) ,2) # removed %

    """ # debug
    print (f"list_of_extra_chars> {list_of_extra_chars}")
    print (f"correctly_spelled> {correctly_spelled}")
    print (f"spelled_incorrectly> {spelled_incorrectly} and it contains {len(spelled_incorrectly)}")
    """

    spelled_incorrectly_dic={}

    spelled_incorrectly_dic= add_str_char_to_dic(spelled_incorrectly_dic,spelled_incorrectly)
    #print(f"this is an STD: {spelled_incorrectly_dic}")
    return char_acc_precent, spelled_incorrectly_dic


def add_str_char_to_dic(dic, std):
    """takes dic and sting and adds string chars to dic"""
    for i in std:
        if i in dic:
            dic[i] +=1
        else:
            dic[i]= 1
    return dic
def clear_comp_txt():
    """ cleares the content of compare.txt"""
    with open("compare.txt", "w") as rewrite:
        rewrite.write("")

def append_user_text(user_data):
    """ takes data from user as text and appends it to compare.txt """
    with open ("compare.txt","a") as user_inp:
        user_inp.write(user_data+"\n")

def all_in_one(filename):
    """uses calls other functions to complete the task"""
    deff_level = filename.split(".")[0]
    test_result=wrinting_test(filename)
    os.system('clear')
    print("Congrats, you have finnished the training ")
    continue_is_selected = input("press enter to see you score: ... ")

    char_acc_res = char_comp(filename)
    word_precision = test_result[1] #
    name_of_user = test_result[2]#

    original_time_in_sec = test_result[3] #
    remaining_time = original_time_in_sec % 60 # time in sec after conv to minuets
    time_in_sec =original_time_in_sec- remaining_time   # removes the time in sec from og time to get hole num after
    time_in_minuets = time_in_sec/60 # div with 60

    if name_of_user is None or name_of_user == "":
        name_of_user ="Anonymous_user"
    append_score([f"{name_of_user}   {word_precision}   {deff_level}"]) #consider using \t for tab spaces  

    fel_list= dic_to_list(char_acc_res[1])
    sorted_fel_list = sorted(fel_list, key=lambda x: (int(x.split(': ')[1]), x.split(': ')[0]), reverse=True)

    user_text= read_file("compare.txt")
    print(user_text)
    gross_wpm = extra_fun.gross_wpm(user_text, original_time_in_sec )
    feltecken_string = "\n".join(sorted_fel_list)
    if continue_is_selected or continue_is_selected =="": #if any key is pressed then the result will show
        print(f"Ordprecision: {word_precision}%")
        print(f"Teckenprecision: {char_acc_res[0]}%")
        print(f"Felstavade tecken: \n{feltecken_string}")
        #print(fel_list)

        print("--------------\nExtra\n---------------")
        false_words =test_result[0] # false/incorrect words as list of tuples
        #print(false_words)
        print(f"it took you {time_in_minuets} minuets and {remaining_time} secounds") #here continue
        print(f"Gross Words per minuetes: {gross_wpm}")
        net_wpm_res= extra_fun.net_wpm(user_text, false_words, original_time_in_sec)
        print(f"Net WPM: {net_wpm_res[0]}")
        print(f"Du skriver snabbt som en {net_wpm_res[1]}")

def ranomized_char_test():
    """random char test"""
    data_saved = "randomTest.txt"
    with open(data_saved, "w")as clean: #clean old content in random_test.txt
        clean.write("")# creates it if it doesnt exist
        
    with open("compare.txt", "w")as clean: #clean old content in comapre.txt
        clean.write("")# creates it if it doesnt exist

    # Display the random character to the user
    abc_lower = "abcdefghijklmnopqrstuvwxyz"
    abc_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_ex_char = "#¤%&/()=?`^*_:;!£$%^*~"
    swe_extras = "åÅöÖäÄ"
    numbers ="0123456789"
    all_chars_to_pick = abc_lower + abc_upper + special_ex_char+ swe_extras + numbers
    to_pick_list= char_list_maker(all_chars_to_pick)
    element_count=len(to_pick_list)
    count_down = int(input("select time in seconds for program to run: "))

    starting_time= time.time()
    to_run = starting_time + count_down

    while True:
        time_running = time.time()
        if time_running >= to_run:
            break

        #picks random int as index to choose from list
        the_chosen_one = random.randint(0, element_count-1) 
        the_randomized_char = all_chars_to_pick[the_chosen_one]
        #the chosen char by index
        os.system("clear")
        print(f"print this char: {the_randomized_char}")    

        #saves users_char in compare.txt
        users_char=input("")
        append_user_text(users_char)

        #spara original chars i data_saved
        with open (data_saved,"a") as original_chars:
            original_chars.write(the_randomized_char+"\n")
    res,false = char_comp(data_saved)
    fel_list= dic_to_list(false)
    sorted_fel_list = sorted(fel_list, key=lambda x: (int(x.split(': ')[1]), x.split(': ')[0]), reverse=True)

    listed_dic_as_str = "\n".join(sorted_fel_list)
    return res, listed_dic_as_str


def len_of_chars(filename):
    """calculates the length of chars from a file, spaces and newlines dont count"""
    whole_file= read_file(filename)
    new_text= whole_file.replace(" ","").replace("\n","")
    return len(new_text)


if __name__ == "__main__":
    name_of_file = "sample.txt"
    char_comp(name_of_file)
    #ranomized_char_test()
