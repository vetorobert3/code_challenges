# Implement an algorithm to determine if a string has all unique characters

"""
Understand:
    Input: "shenfy'
    Output: True

    Input: "hjfgg"
    Output: False

Plan:
    Iterate though the string and put each character in a hash table. As we iterate, we will count each time the character appears in the string. If none are greater than 1, return True, else, return False.
"""

def is_unique(string):
    chars = {}

    for i in string:
        if chars.get(i):
            chars[i] += 1
        else:
            chars[i] = 1

    for i in string:
        if chars[i] > 1:
            return False

    return True


# Book Code:
    # if len(string) > 128:
    #     return False

    # char_set = [False for _ in range(128)]

    # for char in string:
    #     val = ord(char)
    #     if char_set[val]:
    #         return False
    #     char_set[val] = True

    # return True

s =  ("hjpll")
print(is_unique(s))