names = ["Mary","John","Emma"]
heights = [180,165,170]
c=list(zip(heights,names))
c.sort(reverse=True)
sorted_names=[]
for height,name in c:
  sorted_names.append(name)
print(sorted_names)