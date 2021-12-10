def formula(a,b=None,c=None):
    if b==None:
        return a*a
    if c!=None:
        return a*a+b*b+c*c+2*(a*b+b*c+c*a)
    return a*a+b*b+2*a*b
print(formula(6))
