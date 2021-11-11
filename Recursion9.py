def fun(n):
    if n<=0:
        return
    fun(n-1)
    print("*")
    fun(n-2)
    
fun(5)
