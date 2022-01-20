from operator import le
import pickle
import random

WORD_LIST = []
with open("five_words.txt", 'rb') as f:
    WORD_LIST = pickle.load(f)

"""
Function that takes in a two lists and a dictionary and spits out a valid guess

letters_used - list of all letters used that are known to not be in the word
letters_in_word - list of letters known to be in the word
position_to_letter - mapping of known letter in a certain position
"""

def guess(letters_used, letters_in_word, letter_to_position):
    new_word_list = []
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
        
        if(keep):
            new_word_list.append(word)
    
    #WORD_LIST = new_word_list
    if(len(new_word_list) == 0):
        print("No words match requirements")
        exit()
    return new_word_list[0]

def main():
    letters_used = set()
    letters_in_word = set()
    letter_to_position = {}
    q1 = input("Start? Y/N\n")
    if(q1 == "Y"):
        #word = guess(letters_used, letters_in_word, letter_to_position)
        #WORD_LIST.remove(word)
        print("audio")
    
    while(True):
        q = input("Solved? Y/N\n")
        if(q == "Y"):
            exit()
        elif(q == "N"):
            letter_input = input("Letters Used :")
            if(letter_input.isalnum()):
                letters_used.update(set(letter_input))
            elif(letter_input == ""):
                continue
            else:
                print("Malformed Input")
            letter_input = input("Letters in Word :")
            
            if(letter_input.isalnum()):
                letters_used.update(set(letter_input))
            elif(letters_used == ""):
                continue
            else:
                print("malformed_input")

            letters_used = letters_used - letters_in_word
            
            index_to_letter_string = input("Input the index to each letter: ")
            if(index_to_letter_string.isalnum()):
                index_to_letter_string = list(index_to_letter_string)
                for i in range(0, len(index_to_letter_string), 2):
                    letter_to_position[int(index_to_letter_string[i])] = index_to_letter_string[i + 1]
            
            letters_used.discard(' ')
            letters_in_word.discard(' ')
            word = guess(letters_used, letters_in_word, letter_to_position)
            print(word)
            WORD_LIST.remove(word)
        else:
            print("Invalid Input")



        
        

        
main()