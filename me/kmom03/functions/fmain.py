#takse in two values and retrun the multilied value of both
#x, x is a number, type float
#y, number type float
def multiplication(x,y):
    mult = float(x) * float(y)
    return mult

def funny_word(makefunny):
    isfunny = makefunny + " is a funny word"
    return isfunny

def decider(decide):
    if decide.isdigit():
        return multiplication(decide,decide)
    else: 
        return funny_word(decide)
    
def double_decider(decide1, decide2):
    first_dec = decider(decide1)
    sec_dec = decider(decide2)
    double_dec = str(first_dec) + str(sec_dec)
    return double_dec