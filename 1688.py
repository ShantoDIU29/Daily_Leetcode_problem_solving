# from collections import Counter
# arr = ["a","b","a"]
# k=3
# count=Counter(arr)
# D_count=0
# for i in arr:
#     if count[i]==1:
#       D_count+=1
#       if D_count==k:
#          print(i)
#          break
# else:
#     print("")
sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
max_word=0
for i in sentences:
  words=i.split(" ")
  count=len(words)
  max_word=max(max_word,count)
print(max_word)