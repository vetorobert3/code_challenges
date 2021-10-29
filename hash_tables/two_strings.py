# Given 2 strings, determine if they share a common substring. A substring may be as small as 1 character.

def two_strings(string_1, string_2):
    set1 = set()

    for char in string_1:
        set1.add(char)

    for char in string_2:
        if char in set1:
            return "Yes"

    return "No"

s1 = "qwerty"
s2 = "qwerty"
print(two_strings(s1, s2))

s3 = "qwerty"
s4 = "poiuh"
print(two_strings(s3, s4))

s5 = "qwerty"
s6 = "ncbfhy"
print(two_strings(s3, s4))