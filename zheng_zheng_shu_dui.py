# coding: utf-8
"""
链接：https://www.nowcoder.com/questionTerminal/bac5a2372e204b2ab04cc437db76dc4f
来源：牛客网

牛牛以前在老师那里得到了一个正整数数对(x, y), 牛牛忘记他们具体是多少了。

但是牛牛记得老师告诉过他x和y均不大于n, 并且x除以y的余数大于等于k。
牛牛希望你能帮他计算一共有多少个可能的数对。
"""

n, k = list(map(int, input().split()))

count = 0
for y in range(k+1, n+1):
    if k:
        c = n//y*(y-k)
        if n%y>=k:
            c+=n%y-k+1
    else:
        c = n
    
    count += c

    # for remainder in range(k, y):
    #     for quotient in range(0,int(n//y)+1):
    #         x = y*quotient+remainder
    #         if x > n:
    #             break
    #         else:
    #             count += 1

print(count)

# n/y*(y-k)
# n%y-k+1