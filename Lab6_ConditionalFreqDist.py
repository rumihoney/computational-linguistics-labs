'''
Lab 6 — NLTK Conditional Frequency Distributions
Computational Methods in Linguistics

This lab introduces the core concepts of conditional frequency distributions (CFDs) in NLTK, which are a powerful tool for analyzing linguistic data.

Conditional frequency distributions are a way to count frequencies of items (like words) conditioned on some other variable (like genre, part of speech, etc.).
In NLTK, we can create a CFD using the 'nltk.ConditionalFreqDist' class.
'''

import nltk
import math
from nltk import FreqDist, ConditionalFreqDist
from nltk.corpus import brown
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

nltk.download('brown', quiet=True)
nltk.download('universal_tagset', quiet=True)

print("Brown corpus genres:", brown.categories())
print("Total words:", len(brown.words()))

# ======================================================
# Part 1 — Building a Conditional Frequency Distribution
# ======================================================
print("=======\nPart 1\n=======")

'''A ConditionalFreqDist (CFD) is NLTK's way of storing a separate FreqDist for each condition.
You build one by giving it a list of (condition, event) pairs:

ConditionalFreqDist(
    (condition, event)
    for each item in your data
)

The condition can be whatever you want:a genre, a word, a POS tag, a speaker. 
The event is what you're counting within each condition.

Exercise 1.1 — Build a genre x word CFD

The cell below builds a CFD where:
*   condition = genre(e.g. 'news', 'romance')
*   event = word (lowercased)
'''

# Build the CFD: condition = genre, event = lowercased word
cfd_genre = ConditionalFreqDist(
    (genre, word.lower())
    for genre in brown.categories()
    for word in brown.words(categories=genre)
)

print("Number of conditions:", len(cfd_genre.conditions()))     # Number of conditions: 15
print("Conditions:", cfd_genre.conditions())                    


'''
Exercise 1.2 — Inspect a single condition

Each condition in the CFD gives you a FreqDist. Access it like a dictionary: cfd_genre['news']:
'''

# Looking at the FreqDist for the 'news' genre
fd_news = cfd_genre['news']

print("Total tokens in 'news':", fd_news.N())
print("Unique types in 'news':", fd_news.B())
print()
print("Top 15 words in 'news':")
for word, count in fd_news.most_common(15):
    print(f"  {word:<20} {count:>5}")

'''
In one sentence, explain what cfd_genre['news'] returns and how it's different from cfd_genre itself:

cfd_genre['news'] returns a FreqDist object containing the frequency distribution of words in the 'news' genre, 
while cfd_genre itself is a ConditionalFreqDist object that contains separate FreqDist objects for each genre.

'''

# ======================================================
# Part 2 — From Counts to Conditional Probabilities
# ======================================================
print("=======\nPart 2\n=======")



# ======================================================
# Part 3 — Tabulating and Plotting 
# ======================================================
print("=======\nPart 3\n=======")



# ======================================================
# Part 4 — Conditioning on Something Other Than Genre
# ======================================================
print("=======\nPart 4\n=======")



# ======================================================
# Part 5 — My Own Question
# ======================================================
