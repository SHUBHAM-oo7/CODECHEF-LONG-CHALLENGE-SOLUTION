#code by shubham kumar singh
def val(c): 
    if c >= '0' and c <= '9': 
        return ord(c) - ord('0') 
    else: 
        return ord(c) - ord('A') + 10
        
        
        
def toDeci(str,base): 
    llen = len(str) 
    power = 1 
    num = 0   
    for i in range(llen - 1, -1, -1): 
        num += val(str[i]) * power 
        power = power * base 
    return num 


from functools import reduce
for _ in range(int(input())):
    lst=[]
    n=int(input())
    for i in range(n):
        str=input().split()
        if str[0]==('-1'):
            n=[]
            for j in range(2,37):
                try:
                    func=int(str[1],j)
                    n.append(func)
                except:
                    pass
            lst.append(n)
        else:
            func=int(str[1],int(str[0]))
            lst.append([func])
    period=reduce(set.intersection, [set(loop) for loop in lst])
    period=list(period)
    if((len(period)==0) or (min(period)>10**12)):
        print(-1)
    else:
        print(min(period))
