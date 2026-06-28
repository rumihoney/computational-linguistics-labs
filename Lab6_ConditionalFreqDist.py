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

'''
A conditionalFreqDist store counts, not probabilities. To get P(word | genre) you need to divide by the total number of tokens for that genre — which is fd.N() or equivalently fd.freq(word).

Exercise 2.1 — Compute P(word | genre) for some words

Using the function below, explore the probability of "romance" and "police" in the "news" and "romance" genres. An example usage is given, you can copy/paste and change the word/genre.
'''

def cond_prob(cfd, condition, event):
    """
    Returns P(event | condition) using the given CFD.
    """
    return cfd[condition].freq(event)

# Test it — these should be small positive numbers (not zero, not 1)
print("P('police' | 'news')     =", cond_prob(cfd_genre, 'news', 'police'))
# Add your tests below
print("P('romance' | 'news')    =", cond_prob(cfd_genre, 'news', 'romance'))
print("P('police' | 'romance')  =", cond_prob(cfd_genre, 'romance', 'police'))

'''
Exercise 2.2 — Build a comparison table
Use your cond_prob function to fill in the table below. Pick 5 words that you expect to behave differently across genres. One of them should be a function word (like the, a, of) as a baseline.

Choose your genres from: news, romance, humor, government, hobbies, religion, science_fiction, mystery
'''

# Define your words and genres
my_words  = ['the', 'love', 'money', 'christmas', 'food']   
my_genres = ['news', 'romance', 'government', 'religion']     

# Print comparison table
header = f"{'word':<18}" + "".join(f"{g:<16}" for g in my_genres)
print(header)
print("-" * len(header))

for word in my_words:
    row = f"{word:<18}"
    for genre in my_genres:
        p = cond_prob(cfd_genre, genre, word)
        row += f"{p:<16.6f}"
    print(row)


'''
Look at the row for your function word. What do you notice about its probability across genres, compared to your content words? 
What does this tell you about what conditional probability on genre is actually measuring?

This tells us that function words like 'the' have similar probabilities across genres, while content words like 'love', 'money', 'christmas', and 'food' show more variation. 
This indicates that conditional probability on genre captures contextual differences between genres, as content words are more genre-specific while function words are more universal.
'''

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
