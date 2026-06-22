'''
Lab 3 — Control Flow and Simple Functions
Computational Methods in Linguistics

Themes: Phonological Rules, Patterns, Conditionals,Control Flow, and Functions

This lab explores how Python makes decisions (control flow)
and how functions let us formalize linguistic generalizations.

Phonological patterns look like rules or generalizations.
In Python, these are expressed with IF statements (conditionals) and functions.
'''

# ======================================================
# Part 0 — Basic Control Flow with if / else
# ======================================================

segments = {"p", "b", "t", "d", "s", "m"}
voiceless_stops = {"p", "t", "k"}

print("=======\nPart 0\n=======")

for seg in segments:
    if seg in voiceless_stops:
        print(seg, "is a voiceless stop")
    else:
        print(seg, "is NOT a voiceless stop")


# ======================================================
# Part 1 — Testing a Phonological Rule
# ======================================================

print("=======\nPart 1\n=======")

segment = "s"

if segment in voiceless_stops:
    print(f"With segment {segment}: rule applies, it is a voiceless stop")
else:
    print(f"With segment {segment}: rule does not apply, it is NOT a voiceless stop")
    

# ======================================================
# Part 2 — Simple Function
# ======================================================

print("=======\nPart 2\n=======")

def is_voiceless_stop(segment):
    if segment in voiceless_stops:                            # takes a segment as input
        return True                                           # returns True if it's a voiceless stop
    else:                        
        return False                                          # returns False if NOT voiceless stop
    
print("Test 'p':", is_voiceless_stop("p"))                    # True
print("Test 'm':", is_voiceless_stop("m"))                    # False


# ======================================================
# Part 3 — Testing the Function
# ======================================================
print("=======\nPart 3\n=======")

print("Voiceless stop, true or false?")
for seg in segments:
    result = is_voiceless_stop(seg)    # True/False
    print(f'{seg} is:', result)
    

# ======================================================
# Part 4 — Adding a Second Condition
# ======================================================

print("=======\nPart 4\n=======")

nasals = {"m", "n"}
print('Nasals:', nasals)

print("Voiceless stop or a nasal? (true) or neither? (false)")
def is_special_segment(segment):
    if (segment in voiceless_stops) or (segment in nasals):
        return True                                           # returns true if it's either or 
    else:
        return False                                          # returns false if it's neither
    
for seg in segments:
    print(seg, is_special_segment(seg))


# ======================================================
# Part 5 — Collecting Data
# ======================================================
print("=======\nPart 5\n=======")

word_list = ["pop","pik","map","mom","blak","zum"]
words_with_vcls_stops = list()                                # initialize an empty list to store words with voiceless stops
for word in word_list:                                        # loop through each word in the list
    for seg in word:                                          # loop through each segment in the word
        if is_voiceless_stop(seg):                            # check if segment is a voiceless stop
            words_with_vcls_stops.append(word)                # add word in the result list
            break                                             # stop the loop = avoid duplicates
print("words with voiceless stops:",words_with_vcls_stops)    # display result


# ======================================================
# Part 6 - Feature Dictionary
# ======================================================

print("=======\nPart 6\n=======")

feature_dict = {
    "p": {"-voice", "-nasal","+labial"},
    "b": {"+voice", "-nasal","+labial"},
    "m": {"+voice", "+nasal","+labial"},
    "t": {"-voice", "-nasal","+coronal"},
    "d": {"+voice", "-nasal","+coronal"},
    "n": {"+voice", "+nasal","+coronal"}
}
# print("Feature dictionary:", feature_dict)

def segments_with_feature(feature):
    result = list()                                           # initialize an empty list to store segments with the specified feature
    for segment in feature_dict:                              # loop through each segment in the feature_dict
        if feature in feature_dict[segment]:                  # check if segment has the feature
            result.append(segment)                            # if segments share the same feature value = add to result list
    return result

# For example, the following function call should
# output "m" and "n", based on feature_dict
print("Segments with +nasal:", segments_with_feature("+nasal"))
# Example #2, will output 'p', 't' as they both share the feature -voice
print('Segments with -voice:', segments_with_feature("-voice"))

# If I want a function that checks for more than 2 features:
# def segments_with_features(feature1, feature2):
#     result = list()
#     for segment in feature_dict:
#         if feature1 in feature_dict[segment] and feature2 in feature_dict[segment]:
#             result.append(segment)
#     return result
# print('Segments with -voice and -nasal:', segments_with_features('-voice','-nasal'))