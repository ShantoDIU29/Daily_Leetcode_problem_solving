num =121
count=0
for i in str(num):
  digit=int(i)
  if digit!=0:
       if num%digit==0:
        count+=1
print(count)      