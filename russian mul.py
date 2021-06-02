#russian multiplication
def mul(a,b):
    c=0    
    while a:
        if a%2!=0:
            c+=b
        a=a//2
        b=b*2
    print(c)
    
