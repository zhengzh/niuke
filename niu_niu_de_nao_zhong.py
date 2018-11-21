n = int(input())

def to_minute(h, m):
    return h*60+m

alarm = [list(map(int, input().split())) for i in range(n)]

t = int(input())
t_class = list(map(int, input().split()))

res = [0, 0]
for i in alarm:
    if to_minute(*i)+t <= to_minute(*t_class) and to_minute(*i) > to_minute(*res):
        res = i
        
print(*res)

