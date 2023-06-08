"""
Write a function that will check whether ANY permutation of the characters of the input string is a palindrome.
Bonus points for a solution that is efficient and/or that uses only built-in language functions.
Deem yourself brilliant if you can come up with a version that does not use any function whatsoever.

Example
madam -> True
adamm -> True
junk -> False

Hint
The brute force approach would be to generate all the permutations of the string and check each one of them
whether it is a palindrome. However, an optimized approach will not require this at all.
"""



def permute_palindrome(word):

    def create_perms(string):
        perms = create_perms(word[1:])
        result = set()
        for perm in perms:
            for i in range(len(perm) + 1):
                new_perm = perm[:i] + string[0] + perm[i:]
                result.add(new_perm)

        return sorted(list(result))

    mutations = create_perms(word)

    for word in mutations:
        if word == word[::-1]:
            return True
        else:
            return False
