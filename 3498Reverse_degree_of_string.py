# 3498. Reverse Degree of a String
# Given a string s, calculate its reverse degree.

# The reverse degree is calculated as follows:

# For each character, multiply its position in the reversed alphabet ('a' = 26, 'b' = 25, ..., 'z' = 1) with its position in the string (1-indexed).
# Sum these products for all characters in the string.
# Return the reverse degree of s.
# Example 1:
# Input: s = "abc"
Output: 148

s = "abc"
total=0
for i in range(len(s)):
    char=s[i]
    r_value=26-(ord(char)-ord('a'))
    pos=i+1
    total+=r_value*pos
print(total)      