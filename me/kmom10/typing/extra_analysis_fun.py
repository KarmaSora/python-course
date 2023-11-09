"""
more functions for text analysis for typing_analysis.py
"""
def gross_wpm(words, secounds):
    """calculates total words per minute"""
    if isinstance(words, str):  # Check if words is a string
        words = words.split()
    
    words_count =len(words) # takes words as list and checks count
    time_in_min = time_rounder(secounds)

    words_per_min= words_count/time_in_min
    
    
    return words_per_min

def time_rounder(time_in_sec):
    """rounds up time to the nearest min"""
    time_in_min = time_in_sec//60
    if time_in_sec % 60 >= 30:
        time_in_min += 1
    if time_in_min == 0:
        time_in_min =1
    return time_in_min

def wpm_animal(words_per_minute):
    """calculates what animal represents user based on speed"""
    speed_animal =""
    if words_per_minute > 120:
        speed_animal= "Pilgrimsfalk"
    elif words_per_minute >= 100:
        speed_animal= "Kungsörn"
    elif words_per_minute >= 90:
        speed_animal= "Taggstjärtseglare"
    elif words_per_minute >= 80:
        speed_animal= "Sporrgås"
    elif words_per_minute >= 70:
        speed_animal= "Svärdfisk"
    elif words_per_minute >= 60:
        speed_animal= "Gepard"    
    elif words_per_minute >= 50:
        speed_animal= "Struts"
    elif words_per_minute >= 40:
        speed_animal= "Gasell"
    elif words_per_minute >= 30:
        speed_animal= "Människa"
    elif words_per_minute >= 20:
        speed_animal= "Sjöko"
    elif words_per_minute >= 10:
        speed_animal= "Snigel"
    else :
        speed_animal= "Sengångare"
    return speed_animal


def net_wpm(words, false_words, seconds):
    """calculates correct words per min"""
    if isinstance(words, str):  # Check if words is a string
        words = words.split()
    false_count = len(false_words)
    gross = gross_wpm(words, seconds)
    rounded_time = time_rounder(seconds)
    net_value = gross - (false_count / rounded_time)

    speed_animal = wpm_animal(net_value)

    return net_value, speed_animal



if __name__ =="__main__":
    print("test")
    test_res= net_wpm(" i dont even know asd sad as f  s f f g asd g h r s sa das f gas d",["kj","hg,",78], 20235)
    print(test_res)
