"""
    Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.You must write an algorithm with O(log n) runtime complexity
"""

"""
    Fixed the code. Runs and is accepted by Leetcode.
"""

def searchInsert(nums, target):
    l = 0
    r = len(nums) - 1
        
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            r = mid - 1
        else:
            l = mid + 1
    
    return l