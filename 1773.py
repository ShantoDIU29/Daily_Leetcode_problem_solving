items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]]
ruleKey = "color"
ruleValue = "silver"
count=0
key_map={"type":0,"color":1,"name":2}
index=key_map[ruleKey]
for i in items:
   if i[index]==ruleValue:
     count+=1
print(count)