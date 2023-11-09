"""inventory.py marvin 3, kmom4 """
def pick(backpack, to_pick, item_index = None):
    """ 
    inventory manager
    """
    try:
        if to_pick is None:
            print("no item selected")   
        
        if item_index is None:
            backpack.append(to_pick)
            print(backpack, item_index)
        elif int(item_index) <= len(backpack):
            backpack.insert(int(item_index),to_pick)
            print(backpack, item_index)
        else:
            print("Error : ", backpack, item_index)
    except IndexError:
        print("Error given index out of range, ",str(item_index), " is too high")
    return backpack

def inventory(backpack):
    """
    print backpack count and content
    """
    item_count = len(backpack)
    print("Backpack has "+ str(item_count)+ " and has the following items:", backpack)

def drop (backpack, content):
    """
    removes first occurens from list
    """
    try:
        backpack.remove(content)
        print("dropped: "+ content+ ". Here is the remaining content:", backpack)
    except ValueError:
        print("Value Error caught cont is: ", content, "backP is: ",backpack )
    return backpack

def swap(backpack,first_item, secound_item):    
    """
    swaps two items in list
    """    
    first_bool = False
    sec_bool = False
    try:
        for element in backpack:
            if element == first_item:
                first_bool = True
            if element == secound_item:
                sec_bool = True
        if first_bool is True and sec_bool is True:
            first_it_index = backpack.index(first_item)
            sec_it_index = backpack.index(secound_item)
            backpack[first_it_index] = secound_item
            backpack[sec_it_index] = first_item
        else: 
            lost_content = ""
            if first_bool is False and sec_bool is False:
                lost_content+="Error : "+ first_item + " and " + secound_item + " do not exist in backpack" 
            elif first_bool is False:
                lost_content += "Error : "+  first_item + " do not exist in backpack" 
            else: 
                lost_content += "Error : "+ secound_item  + " do not exist in backpack" 
            print(lost_content)
    except (ValueError, IndexError):
        print("errors, caught")
    print(backpack)
    return backpack
