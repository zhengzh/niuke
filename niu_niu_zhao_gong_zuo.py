n,m=list(map(int, input().split()))
i,dp=0,[]
while i<n:
    v = list(map(int, input().split()))
    if len(v)==2:
        dp.append(v)
        i+=1
ai=[]
while len(ai) != m:
    ai = list(map(int, input().split()))
from collections import defaultdict
dp = defaultdict(int, dp)
 
ma=0
d=sorted(list(dp.keys())+ai)
for i in d:
    ma = max(dp[i], ma)
    dp[i]=ma
for i in ai:
    print(dp[i])