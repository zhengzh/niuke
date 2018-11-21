n, w = list(map(int, input().split()))
v = list(map(int, input().split()))

from functools import lru_cache

@lru_cache(maxsize=32)
def dfs(i, w):
    if w<0: return 0
    if i==1:
        if v[0]<=w:
            return 2
        return 1
    return dfs(i-1, w) + dfs(i-1, w-v[i-1])

print(dfs(n,w))