"""
In this challenge, we will check to see if two strings are permutations of each other. That is, if the strings contain the same characters but just in different order.

Understand:
    Input: ("abcd", "bdca")
    Output: True

    Input: ("abcd", "1234")
    Output: False

Plan:
    First, I would create a dictionary to house all the characters from the first string. Than I would iterate through the second string. If the characters from the second string match, then I would add one to the total number from first iteratation of th first string. If the number of...
"""
from collections import Counter

def check_perms(s1, s2):
    if len(s1) != len(s2):
        return False

    counter = Counter()

    for i in s1:
        counter[i] += 1
    for i in s2:
        if counter[i] == 0:
            return False
        counter[i] -= 1

    return True


string_1 = "asdf"
string_2 = "asef"

print(check_perms(string_1, string_2))
