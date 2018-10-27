input()
s = input()
c = 0
d = "NESW"
for i in s:
    c += -1 if i=='L' else 1
print(d[c%4])