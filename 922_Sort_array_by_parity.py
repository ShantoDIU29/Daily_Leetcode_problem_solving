# Given an array of integers nums, half of the integers in nums are odd, and the other half are even.
# Sort the array so that whenever nums[i] is odd, i is odd, and whenever nums[i] is even, i is even.
# Return any answer array that satisfies this condition.
# Example 1:
# Input: nums = [4,2,5,7]
# Output: [4,5,2,7]
# Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.

nums = [4,2,5,7]
lst1=[]
lst2=[]
for i in range(len(nums)):
  if i%2==0 and nums[i]%2==0:
    lst1.append(nums[i])
  else:
    i%2!=0 and nums[i]%2!=0
    lst2.append(nums[i])
      
 
print(lst1+lst2)   