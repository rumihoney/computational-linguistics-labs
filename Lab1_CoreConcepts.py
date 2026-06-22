'''
Lab 1 — Core Python Concepts for Linguistic Analysis
Computational Methods in Linguistics

This lab introduces core Python concepts such as variables, data types, lists, strings, and basic operations.
'''

# ======================================================
# Part 1 — Storing Linguistic Data in Variables
# ======================================================

print("=======\nPart 1\n=======")
    
word1 = 'linguistics'
word2 = 'phonetics'
word3 = 'morphology'
word4 = 'syntax'
word5 = 'semantics'

consonants = ["t", "n", "s", "q", "r"]  

print('words:',word1, word2, word3, word4, word5)                                          # prints all the words stored in the variables
print('number of words:', len([word1, word2, word3, word4, word5]))                        # prints the number of words in the list
print('consonants:', consonants)                                                           # prints the list of consonants stored in the variable
print('first consonant:', consonants[0])                                                   # prints the first consonant in the list (index 0)
print('last consonant:', consonants[-1])                                                   # prints the last consonant in the list (index -1)

# ======================================================
# Part 2 — List Indexing and Length
# ======================================================

print("=======\nPart 2\n=======")

words = ["pat", "bat", "cat", "spat", "tap"]

print('words:', words)
print('first word:', words[0])                                                             # prints the first word in the list

# ======================================================
# Part 3 — Simple String Operations
# ======================================================

print("=======\nPart 3\n=======")

example = "spat"
print('example word:', example)                                                            # prints the example word stored in the variable
print('first character:', example[0])                                                      # prints the first character in the string (index 0)
print('last character:', example[-1])                                                      # prints the last character in the string (index -1)
print('length:', len(example))                                                             # prints the length of the string "spat"

# ======================================================
# Part 4 — Printing with Labels 
# ======================================================

print("=======\nPart 4\n=======")

print('Word list:', words)                                                                # prints the list of words with a label
print('Number of words:', len(words))                                                     # prints the number of words with a label
print('First word:', words[0])                                                            # prints the first word with a label


