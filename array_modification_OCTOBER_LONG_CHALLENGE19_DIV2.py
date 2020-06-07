#code by shubham kumar singh
for _ in range(int(input())):
    num,rep=map(int,input().split())
    lst=list(map(int,input().split()))
    remain=rep%num
    for __ in range((rep//num)%3):
        for i in range(num):
            lst[i]^=lst[num-1-i]
    for i in range(remain):
        lst[i]^=lst[num-1-i]
    if(num%2!=0 and rep>num//2):
        lst[num//2]=0
    print(*lst)
        
