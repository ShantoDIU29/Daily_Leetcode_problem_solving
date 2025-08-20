s = "successes"
vowels="aeiou"

max_c=0
max_b=0
for v in vowels:
  c=s.count(v)
  if c>max_c:
    max_c=c
for x in s:
   y=s.count(x)
   if y>max_b:
     max_b=y
    
print(max_c+max_b)    
    