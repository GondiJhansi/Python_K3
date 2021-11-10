def fun(n):
    if n<=0:
        return 1
    return fun(n-2)+fun(n-1)

print(fun(5))
