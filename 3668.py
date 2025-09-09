order = [1,4,5,3,2]
friends = [2,5]
lst=[]
for i in order:
  for j in friends:
    if i==j:
     lst.append(i)
print(lst)     