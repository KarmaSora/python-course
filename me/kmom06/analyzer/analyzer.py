"""functions for text analysis for kmom06"""
def word_counter(text):
    """
    places the text in a list and splits where space exists leaving only words
    returns the count of elements in list, which is equal to count of words
    """
    text_as_list = text.split()

    return len(text_as_list) 

def char_counter(text):
    """
    return the lenght of whole texts
    """
    to_remove_list = [" ", ",",".","\n","<",">",":",";","-","_","+","*","/","&","%","¤","#","!","(",")","=","{","}"]
    for char in to_remove_list:
        text = text.replace(char, "")
    return len(text)


def line_counter(text): 
    """
    devides text into list where there is new line. And returns len of list  
    """
    text_as_list = text.split("\n")
    return len(text_as_list)

def read_file(file):
    """
    reads file and returns content as list
    """
    with open(file, "r") as fd:
        file_content_as_list= fd.read()
    return file_content_as_list

def word_frequency(text):
    """calculates frequency of every word in string """
    text = text.replace(",","").replace(".", "").replace(":","")
    text = text.lower()
    text_as_list = text.split()
    word_count = len(text_as_list) 
    
    word_freq_list = {}
    for i in text_as_list:
        if i.isalpha():
            if i in word_freq_list:
                word_freq_list[i]+=1
            else:
                word_freq_list[i] =1    
    ans= calc_freq(word_freq_list, word_count)

    return ans

def letter_frequency(text):
    """
    calculates letter frequency
    returns dict with letters as key and occurence as values
    """
    text=text.lower()
    count_of_chars = char_counter(text)
    letter_freq_dict ={}
    for i in text:
        if i.isalpha():
            if i in letter_freq_dict:
                letter_freq_dict[i]+=1
            else:
                letter_freq_dict[i] =1
    print(letter_freq_dict)
    ans= calc_freq(letter_freq_dict, count_of_chars)
    return ans #letter_freq_dict #ans


def calc_freq(dic, charlet_count):
    """
    Calculates frequency and sorts the list by frequencies and alptha order.
    """

    # Create list and appends string with required values as tuples
    newlist = []
    for character, count in dic.items():
        percent = (count / charlet_count) * 100
        percent = round(percent, 1)
        count_with_percent = f"{character}: {count} | {percent}%"
        newlist.append((count, character, count_with_percent))

    # Sort the list by frequencies (count) in descending order, and then by (letters) in ascending order
    newlist = sorted(newlist, key=lambda x: (x[0], x[1]), reverse=True)

    # Take the top 7 items
    newlist = newlist[:7]

    # create new list and takes the secound element from lists tuple aka character
    # answers with only the count precentage text 
    result_list = []
    for item in newlist:
        result_list.append(item[2])
    return result_list


def freq_all(file_content):
    """returns the value of all other functions"""
    words= word_counter(file_content)
    lines = line_counter(file_content)
    charc= char_counter(file_content)
    letfreq = letter_frequency(file_content)
    stringfid_letfreq = "\n".join(letfreq)
    wofreq = word_frequency(file_content)
    stringfied_wordfreq = "\n".join(wofreq)

    result= f" {lines} \n {words} \n {charc} \n {stringfied_wordfreq} \n {stringfid_letfreq}"
    #result= f" {lines} \n {words} \n {charc} \n {stringfied_wordfreq} \n {letfreq}"
    #result= f" {lines} \n {words} \n {charc} \n {wofreq} \n {stringfid_letfreq}"

    #result= f" {lines} \n {words} \n {charc} \n {wofreq} \n {letfreq}"
    
    #print(file_content)

    return result
