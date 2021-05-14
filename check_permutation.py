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