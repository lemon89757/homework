a, b =0, 1
for i in range(99):
    a, b = b, a+b
print(a)    #计算出n=100时斐波那契数列的值，a(n)=a(n-1)+a(n-2)
