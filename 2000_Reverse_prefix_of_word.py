word = "abcdefd"
ch = "d"

for letter in word:
    print(reversed(letter), end='')  
    if letter == ch:
        break