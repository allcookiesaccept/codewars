# https://www.codewars.com/kata/525f50e3b73515a6db000b83

# Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.

def create_phone_number(array):

    return f'({"".join(str(x) for x in array[:3])}) ' \
           f'{"".join(str(x) for x in array[3:6])}-{"".join(str(x) for x in array[6:])}'

def create_phone_number_best_practice_variant(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)

def create_phone_number_best_practice_map_variant(n):
    n = ''.join(map(str,n))
    return '(%s) %s-%s'%(n[:3], n[3:6], n[6:])