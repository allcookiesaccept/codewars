# https://www.codewars.com/kata/5264d2b162488dc400000001

# Write a function that takes in a string of one or more words, and returns the same string, but with all five or
# more letter words reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces.
# Spaces will be included only when more than one word is present.

def spin_words(string):

    words = string.split(' ')
    new_words = []

    for word in words:
        if len(word) < 5:
            new_words.append(word)
        else:
            word = word[::-1]
            new_words.append(word)

    return " ".join(x for x in new_words)

def spin_words_best_practice(sentence):
    # Your code goes here
    return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])