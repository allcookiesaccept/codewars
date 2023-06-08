"""
In this kata you are required to, given a string, replace every letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

"a" = 1, "b" = 2, etc.
"""
# ord(char) = index
# chr(97) = char

def alphabet_position(text):

    chars = [x.lower() for x in text]
    result = []

    for char in chars:
        char_index = ord(char)
        if char_index < 123 and char_index > 96:
            position = char_index - 96
            result.append(position)

    return ' '.join(str(x) for x in result)


def alphabet_position_best_practice(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())
