nums = [5,4,2,3]
a=[]

while nums:
    alice=min(nums)
    nums.remove(alice)
    bob=min(nums)
    nums.remove(bob)
    
    a.append(bob)
    a.append(alice)
print(a)    
    
  
  