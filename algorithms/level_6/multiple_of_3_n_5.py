# https://www.codewars.com/kata/514b92a657cdc65150000006/train/python

# Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.
# Additionally, if the number is negative, return 0 (for languages that do have them).


def sum_of_multipliers(number):

    sum = 0

    if number < 3:
        return sum

    for i in range(1, number):
        if i % 3 == 0 or i % 5 == 0:
            sum += i

    return sum

def sum_of_multipliers_best_practice(number):
    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)