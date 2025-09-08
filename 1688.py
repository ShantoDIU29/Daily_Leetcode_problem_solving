from collections import Counter
arr = ["a","b","a"]
k=3
count=Counter(arr)
D_count=0
for i in arr:
    if count[i]==1:
      D_count+=1
      if D_count==k:
         print(i)
         break
else:
    print("")