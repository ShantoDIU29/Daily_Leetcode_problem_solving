nums = [1,1,2]
dup=[]
s=set()
for i in nums:
   if i in s and i not in dup:
     dup.append(i)
   else:
     s.add(i) 
return(dup)      