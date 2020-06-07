#code by shubham kumar singh
for _ in range(int(input())):
    num=int(input())
    lst=list(map(int,input().split()))
    count=1
    lst1=[]
    for i in range(1,num):
        if(i<5):
            lst1=lst[0:i]
        else:
            lst1=lst[i-5:i]
        if(lst[i]<(min(lst1))):
            count+=1
    print(count)
            
    
