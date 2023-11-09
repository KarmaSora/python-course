""" module contains functions to F your mind and cause pylint errors """

def multiplication(num_x,num_y):
    """
    takes in two values and retrun the multilied value of both
    Parameter:
    num_x (float): num_x is a number, type float
    
    Parameter:
    num_y (float): number type float
    return : multiplied value of num_x and num_y

    """
    mult = float(num_x) * float(num_y)
    return int(mult)

def funny_word(makefunny):
    """
    Adds ' is a funny word' to the given word.

    Parameters:
    makefunny (str): The word to make funny.

    Returns:
    str: The original word with ' is a funny word' appended.
    """
    isfunny = makefunny + " is a funny word"
    return isfunny

def decider(decide):
    """
    Decides whether to multiply the input number or make a word funny.

    Parameters:
    decide (int, float, str): The input to decide upon.

    Returns:
    str or float: The result of multiplication or a funny word.
    """
    if isinstance(decide, int):
        return multiplication(decide, decide)
    if isinstance(decide, float):
        return multiplication(decide, decide)
    return funny_word(decide)
    
def double_decider(decide1, decide2):
    """
    Decides and constructs a string based on two inputs.

    Parameters:
    decide1 (int, float, str): The first input.
    decide2 (int, float, str): The second input.

    Returns:
    str: A formatted string containing the decisions.
    """
    first_dec = decider(decide1)
    sec_dec = decider(decide2)
    double_dec = str(first_dec) +' and the square is '+ str(sec_dec)
    return double_dec
