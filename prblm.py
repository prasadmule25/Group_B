def fun(s):
    if len(s)>=2:
        a=s[:2]+s[-2:]
        print(a)
    else:
        print("empty")
fun('hello')