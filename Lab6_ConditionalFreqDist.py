'''
Lab 6 — NLTK Conditional Frequency Distributions
Computational Methods in Linguistics

This lab introduces the core concepts of conditional frequency distributions (CFDs) in NLTK, which are a powerful tool for analyzing linguistic data.

Conditional frequency distributions are a way to count frequencies of items (like words) conditioned on some other variable (like genre, part of speech, etc.).
In NLTK, we can create a CFD using the 'nltk.ConditionalFreqDist' class.
'''

import nltk
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

Using the function below, explore the probability of "romance" and "police" in the "news" and "romance" genres. 
An example usage is given, you can copy/paste and change the word/genre.
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

Use your cond_prob function to fill in the table below. Pick 5 words that you expect to behave differently across genres. 
One of them should be a function word (like the, a, of) as a baseline.

Choose your genres from: news, romance, humor, government, hobbies, religion, science_fiction, mystery
'''

# Define your words and genres
my_words  = ['the', 'love', 'money', 'christmas', 'food']   
my_genres = ['news', 'romance', 'government', 'science_fiction', 'mystery']     

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

'''
NLTK's built-in .tabulate() method gives a quick count-based overview. For probability-based comparison, we'll build a simple bar chart.

Exercise 3.1 — Tabulate

The .tabulate() method shows raw counts (not probabilities) for a selection of words across conditions.
'''

# Tabulate selected words across 4 genres
cfd_genre.tabulate(
    conditions=['news', 'romance', 'government', 'humor'],
    samples=['the', 'police', 'love', 'federal', 'laughed']
)

'''
Exercise 3.2 — Plot conditional probabilities

The function below plots P(word | genre) for a list of words across genres. Complete the missing line, then run it for your chosen words.
'''

def plot_cond_probs(cfd, words, genres, title="Conditional Probability by Genre"):
    # Bar chart of P(word | genre) for each word across genres.
    import numpy as np
    n_words  = len(words)
    n_genres = len(genres)
    x = np.arange(n_words)
    width = 0.8 / n_genres
    colours = ['#065A82', '#0D9488', '#B85042', '#F5A623',
               "#6B3FA0", '#2E7D32', '#795548', '#0288D1']

    fig, ax = plt.subplots(figsize=(10, 4.5))
    for i, genre in enumerate(genres):
        probs = [cond_prob(cfd, genre, word) for word in words]

        ax.bar(x + i * width, probs, width, label=genre, color=colours[i % len(colours)], alpha=0.85)

    ax.set_xticks(x + width * (n_genres - 1) / 2)
    ax.set_xticklabels(words, rotation=15, ha='right', fontsize=11)
    ax.set_ylabel("P(word | genre)", fontsize=11)
    ax.set_title(title, fontsize=13, fontweight='bold')
    ax.legend(fontsize=10)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.tight_layout()
    plt.savefig("lab6_plot1.png", dpi=120)
    plt.show()
    print("Plot saved as lab6_plot1.png")

# Call it with your chosen words and genres
plot_cond_probs(
    cfd_genre,
    words=['police', 'love', 'federal', 'god', 'laughed'],
    genres=['news', 'romance', 'government', 'religion', 'humor'],
    title="P(word | genre) — Brown Corpus"
)


'''
word 'god' is expected to have a high probability in the 'religion' genre and low probabilities in other genres. 
This illustrates how conditional probabilities can highlight the contextual relevance of words across different genres.
'''

# ======================================================
# Part 4 — Conditioning on Something Other Than Genre
# ======================================================
print("=======\nPart 4\n=======")

'''
So far the condition has been genre. But ConditionalFreqDist works with any condition you can extract from the data.

In this part, you'll build a CFD where the condition is a part-of-speech tag and the event is the word. This lets you ask: given that we're looking at nouns, what are the most frequent ones?

Exercise 4.1 — Build a POS x word CFD

The Brown corpus comes with POS-tagged words. brown.tagged_words(tagset='universal') gives you (word, tag) pairs using a simplified 12-tag set.
'''

# Preview the tagged words
sample = brown.tagged_words(categories='news', tagset='universal')[:20]
for word, tag in sample:
    print(f"  {word:<20} {tag}")

# Build a CFD: condition = POS tag, event = lowercased word
cfd_pos = ConditionalFreqDist(
    (tag, word.lower())
    for word, tag in brown.tagged_words(tagset='universal')
)
print("POS tags (conditions):", cfd_pos.conditions())

'''
Exercise 4.2 — Most frequent words per POS tag

For each of the four POS tags below, print the top 10 most frequent words.
'''

for tag in ['NOUN', 'VERB', 'ADJ', 'ADV']:
    print(f"\n--- Top 10 {tag}s ---")
    for word, count in cfd_pos[tag].most_common(10):
        print(f"  {word:<20} {count:>6}")

'''
Look at the top 10 NOUNs. Several of them are probably not what you'd expect from a "list of nouns" — they might look like function words or auxiliaries. 
Why might this happen? (Hint: think about how the universal tagset works and what "noun" covers.)

This happens because the universal tagset simplifies the original Brown corpus tags, and some words that are not strictly nouns (like pronouns or certain determiners) may be tagged as NOUNs. 
Additionally, common words that can function as multiple parts of speech may be tagged as NOUNs in certain contexts, leading to unexpected entries in the top 10 list.
'''

# ======================================================
# Part 5 — My Own Question
# ======================================================
print("=======\nPart 5\n=======")

'''
This is the open-ended part. Design and answer a small linguistic question using ConditionalFreqDist.

Requirements

your question must:
*   Use a different condition than the ones above (not just genre or POS tag repeated), OR use the same condition to ask a genuinely different question
*   Produce at least one piece of visible output (a table, a plot, or printed counts)
*   Be answerable with the tools you've used today

Step 1 — State your question(s):
*   Gendered language by genre: Are words like he, she, his, her distributed differently across genres? What does the ratio tell you?
*   Modal verbs by genre: How does the frequency of must, should, might, can vary? What does this suggest about epistemic vs. deontic modality across text types?
*   High-frequency verbs by genre: Does the most common verb differ by genre? Build a CFD where condition = genre and look at what the top VERB is in each.
*   Word length by genre: Build a CFD where condition = genre and event = word length (len(word)). Do some genres use longer words on average?

Step 2 — Plan your CFD and analysis:
*   What is the condition (the A in P(B | A))?
*   What is the event (the B in P(B | A))?
*   What corpus or data will you use?
*   What output will you produce (table, plot, counts)?

Step 3 — Build and run it:

Step 4 — Interpret:

In 2–4 sentences, describe what you found. Does the result support your initial expectation? Is there anything in the output you can't fully explain?
'''
# ======================================================

'''
Step 1 — State your question(s): Robots vs. humans: Build a CFD where condition = genre and event = whether the word is a robot-related term (like robot, android, AI) or not. 
Are robots more common in science fiction than other genres?

Step 2 — Plan your CFD and analysis:
*   Condition = genre
*   Event = robot-related term (robot, android, AI, cyborg, etc.)
*   Corpus = Brown corpus
*   Output = table of counts and a bar plot

Step 3 — Build and run it:
'''

robot_terms = {'robot', 'android', 'ai', 'cyborg', 'automation', 'machine', 'artificial', 'intelligence', 'droid', 'clanker'}

# Function to check if a word is robot-related
def is_robot_related(word):
    return word.lower() in robot_terms

# Build CFD: condition = genre, event = robot-related word
cfd_robot = ConditionalFreqDist(
    (genre, word.lower())
    for genre in brown.categories()
    for word in brown.words(categories=genre)
    if is_robot_related(word)
)

# Print table of robot-related terms by genre
print("Robot-related word counts by genre:")
cfd_robot.tabulate(
    conditions=brown.categories(),
    samples=sorted(robot_terms)
)

# Total robot-related words per genre
print("\nTotal robot-related words per genre:")
for genre in brown.categories():
    total = cfd_robot[genre].N()
    print(f"{genre:<18} {total}")
    
# Plot total robot-related words by genre
def plot_robot_counts(cfd, genres, title="Robot-related Words by Genre"):
    import numpy as np

    counts = [cfd[genre].N() for genre in genres]
    x = np.arange(len(genres))

    fig, ax = plt.subplots(figsize=(11, 4.5))

    ax.bar(x, counts, color="#6B3FA0", alpha=0.85)

    ax.set_xticks(x)
    ax.set_xticklabels(genres, rotation=45, ha='right')
    ax.set_ylabel("Frequency of robot-related terms")
    ax.set_title(title, fontsize=13, fontweight='bold')

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    plt.tight_layout()
    plt.savefig("lab6_robot_plot2.png", dpi=120)
    plt.show()

    print("Plot saved as lab6_robot_plot2.png")


# Call the plotting function
plot_robot_counts(
    cfd_robot,
    genres=brown.categories(),
    title="Robot-related Words — Brown Corpus"
)

'''
Step 4 — Interpret:

The results did not support my original hypothesis. Although I expected science fiction to contain the highest number of robot-related words, 
the learned and government genres contained many more occurrences. This is because most of the matches came from words such as "machine", "artificial", and "intelligence", 
which are often used in scientific, technical, or political contexts rather than to describe robots. 

In addition, the Brown corpus was compiled in the 1960s, before modern AI and robotics vocabulary became common in science fiction so it's not surprising that the science fiction genre did not contain many robot-related words.
'''