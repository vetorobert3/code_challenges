"""
    Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.You must write an algorithm with O(log n) runtime complexity
"""

"""
    Having a problem with this input...
    Input: [1,3,5,6], target = 2
    Output: 1

    Not getting the correct output. Getting 0...
"""

def searchInsert(nums, target):
    l = 0
    r = len(nums) - 1
        
    while l <= r:
        mid = l + r // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            r = mid - 1
        else:
            l = mid + 1
                
        if nums[mid] > target:
            return mid - 1
        elif nums[mid] < target:
            return mid + 1