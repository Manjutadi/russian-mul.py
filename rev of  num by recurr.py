#rev of num using recursion
#re=0
def rev(re,num):
    #global re
    if num==0:
        return re
    re=re*10+num%10
    return rev(re,num//10)

num=int(input())
print(rev(0,num))
