'''
Lab 4 — Inflectional Morphology and Corpora
Computational Methods in Linguistics

This lab explores how Python can be used to manipulate strings and lists, 
and how we can use these tools to analyze linguistic data from corpora.

Inflectional morphology is the study of how words change form to express grammatical features like tense, number, case, etc. 
In this lab, we'll write a simple function to pluralize English nouns and then analyze a corpus to see how many words follow certain patterns.
'''

import nltk
import collections                                    # Useful for counting frequencies
from typing import List, Any
import bisect                                         # for searching algorithm with sorted lists


try:
    nltk.data.find('corpora/brown')
except:
    print("Downloading 'brown' corpus...")
    nltk.download('brown')
from nltk.corpus import brown

print(f"Successfully loaded the Brown corpus. It contains {len(brown.words())} words.\n")

# =============================================
# Part 1 — Simple pluralization
# =============================================
print("=======\nPart 1\n=======")

# If a word ends in 's', 'x', 'ch', 'sh', append 'es'.
# Otherwise, append 's'. This is a simplification, but good for practice.

def simple_pluralize(word):
    if word.endswith(('s', 'x', 'ch', 'sh')):
        return word + 'es'
    elif word.endswith('ty'):         # if word suffix [-ty] like 'city', remove [-y] and add [-ies]
        return word[:-1] + 'ies'
    elif word.endswith('f'):
        return word[:-1] + 'ves'      # if word suffix [-f] like 'wolf', remove [-f] and add [-ves]
    else:
        return word + 's'

# Test cases for the function
print(f"Plural of 'cat': {simple_pluralize('cat')}")
print(f"Plural of 'bus': {simple_pluralize('bus')}")
print(f"Plural of 'box': {simple_pluralize('box')}")
print(f"Plural of 'church': {simple_pluralize('church')}")
print(f"Plural of 'dish': {simple_pluralize('dish')}\n")

singular_words = ['apple', 'banana', 'orange', 'grape', 'peach', 'wolf', 'fox', 'match',
                  'brush', 'house', 'city', 'day', 'program', 'index']

# list of plural words by applying the 'simple_pluralize' function to each word in singular_words. 
# Optional: using a for-loop, or a list comprehension https://www.w3schools.com/python/python_lists_comprehension.asp
plural_words = [simple_pluralize(word) for word in singular_words]

print(f"Original singular words in order: {singular_words}")
print(f"Plural words in order: {plural_words}\n")

# =============================================
# Part 2 — Sorting words
# =============================================
print("=======\nPart 2\n=======")
'''
Python provides two ways to sort an iterable:
    - the built-in function 'sorted()': takes an iterable argument and returns a sorted list.
    - the list method '.sort()': sorts a list in place (and returns nothing).
Example usage:
sorted(my_list) : generates a new, sorted copy of my_list
my_list.sort() : modifies the existing my_list variable
'''

# Using 'sorted()' to create a new list of singular words sorted alphabetically.
sorted_singular = sorted(singular_words)
print(f"Sorted singular words (using sorted()): {sorted_singular}")

# Sorting the 'plural_words' list in-place using '.sort()'.
plural_words.sort()
print(f"Sorted plural words (using .sort()): {plural_words}\n")

# =============================================
# Part 3 — Searching for words in a corpus
# =============================================
print("=======\nPart 3\n=======")

# Sorted list of words from the Brown corpus
corpus_words = [word.lower() for word in brown.words() if word.isalpha()]
corpus_words.sort()
print(f"Prepared a sorted list of {len(corpus_words)} words from the Brown corpus.\n") 

# Function to test whether the sorted list 'sorted_list' contains 'item' using bisect
def contains(sorted_list: List[Any], item: Any) -> bool:
    i = bisect.bisect_left(sorted_list, item)
    return i != len(sorted_list) and sorted_list[i] == item

# Example uses of the 'contains()' function
print(f"Does corpus contain 'the'? {contains(corpus_words, 'the')}")
print(f"Does corpus contain 'zyxw'? {contains(corpus_words, 'zyxw')}\n")

# Using the 'contains' function defined above to check if the singular form of 'boxes'
# and the plural form of 'box' exist in the 'corpus_words list.

word_to_find_singular = 'box'
word_to_find_plural = simple_pluralize(word_to_find_singular)

print(f"Does corpus contain '{word_to_find_singular}'? {contains(corpus_words, word_to_find_singular)}")
print(f"Does corpus contain '{word_to_find_plural}'? {contains(corpus_words, word_to_find_plural)}\n")

# =============================================
# Part 4 — String manipulation
# =============================================
print("=======\nPart 4\n=======")

# String splitting and joining

sample_sentence = "The quick brown fox jumps over the lazy dog."

# Splitting the 'sample_sentence' into a list of words using the '.split()' method on 'sample_sentence' By default it will separate by spaces 
# reference: https://www.w3schools.com/python/ref_string_split.asp

sentence_tokens = sample_sentence.split()
print(f"Original sentence: '{sample_sentence}'")
print(f"Tokens after splitting: {sentence_tokens}\n")

# The '.join()' method example:
"#".join(["apple","banana","orange"]) 

# Joining the 'sentence_tokens' back into a single string using a hyphen '-' as a separator.
hyphenated_sentence = '-'.join(sentence_tokens)
print(f"Tokens joined with hyphens: '{hyphenated_sentence}'\n")

# Finding all the words in the Brown corpus that end with 'ing' and print the first 10.
words_ending_in_ing = []

# for loop to find words ending in 'ing'
for word in corpus_words:
    if word.endswith('ing'):
        words_ending_in_ing.append(word)
        
print(f"First 10 words ending in 'ing': {words_ending_in_ing[:10]}\n") # [:10] slices list to the first 10

# Counting how many unique words in the corpus end with 's'.
unique_words_ending_in_s_count = []

for word in set(corpus_words):  # convert to set to get unique words removing duplicates
    if word.endswith('s'):
        unique_words_ending_in_s_count.append(word) # if it does, add to the list
print(f"Number of unique words ending in 's': {len(unique_words_ending_in_s_count)}\n") # len to count