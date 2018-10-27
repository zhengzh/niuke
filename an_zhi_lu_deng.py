n = int(input())

def get_num(l, s):
    count = 0
    i=0
    while i < l:
        if s[i]=='.':
            count+=1
            i+=3
        elif s[i]=='X':
            i+=1
    return count


for i in range(n):
    l = int(input())
    s = input()
    print(get_num(l,s))
