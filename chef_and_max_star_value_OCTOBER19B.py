for _ in range(int(input())):
    num=int(input())
    lst=list(map(int,input().split()))
    lst.reverse()
    maxstar=0
    for i in range(1,4000):
        star=0
        if(i in lst):
            k=lst.index(i)
            for j in range(k+1,num):
                if(lst[j]%i==0):
                    star+=1
            maxstar=max(star,maxstar)
    print(maxstar)
