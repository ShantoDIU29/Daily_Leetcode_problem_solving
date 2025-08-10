# You are given an integer array nums. Transform nums by performing the following operations in the exact order specified:

# Replace each even number with 0.
# Replace each odd numbers with 1.
# Sort the modified array in non-decreasing order.
# Return the resulting array after performing these operations.

 

# Example 1:

# Input: nums = [4,3,2,1]

# Output: [0,0,1,1]
class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
                for idx in range(len(nums)):  
                      if nums[idx] % 2 == 0:      
                             nums[idx] = 0
                      else:
                         nums[idx] = 1
                nums.sort()
                return nums