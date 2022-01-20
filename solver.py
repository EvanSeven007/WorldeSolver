import pickle
from collections import defaultdict

WORD_LIST = []
with open("five_words.txt", 'rb') as f:
    WORD_LIST = pickle.load(f)

"""
Function that takes in a two lists and a dictionary and spits out a valid guess

letters_used - list of all letters used that are known to not be in the word
letters_in_word - list of letters known to be in the word
position_to_letter - mapping of known letter in a certain position
"""

def guess(letters_used, letters_in_word, letter_to_position, yellow_letters):
    global WORD_LIST
    for word in WORD_LIST:
        keep = True
        for char in word:
            if(char in letters_used):
                keep = False
        for char in letters_in_word:
            if char not in word:
                keep = False
        for index, character in letter_to_position.items():
            if(word[index] != character):
                keep = False
        for index, char_set in yellow_letters.items():
            for char in char_set:
                if word[index] == char:
                    keep = False
        if(keep):
            return word
    
    #WORD_LIST = new_word_list
    print("No words match restraints")
    exit()

def main():
    letters_used = set()
    letters_in_word = set()
    letter_to_position = {}
    yellow_letters = defaultdict(set)
    q1 = input("Start? Y/N\n")
    if(q1 == "Y"):
        #Good starting word
        print("audio")
    
    while(True):
        q = input("Solved? Y/N\n")
        if(q == "Y"):
            exit()
        elif(q == "N"):
            letter_input = input("Letters Used :")
            if(letter_input.isalnum()):
                letters_used.update(set(letter_input))
            elif(letter_input == "" or letter_input == " "):
                pass
            else:
                print("Malformed Input")

            letter_input = input("Letters in Word :")
            if(letter_input.isalnum()):
                letters_in_word.update(set(letter_input))
            elif(letter_input == ""):
                pass
            else:
                print("malformed_input")

            letters_used = letters_used - letters_in_word
            
            index_to_letter_string = input("Input the index to each letter: ")
            if(index_to_letter_string.isalnum()):
                index_to_letter_string = list(index_to_letter_string)
                for i in range(0, len(index_to_letter_string), 2):
                    try:
                        letter_to_position[int(index_to_letter_string[i])] = index_to_letter_string[i + 1]
                    except:
                        pass

            yellow_letter_string = input("Yellow Letters? :")
            if(yellow_letter_string.isalnum()):
                yellow_letter_list = list(yellow_letter_string)
                for i in range(0, len(yellow_letter_list),2):
                    try:
                        yellow_letters[int(yellow_letter_list[i])].add(yellow_letter_list[i + 1])
                    except:
                        pass

            letters_used.discard(' ')
            letters_in_word.discard(' ')
            word = guess(letters_used, letters_in_word, letter_to_position, yellow_letters)
            print(word)
            WORD_LIST.remove(word)
        else:
            print("Invalid Input")



        
        

        
main()