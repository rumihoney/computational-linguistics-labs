'''
Lab 5 — Derivational Morphology and Regular Expressions
Computational Methods in Linguistics

This lab explores how Python can be used to identify and extract morphological patterns using regular expressions.

Derivational morphology is the study of how words are formed through the addition of affixes.
In Python, these are expressed with regular expressions (regex) and the 're' module.
'''

import re
import nltk
nltk.download('brown')
nltk.download('nps_chat')
nltk.download('webtext')
nltk.download('stopwords')
words = [
    "happy", "unhappy", "happiness", "happily",
    "construct", "reconstruct", "construction",
    "organize", "organization", "organizational",
    "kind", "kindness",
    "read", "reader", "readable", "reading",
    "walk", "walker", "walking", "walked",
    "teach", "teacher",
    "compute", "computer", "computation",
    "act", "action", "active", "react", "reaction",
    "govern", "government", "ungovernable",
    "develop", "development", "undeveloped",
    "color", "colour", "colorful", "discolor",
    "apple", "banana", "table"
]


# =============================================
# Part 1 - Words with specific prefixes 
# =============================================

print("=======\nPart 1\n=======")

'''
Matching words starting with 'un-':

To find words that begin with the prefix 'un-', we can use regex: '^un\w+'
-   '^': This is an anchor that asserts the position at the start of the string.
-   'un': These are literal characters that match the sequence 'un' exactly.
-   '\w+': This is a character class and a quantifier combination. '\w' matches any word character (alphanumeric character and underscore: '[a-zA-Z0-9_]'), 
    and '+' means one or more occurrences of the preceding element. 
    So, '\w+' matches one or more word characters following 'un'.
'''

# Example usage -- using the "list comprehension" way

un_prefix_words = [x for x in words if re.match(r'^un\w+', x)]

# Alternative method using for loops:
un_prefix_words_v2 = []

for w in words:
  if re.match(r'^un\w+', w):
    un_prefix_words_v2.append(w)
  else:
    pass

print(f"Words starting with 'un-': {un_prefix_words}")
print(f"\nWords starting with 'un-' version 2: {un_prefix_words}")

# Step 1: Retrieve all of the "un-" prefixed words in the Brown corpus
# Step 2: Store them in the variable brown_un_words.
# Step 3: Output will show the first 20 un-words below.

brown_all_words = nltk.corpus.brown.words()                                              # get all the words in the Brown corpus as a list                                  
brown_un_words = [word for word in brown_all_words if re.match(r'^un\w+', word)]         # list comprehension to find all the words that start with 'un-' & store them in brown_un_words  
print(brown_un_words[:20])                                                               # print the first 20 un-words in the Brown corpus


# =============================================
# Part 2 - Words with specific suffixes 
# =============================================

print("=======\nPart 2\n=======")

'''
Matching words ending with '-ation':

To find words that end with the suffix '-ation', we can use the regular expression '\w+ation$'.

*   '\w+': This is a **character class** and a **quantifier** combination. 
    '\w' matches any word character (alphanumeric character and underscore: '[a-zA-Z0-9_]'), 
    and '+' means one or more occurrences of the preceding element. 
    This matches the base form of the word before the suffix.
*   'ation': These are **literal characters** that match the sequence 'ation' exactly.
*   '$': This is an **anchor** that asserts the position at the end of the string. 
    It ensures that 'ation' is at the very end of the word.
'''

ation_suffix_words = [word for word in words if re.search(r'\w+ation$', word)]
print(f"Words ending with '-ation': {ation_suffix_words}")

"""
Matching words ending with '-ness':

TODO: Write a code to find a list of all the words that end in '-ness' in the Brown corpus, 
and use a print statement to show the first 20 words, alphabetically.
"""

ness_suffix_words = [word for word in brown_all_words if re.search(r'\w+ness$', word)]
ness_suffix_words.sort() # alphabetically sorted

print(f"Words ending with '-ness': {ness_suffix_words[:20]}")


# =============================================
# Part 3 - Extracting base forms and affixes using capturing groups
# =============================================

print("=======\nPart 3\n=======")

'''
Capturing groups in regular expressions allow you to extract specific parts of a matched string. 
They are defined by enclosing the part of the pattern you want to capture within parentheses '()'. 
When a match is found, the text matched by each capturing group can be retrieved separately.

This is particularly useful in morphological analysis for separating affixes from base words, enabling a more granular examination of word structure.

Extracting 'un-' prefix and base word:

To extract the 'un-' prefix and the base word from words starting with 'un-', 
we can modify our previous regex pattern to include capturing groups: '^(un)(\w+)$'.

*   '^': Asserts the position at the start of the string.
*   '(un)': This is the **first capturing group**. It matches the literal sequence 'un' and captures it.
*   '(\w+)': This is the **second capturing group**. It matches one or more word characters (`[a-zA-Z0-9_]`) and captures them, representing the base word.
*   '$': Asserts the position at the end of the string.
'''

un_extracted = []
for word in brown_all_words:
    match = re.match(r'^(un)(\w+)$', word)
    if match:
        un_extracted.append({'word': word, 'prefix': match.group(1), 'base': match.group(2)})

print(f"Extracted 'un-' prefix and base words: {un_extracted}")

"""
Extracting base word and '-ness' suffix:

TODO: Write a code to extract all the bases of words with a '-ness' suffix. Print out the last 20 bases in the list.
"""

ness_extracted = []
for word in brown_all_words:
    match = re.match(r'^(\w+)(ness)$', word)
    if match:
        ness_extracted.append({'word': word, 'suffix': match.group(2), 'base': match.group(1)})

print(f"Extracted '-ness' suffix and base words: {ness_extracted}")


# =============================================
# Part 4 - Comparing comparative strategies
# =============================================

print("=======\nPart 4\n=======")

'''
As we saw in class, English has two strategies to form the comparative, a synthetic -er affix 
and an analytic "more X" strategy. Using what you have learned so far, 
gather data and provide a brief, speculative analysis about some possible 
differences between bases that use one or there other strategy. 

Some possible questions to investigate:
- Which strategy has the most tokens? Which has the most unique base types?
- How long is the average base in the synthetic vs analytic category?
- Are there any bases which are found in both categories?
'''

# -er affix analysis of the words in the brown corpus
er_extracted = []
for word in brown_all_words:
    match = re.match(r'^(\w+)(er)$', word)
    if match:
        er_extracted.append({'word': word, 'suffix': match.group(2), 'base': match.group(1)})

print(f"Extracted '-er' suffix and base words: {er_extracted}")

# Token count for each affix
er_tokens = len(er_extracted)
ness_tokens = len(ness_extracted)
un_tokens = len(un_extracted)

# Simple unique base count 
# creating sets of the base words for each affix to find unique base types and avoid duplicates
# for loops to extract the base words from the lists
er_unique_bases = set([base['base'] for base in er_extracted]) 
ness_unique_bases = set([base['base'] for base in ness_extracted])
un_unique_bases = set([base['base'] for base in un_extracted])

# results
print(f"Tokens for '-er': {er_tokens}")
print(f"Tokens for '-ness': {ness_tokens}")
print(f"Tokens for '-un': {un_tokens}")
print(f"Unique base types for '-er': {er_unique_bases}")
print(f"Unique base types for '-ness': {ness_unique_bases}")
print(f"Unique base types for 'un-': {un_unique_bases}")

# =============================================
# Part 5 - Findings report
# =============================================
'''
Tokens for '-er': 28515
Tokens for '-ness': 1442
Tokens for '-un': 4479

-er affix is extremely prevalent as a token, appearing 28,515 times, -ness appears 1142 times and -un prefix appears 4479 times.
 
It makes sense as the morpheme -er can transform any verb into a comparative adjective or an agent noun so it can
attach to a wide variety of bases, while -ness is more limited in its application and can only attach to adjectives to form nouns, 
and the prefix un- is also limited in its application as it typically attaches to adjectives and some verbs to form their negative or opposite forms. 
'''
