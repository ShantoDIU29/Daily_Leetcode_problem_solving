# You are given a positive integer array nums.
# The element sum is the sum of all the elements in nums.
# The digit sum is the sum of all the digits (not necessarily distinct) that appear in nums.
# Return the absolute difference between the element sum and digit sum of nums.

# Note that the absolute difference between two integers x and y is defined as |x - y|.
# Example 1:

# Input: nums = [1,15,6,3]
# Output: 9
# Explanation: 
# The element sum of nums is 1 + 15 + 6 + 3 = 25.
# The digit sum of nums is 1 + 1 + 5 + 6 + 3 = 16.
# The absolute difference between the element sum and digit sum is |25 - 16| = 9.
class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        sum1=0
        sum2=0
        for i in nums:
            sum1+=i
        for j in nums:
            for digit in str(j):
                sum2+=int(digit)
        return(abs(sum1-sum2))