""" main module"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import inventory as inv
import marvin1 as m1
import marvin2 as m2

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


def main():
    """
    runs main code, 
    """
    backpack = []
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
        print("9) create_ssn")
        print("10) get acronym ")
        print("11) String randomizer" )
        print("12) srting index processer")
        print("q) Quit.")
        print("a1) string compareing.")
        print("inv pick, add to backpack")
        print("inv, to see backpack")
        print("inv drop, to remove from backpack")



        choice = input("--> ")

        if choice == "q":
            print("Bye, bye - and welcome back anytime!")
            stop = True

        elif choice == "1":
            m1.greet()

        elif choice =="2":
            m1.celcius_to_fahrenheit()

        elif choice == "3":
            m1.points_to_grade()

        elif choice == "4":
            m1.sum_and_average()

        elif choice =="5":
            m1.hyphen_string()

        elif choice == "6": # karma; need to fix !
            m1.compare_numbers()

        elif choice =="7":
            m1.validate_ssn()

        elif choice =="8":
            m1.robber_language()

        elif choice == "a1": #compare letters, if first str contains letters in second str
            m1.word_in_another()
        
        elif choice == "9":
            print(m2.create_ssn(input("enter your birthday, 6 digits: "))) 

        elif choice == "10":
            m2.get_acronym(input("enter string to get acronym "))    
        
        elif choice == "11":
            m2.randomize_string(input("Enter sometihng to randomize: "))
        
        elif choice == "12":
            m2.find_all_indexes(input("enter the first string: "), input("enter the secound string: "))

        elif "inv pick" in choice:
            try:
                listed_message = choice.split(" ")
                index = None
                if len(listed_message) == 3:
                    index = None
                elif len(listed_message) == 4: 
                    index = int(listed_message[3])
                inv.pick(backpack, listed_message[2], index)
            except IndexError:
                print ("IndexError caught, no item was assigned to add") 

        elif choice == "inv":
            inv.inventory(backpack)        

        elif "inv drop" in choice:
            listed_message = choice.split(" ")
            inv.drop(backpack, listed_message[2])
        
        elif "inv swap" in choice:
            listed_message = choice.split(" ")
            try:
                if len(listed_message ) == 4:
                    inv.swap(backpack, listed_message[2], listed_message[3])
            except IndexError:
                print("error has occured, must swap exactly two items")

        else:
            print("That is not a valid choice. You can only choose from the menu.")

        if not stop:
            input("\nPress enter to continue...")

if __name__ == "__main__":
    main()
