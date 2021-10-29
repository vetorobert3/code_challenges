"""
Understand
Input: nums = [1, 3, 4], target = 7
Output: [1, 2]

Input: nums = [1, 2, 4, 6], target = 8
Output: [1, 3]

Input: [0], target = 0
Output [0]

Plan
(Brute)
Loop through the list and add first element with the rest of the array 
to find 2 elements that add up to the target.

(Hash Table)
First we create a blank dict.
we loop through the array.
As we loop through, we take the target and subtract it from the current 
index. If that product is in the dict, we return the that index plus the 
current index we are on.
If not, we add that index to the dict.

Reflect


"""

def twoSum(nums, target):
    req = {}
        
    for i in range(len(nums)):
        if target - nums[i] in req:
            return [req[target - nums[i]], i]
        else:
            req[nums[i]] = i


twoSum_1n = [1, 3, 4] 
target_1 = 7
twoSum_2n = [1, 2, 4, 6]
target_2 = 8

print(twoSum(twoSum_1n, target_1))
print(twoSum(twoSum_2n, target_2))


        