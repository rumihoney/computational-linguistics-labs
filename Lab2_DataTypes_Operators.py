'''
Lab 2 — Python Data Types, Sets, and Functions
Computational Methods in Linguistics

Theme: Phonology, Natural Classes, and Features

This lab explores how Python's data types (lists, sets, and dictionaries) can be used to represent linguistic data and generalizations.
It will cover how sets can model natural classes of segments, and how dictionaries can represent feature matrices.
'''

# ======================================================
# Part 1: Lists vs. Sets
# ======================================================

print("=======\nPart 1\n=======")

segments_list = ["t", "k", "t", "p", "b", "d", "t"]

segments_set = set(segments_list)                                                         # Segment_list to segment_set conversion 

print("List:", segments_list)
print("Set:", segments_set)
print("Length of list:", len(segments_list))
print("Length of set:", len(segments_set))


# ======================================================
# Part 2: Defining Natural Classes with Sets
# ======================================================

print("=======\nPart 2\n=======")

consonants = {"p", "t", "k", "b", "d", "g", "m", "n"}
vowels = {"a", "e", "i", "o", "u"}
voiced = {"b", "d", "g", "m", "n"}
nasal = {"m", "n"}

voiceless_consonants = consonants - voiced                                                # consonant - voiced = voiceless
voiced_oral_consonants = voiced - nasal                                                   # voiced - nasal = voiced oral 

print("Voiceless consonants:", voiceless_consonants)
print("Voiced oral consonants:", voiced_oral_consonants)


# ======================================================
# Part 3: Membership and Subsets
# ======================================================

print("=======\nPart 3\n=======")

is_m_consonant = "m" in consonants                                                       # Check if 'm' is in the set of consonants
nasal_is_subset = nasal <= consonants                                                    # Check if nasal is a subset of consonants

print("Is 'm' a consonant?", is_m_consonant)
print("Are nasals a subset of consonants?", nasal_is_subset)


# ======================================================
# Part 4: Dictionaries as Feature Mappings
# ======================================================

print("=======\nPart 4\n=======")

feature_dict = {
    "p": {"-voice", "-nasal"},
    "b": {"+voice", "-nasal"},
    "m": {"+voice", "+nasal"},
    "t": {"-voice", "-nasal"},
}

m_features = feature_dict["m"]                                                          # Retrieve the feature set for 'm'
m_is_nasal = "+nasal" in m_features                                                     # Check if '+nasal' is one of its features

print("Features of 'm':", m_features)
print("Is 'm' nasal?", m_is_nasal)


# ======================================================
# Part 5: Functions for Natural Class Size
# ======================================================

print("=======\nPart 5\n=======")

def natural_class_size(class_set):
    return len(class_set)                                                               # returns the number of segments in the class 
print("Number of vowels:", natural_class_size(vowels))
# can reuse the function to find the size of any natural class, for example:
print("Number of voiced consonants:", natural_class_size(voiced))


# ======================================================
# Part 6: Reflection 
# ======================================================

'''
1. Why are sets a good model for natural classes?
    Sets are a good model for natural classes because they contain no duplicates and can implement set theory.
    It's also very useful when counting segments or dealing with other arithmetics operations.

2. When would a list be a better choice than a set?
    A list would be a better choice than a set if we are dealing with segments that require a specific order and when dealing with repetition.
    for example looking at the frequency of a verb in sentences in a string.

3. How do dictionaries relate to feature matrices?
    Since dictionaries represent relational aspects between keys (sets) and other values, we can use dictionaries for linguistic feature matrices 
    to store keys such as vowels and then their features such as whether it's voiced or nasalized.
'''