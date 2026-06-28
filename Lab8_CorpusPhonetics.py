'''
Lab 8 — Corpus Phonetics with pandas
Computational Methods in Linguistics

This lab explores the data from Buckeye Corpus — conversational speech from 40 speakers in Columbus, Ohio. 
The dataset tracks what happens to word-final /t/ and /d/ in connected speech: are they tapped, glottalized, deleted, or released?

You'll use pandas (Python's standard library for tabular data) instead of NLTK today.
'''

# ======================================================
# Part 1 — Load & Explore
# ======================================================
print("=======\nPart 1\n=======") 

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("buckeye_data_withLmProbs.csv")
print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")
df.head()

'''
Key columns for today's lab:

Column:                                         What it is:

orthography:                                    The word (e.g. "but", "get")
underlying_final:                               Underlying consonant: /t/ or /d/
Outcome:                                        How it was pronounced: tap, glot, deleted, other
word_duration:                                  Duration in seconds
sylls:                                          Monosyllabic or polysyllabic
following_pause:                                None = next word follows immediately
speaker:                                        Speaker ID (s01–s40)
SUBTLWF:                                        Word frequency (higher = more common)
logWordLmProb                                   Log probability from a language model


Pick 3 column names from df.columns and write a one-sentence guess about what each contains:
*   orthography: the actual word being spoken (e.g., "but", "get")
*   outcome: how the final consonant is pronounced (tap, glot, deleted, etc.)
*   word_duration: how long the word lasts in seconds
'''

# ======================================================
# Part 2 — Counting Outcomes
# ======================================================
print("=======\nPart 2\n=======") 


df["Outcome"].value_counts()

# What proportion does each outcome represent?
df["Outcome"].value_counts(normalize=True).round(3)

# Does the underlying consonant matter?
pd.crosstab(df["underlying_final"], df["Outcome"], normalize="index").round(3)

# Notice: glottalization is almost exclusively a /t/ phenomenon. Why might that be?

# Create a cross-tabulation of 'Outcome' by 'sylls' (mono vs. poly). Use 'normalize="index"'.  
# Which syllable type has more deletion?

pd.crosstab(df["sylls"], df["Outcome"], normalize="index").round(3)

'''
Interpretation:

Monosyllabic words tend to have more deletion than polysyllabic words.
This may be because shorter words tend to be more common?
'''


# ======================================================
# Part 3 — Following Context
# ======================================================
print("=======\nPart 3\n=======") 

# One of the strongest effects on /t,d/ realization is whether another word follows immediately or there's a pause.

# Simplify pause into two categories
df["pause"] = df["following_pause"].apply(lambda x: "pause" if x != "NaN" else "no_pause")
pd.crosstab(df["pause"], df["Outcome"], normalize="index").round(3)

# Before another word, tapping dominates (64%). Before a pause, it nearly disappears (1.5%) — replaced by glottalization and released variants. 
# Why? Because tapping is a coarticulatory process that requires another word to follow, while glottalization and release are more common in final position.

# Make a bar chart of this pattern. Describe it in 1–2 sentences below the chart.
ct_pause = pd.crosstab(df["pause"], df["Outcome"], normalize="index")

ct_pause.plot(kind="bar", figsize=(8, 5))
plt.title("Realization of final /t,d/ by following context")
plt.ylabel("Proportion")
plt.xlabel("Following context")
plt.xticks(rotation=0)
plt.legend(title="Outcome")
plt.tight_layout()
plt.show()

# Tapping is much more frequent when there is no pause (continuous speech).
# Before a pause, tapping drops and glottalization or release increases,


# ======================================================
# Part 4 — Frequency & Predictability
# ======================================================
print("=======\nPart 4\n=======") 

# Words that are more frequent or predictable tend to be reduced — shorter, with more deletion/tapping. (Recall Bell et al., 1999 from Weeks 8–9.)

# Average word duration by outcome
df.groupby("Outcome")["word_duration"].mean().round(4)

# Average language model probability by outcome
# (less negative = more probable)
df.groupby("Outcome")["logWordLmProb"].mean().round(4)

# Deleted words are shortest and most probable. Released words are longest and least probable. This fits the prediction: more predictable → more reduction.

# Box plot of duration by outcome
df.boxplot(column="word_duration", by="Outcome", figsize=(8, 5))
plt.suptitle("")
plt.title("Word duration by realization")
plt.ylabel("Duration (seconds)")
plt.tight_layout()
plt.show()

'''
The 'SUBTLWF' column has raw word frequency (some values are "NA").
    (a) Convert it to numeric  
    (b) Get mean frequency per Outcome  
    (c) Is this consistent with the language model results above?
'''

df["SUBTLWF"] = pd.to_numeric(df["SUBTLWF"], errors="coerce")
df.groupby("Outcome")["SUBTLWF"].mean().round(2)

'''
Interpretation:
It seems like words that are deleted or tapped tend to have a higher frequency. 
This is consistent with the language model results: more frequent and predictable words are reduced more in speech.
'''


# ======================================================
# Part 5 — Speaker Variation
# ======================================================
print("=======\nPart 5\n=======") 

# Tapping rate per speaker
df["is_tapped"] = (df["Outcome"] == "tap").astype(int)
tap_rate = df.groupby("speaker")["is_tapped"].mean().sort_values()

tap_rate.plot(kind="bar", figsize=(12, 5), color="steelblue")
plt.title("Tapping rate by speaker")
plt.ylabel("Proportion tapped")
plt.xlabel("Speaker")
plt.tight_layout()
plt.show()


# Pick two speakers with very different tapping rates & compare their full outcome distributions.

speaker1 = df[df["speaker"] == "s01"]
speaker2 = df[df["speaker"] == "s02"]

print("Speaker 1:")
print(speaker1["Outcome"].value_counts(normalize=True).round(3))
print("\nSpeaker 2:")
print(speaker2["Outcome"].value_counts(normalize=True).round(3))

'''
How do these two speakers differ? 
*   Speaker 1 uses much less tapping and shows more glottalization or deletion, while Speaker 2 taps much more frequently.
*   This shows that pronunciation isn’t just about the word or context: different speakers have their own speaking styles.
*   These differences are linked to speaker identity, since factors like habit, accent, and personal speech patterns influence how sounds are produced.
'''

# ======================================================
# Part 6 — Reflection
# ======================================================
print("=======\nPart 6\n=======") 

'''
What factors influence how a speaker realizes word-final /t/ or /d/?

Draw on at least two of: underlying voicing, following context, word frequency, speaker identity. Connect your findings to ideas from Weeks 8–9.

*   Several factors affect how speakers pronounce word-final /t/ or /d/. First, the underlying sound matters, since /t/ is much more likely to be glottalized.
*   The context is also really important: when another word comes right after, tapping is much more common, but before a pause, speakers tend to pronounce sounds more clearly.
*   It seems like word frequency plays a role too, more common and predictable words appear to be reduced more frequently which indicates deletion or taping.
*   Finally, speaker identity matters because different speakers show different patterns, meaning pronunciation isn’t completely uniform.
*   This matches what we saw in Weeks 8–9, where more predictable words tend to be reduced in natural speech.
'''

# ======================================================
# Part 7 — Bonus
# ======================================================
print("=======\nPart 7\n=======") 

#   A.The most common words  — Do the top-10 words behave differently?

top_words = df["orthography"].value_counts().head(10).index.tolist()
top_df = df[df["orthography"].isin(top_words)]
pd.crosstab(top_df["orthography"], top_df["Outcome"], normalize="index").round(3)

#   B. Bigram predictability — Does logCondLmProb (conditional probability of the next word) predict more tapping/deletion?
# write your exploration here: 

#   C. Summary function 
def outcome_summary(word):
    subset = df[df["orthography"] == word]
    if len(subset) == 0:
        print(f"Word '{word}' not found.")
        return
    print(f"\n'{word}' (n={len(subset)}):")
    print(subset["Outcome"].value_counts(normalize=True).round(3))
    print(f"Mean duration: {subset['word_duration'].mean():.3f}s")

outcome_summary("that")
outcome_summary("about")