def str2(a,b):
    char1=a[:2]
    char2=b[:2]
    a=char2+a[2:]
    b=char1+b[2:]
    z=a+" "+b
    return z
print(str2("swastik","kalyane"))