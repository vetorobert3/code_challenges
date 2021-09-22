def search(nums, target):
    # We will create variables to start at each end of the array 
    l = 0
    r = len(nums) - 1

    # Create a while loop that will find the middle index of th array
    while l <= r:
        mid = l + (r - 1) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1

    return -1


arr1 = [-1,0,3,5,9,12]
arr2 = [1,5,6,22,78,99]

print(search(arr1, 9))
print(search(arr2, 7))