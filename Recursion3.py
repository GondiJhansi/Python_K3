def fun(n):
    if n==0:
        return 0
    return 1+fun(n-1)

print(fun(5))
