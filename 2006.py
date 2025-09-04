nums = [1,3]
k=3
count=0
for i in range(len(nums)):
    for j in range(len(nums)):
        if i<j and abs(nums[i] -nums[j])==k:
           count+=1
print(count) 