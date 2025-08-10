grid = [[3,2],[1,0]]
count=0
for row in grid:
  for val in row:
    if val<0:
      count+=1
print(count)