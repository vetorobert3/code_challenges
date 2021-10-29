"""
    In this challenge, we will check to see if two strings are permutations of each other. That is, if the strings contain the same characters but just in different order.

    Understand:
        Input: ("qwer", "rewq)
        Output: True
        
        Input: ("qwer", "12ab")
        Output: False
        
    Plan:
        We will create a counter. The counter will keep track of how many time a character occurs in the first iteration of the first string. We will than iterate through the second string and subtract those characters from the ones already in the counter. If values are 0 then we have a permutation. If values are > or < 0 then we don't have a permutation.
"""
from collections import Counter

def check_perms(s1, s2):
    # If the lengths are not the same for both strings, then there can be no perm
    if len(s1) != len(s2):
        return False
        
    # Init counter
    counter = Counter()
    
    # Add values to the counter by iterating through s1
    for char in s1:
        counter[char] += 1
        
    # Iterating through s2
    for char in s2:
        # If counter[i] is zero, then it wasn't in s1
        if counter[char] == 0:
            # No permutatuion
            return False
        # Else, subtract the value already in the counter
        counter[char] -= 1
    
    # This will make it a True statement    
    return True
    
string_1 = "asddf"
string_2 = "asddf"
print(check_perms(string_1, string_2))

string_3 = "asddf"
string_4 = "asedf"
print(check_perms(string_3, string_4))

string_5 = "asddff"
string_6 = "asedf"
print(check_perms(string_5, string_6))

string_7 = "&*%45"
string_8 = "&*%45"
print(check_perms(string_7, string_8))