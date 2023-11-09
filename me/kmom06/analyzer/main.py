"""main for kmom06"""
import analyzer as fun

def main():
    """ main function"""
    starting_file= "phil.txt"
    stop = False
    while not stop:
        print("Death Note")
        print("words")
        print("letters")
        print("lines")
        print("change")
        print("word_frequency or wf")
        print("letter_frequency or lf")
        choice = input("--> ")

        if choice in ["exit","q" ,"clear"]:
            print("Tell the Devil I said Howdy")
            stop = True
        elif choice == "words":
            file_content = fun.read_file(starting_file)
            word_count =fun.word_counter(file_content)
            print(word_count)

        elif choice== "letters":
            file_content = fun.read_file(starting_file)
            char_count= fun.char_counter(file_content)
            print(char_count)
        elif choice== "lines":
            file_content = fun.read_file(starting_file)
            line_count= fun.line_counter(file_content)
            print(line_count)
        
        
        elif choice =="change":
            to_enter = input("select file to change to: ")
            if to_enter in["lorum.txt", "phil.txt"]:
                starting_file = to_enter
            else:
                print("file not found or cant be choosen. Please try lorum.txt or phil.txt ")



        elif choice in ["word_frequency", "wf"]:
            #print(fun.word_frequency("k karam testing code, test of code is here"))
            file_content = fun.read_file(starting_file)
            freq_list = fun.word_frequency(file_content)
            freq_str= "\n".join(freq_list)
            #freq_str= freq_list
            
            print(freq_str)
        
        elif choice in ["letter_frequency","lf"]:
            file_content = fun.read_file(starting_file)
            freq_list= fun.letter_frequency(file_content)
            freq_str= "\n".join(freq_list)
            #freq_str= freq_list

            print(freq_str)
        
        elif "all" in choice:
            file_content = fun.read_file(starting_file)
            all_list = fun.freq_all(file_content)
            print(all_list)

        else:
            print("choice doesnt exist. Check the possible choice list")
        if not stop:
            input("\nPress enter to continue...")
    

if __name__ == "__main__":
    main()
