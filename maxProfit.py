"""
Understand:
    Input: prices = [7,1,5,3,6,4]
    Output: 5
    Explanation: Buy on day 2(prices = 1) and sell on day 5 (prices = 6), 
        profit = 6 - 1 = 5.

Plan:
    Brute force solution will require a nested for loop were each ith item in the array will iterate through each other item in the array for a O(n^2) (quadratic) time. For O(n) (linear) you can use the pointer method that uses 2 pointers. One L and one R. The L pointer will find the buying stock on the lowest day and R will find the selling day at its highest value in the future. we subtract the values of R to L to find the biggest profit. The max profit will be kept track by a variable and replacing it with the new max profit as we iterate through the array. 
"""

def maxProfit(prices):
    l = 0 # Left pointer will start 0 index
    r = 1 # Right pointer will start at 1 index and will always be right of the left pointer
    maxP = 0 # This will be the maximum profit. Will change if r - l gets bigger

    # Create a while loop to iterate through the whole array
    while r < len(prices):
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            maxP = max(maxP, profit)

        else:
            l = r

        r += 1

    return maxP

pro = [7,1,5,3,6,4]
pro_2 = [7,6,4,3,1]

print(maxProfit(pro))
print(maxProfit(pro_2))
