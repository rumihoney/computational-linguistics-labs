"""
Lab 6 — NLTK Conditional Frequency Distributions
Computational Methods in Linguistics

This lab aims to introduce you to the concept of conditional frequency distributions (CFDs) in NLTK, which are a powerful tool for analyzing linguistic data.

By the end of this lab, you should be able to:
Built a conditional frequency distribution over the Brown corpus
Computed conditional probabilities from it
Compared distributions across conditions using tabulation and plotting
Designed and answered a small linguistic question of your own

Conditional frequency distributions are a way to count frequencies of items (like words) conditioned on some other variable (like genre, part of speech, etc.).
In NLTK, we can create a CFD using the 'nltk.ConditionalFreqDist' class.
"""


import random

animals = {'koala', 'tiger', 'dragon','axolotl'}
objects = {'tomato', 'pizza', 'coin'}
verbs = {'yawned', 'devoured', 'put'}
adverbs = {'there', 'down'}

print(f"Random sentence:\n The {random.choice(list(animals))} {random.choice(list(verbs))} the {random.choice(list(objects))} {random.choice(list(adverbs))}")

more_verbs = {'arrived','slept','bought','loved','heard','confessed'}
food_objects = {'tomato', 'pizza'}
other_objects = {'coin'}

chosen_object = random.choice(list(objects)) 

if chosen_object in food_objects:
    adverb = 'over there'
else:
    adverb = 'down'

print(f"Random sentence, pt 2:\n The {random.choice(list(animals))} {random.choice(list(verbs))} the {chosen_object} {adverb}")

# ======================================================
# Part 1 — Building a Conditional Frequency Distribution
# ======================================================

# ======================================================
# Part 2 — From Counts to Conditional Probabilities
# ======================================================

# ======================================================
# Part 3 — Tabulating and Plotting 
# ======================================================

# ======================================================
# Part 4 — Conditioning on Something Other Than Genre
# ======================================================

# ======================================================
# Part 5 — My Own Question
# ======================================================
