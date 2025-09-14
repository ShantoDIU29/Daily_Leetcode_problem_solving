nums = [8,1,2,2,3]
ans=[]
for i in range(len(nums)):
  count=0
  for j in range(len(nums)):
    if j!=i and nums[j]<nums[i]:
      count+=1
  ans.append(count)
print(ans)