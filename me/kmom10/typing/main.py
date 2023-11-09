"""main for slutprojekt"""
import os
import typing_analysis as typ
def main():
    """ main function"""
    marvin_image = r"""
         MMMMMMMM
        C  ?   %  D
        |    +    |
         \-- K --/
          \ __ /

        """
    
    stop = False
    while not stop:
        print(marvin_image)
        print("DeathNote: Writing test!")
        print("1) easy")
        print("2) medium")
        print("3) hard")
        print("4) score")
        print("5) Train")
        print("quit) to terminate program, enter: q , clear , exit")

        print("6) dbwebb sample: ex, 6, sample")

        choice = input("--> ")

        if choice in ["exit","q" ,"clear"]:
            print("Tell the Devil I said Howdy")
            stop = True
        
        elif choice in ["easy", "e", "1"]:
            name_of_file="easy.txt"
            typ.all_in_one(name_of_file)

        elif choice in ["medium", "m", "2"]:
            name_of_file="medium.txt"
            typ.all_in_one(name_of_file)

        elif choice in ["hard", "h", "3"]:
            name_of_file="hard.txt"
            typ.all_in_one(name_of_file)

        elif choice in ["score","s","4"]:
            print(typ.read_file("score.txt"))

        elif choice in ["train", "t", "5"]:
            char_accurcy, false_words = typ.ranomized_char_test()
            print(f"you got {char_accurcy}% correct")
            print(f"misspelled words {false_words}")


        elif choice in ["ex", "6","sample"]:
            typ.all_in_one("sample.txt")
        else:
            print("choice doesnt exist. Check the possible choice list")
        if not stop:
            input("\nPress enter to continue...")
            os.system("clear")
    

if __name__ == "__main__":
    main()
