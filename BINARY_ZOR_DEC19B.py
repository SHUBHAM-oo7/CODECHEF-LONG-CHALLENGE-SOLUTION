import itertools
import math
def extended_gcd(aa, bb):
    lastremainder, remainder = abs(aa), abs(bb)
    x, lastx, y, lasty = 0, 1, 1, 0
    while remainder:
        lastremainder, (quotient, remainder) = remainder, divmod(lastremainder, remainder)
        x, lastx = lastx - quotient*x, x
        y, lasty = lasty - quotient*y, y
    return lastremainder, lastx * (-1 if aa < 0 else 1), lasty * (-1 if bb < 0 else 1)
 
def modinv(a, m):
	g, x, y = extended_gcd(a, m)
	if g != 1:
		raise ValueError
	return x % m





for _ in range(int(input())):
    n=int(input())
    a=input()
    b=input()
    a=list(a)
    b=list(b)
    a1=a.count('1')
    a0=a.count('0')
    b1=b.count('1')
    b0=b.count('0')
    min1=n-(min(a1,b1)+min(a0,b0))
    max1=min(a1,b0)+min(a0,b1)
    nfac=math.factorial(n)
    c=0
    list1=[]
    #print(min1,max1)
    for j in range(min1,max1+1,2):
        list1.append(min(j,n-j))
    list1.sort()
    a1=list1[0]
    x1=(math.factorial(n)//((math.factorial(a1))*(math.factorial(n-a1))))
    ans=x1%1000000007
    for i in range(1,len(list1)):
        if(list1[i]-list1[i-1])==1:
            x1=(((x1*((n-list1[i]+1)%1000000007))%1000000007)*(modinv(list1[i],1000000007)))%1000000007
        elif(list1[i]-list1[i-1]==2):
            x1=(((x1*((n-list1[i]+2)%1000000007))%1000000007)*(modinv(list1[i]-1,1000000007)))%1000000007
            x1=(((x1*((n-list1[i]+1)%1000000007))%1000000007)*(modinv(list1[i],1000000007)))%1000000007
        ans+=x1
        ans%=1000000007
    #a1=list(itertools.permutations(a))
    #print("old a1",a1)
    #a1=list(set(a1))
    #print("new a1",a1)
    #b1=list(itertools.permutations(b))
    #print("old b1",b1)
    #b1=list(set(b1))
    #print("new b1",b1)
    #c=c%1000000007
    print(ans)
