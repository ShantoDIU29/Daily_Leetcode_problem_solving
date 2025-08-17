# You are given an integer array nums.

# You replace each element in nums with the sum of its digits.

# Return the minimum element in nums after all replacements.
# Example 1:

# Input: nums = [10,12,13,14]

# Output: 1

# Explanation:

# nums becomes [1, 3, 4, 5] after all replacements, with minimum element 1.

class Solution:
    def minElement(self, nums: List[int]) -> int:
        digit_sums = []
        for num in nums:
            s = sum(int(d) for d in str(num))
            digit_sums.append(s)
        min_sum = min(digit_sums)
        return min_sum
