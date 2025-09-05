date = "2080-02-29"
p=date.split("-")
x = bin(int(p[0]))[2:]  
y = bin(int(p[1]))[2:]
z = bin(int(p[2]))[2:]
print(f"{x}-{y}-{z}")
