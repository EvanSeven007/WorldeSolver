import csv
import string
import json
import pickle
keep_words = []
with open("count_1w.txt", "r") as f:
    Lines = f.readlines()
    alphabet = list(string.ascii_lowercase)
    for line in Lines:
        word = line.split()[0]
        keep = True
        for char in word:
            if char not in alphabet:
                keep = False
        if(len(word) == 5 and keep):
            keep_words.append(word)
with open("five_words.txt", "wb") as f:
    pickle.dump(keep_words, f)
