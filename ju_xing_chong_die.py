# coding: utf-8

"""
链接：https://www.nowcoder.com/questionTerminal/a22dd98b3d224f2bb89142f8acc2fe57
来源：牛客网

平面内有n个矩形, 第i个矩形的左下角坐标为(x1[i], y1[i]), 右上角坐标为(x2[i], y2[i])。

如果两个或者多个矩形有公共区域则认为它们是相互重叠的(不考虑边界和角落)。

请你计算出平面内重叠矩形数量最多的地方,有多少个矩形相互重叠。
"""
n = int(input())
x1 = list(map(int, input().split()))
y1 = list(map(int, input().split()))
x2 = list(map(int, input().split()))
y2 = list(map(int, input().split()))

res = 1
for x in x1+x2:
    for y in y1+y2:
        c = 0
        for i in range(n):
            # 竟然对所有的边界或顶点相交的情况都成立，证明需要枚举一个或
            # 两个点相交但矩形不重叠的情况
            if x>x1[i] and y>y1[i] and x<=x2[i] and y<=y2[i]:
                c+=1
        res = max(res,c)
print(res)


