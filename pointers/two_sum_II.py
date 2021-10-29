"""
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= first < second <= numbers.length.

Return the indices of the two numbers, index1 and index2, as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.
"""

def twoSum(nums, target):
    # Create 2 pointers at each end of the array
    l = 0
    r = len(nums) - 1

    # Loop through the array until curSum is no longer < or > target
    while l < r:
        curSum = nums[l] + nums[r]

        if curSum > target:
            r -= 1

        elif curSum < target:
            l += 1

        # return both l and r pointers indices
        else:
            return [l + 1, r + 1]



arr1 = [2, 7, 11, ]
tar1 = 9
print(twoSum(arr1, tar1))

arr2 = [1, 3, 4, 5, 7, 11]
tar2 = 9
print(twoSum(arr2, tar2))