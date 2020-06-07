for _ in range(int(input())):
    vertex,edge=map(int,input().split())
    vertexlist=[0]*vertex
    for __ in range(edge):
        l,r=map(int,input().split())
        vertexlist[l-1]+=1
        vertexlist[r-1]+=1
        store1=l-1
        store2=r-1
    e=0
    o=0
    store3=0
    count=-1
    for i in vertexlist:
        count+=1
        if(i%2==0):
            e+=1
        else:
            store3=count
            o+=1
    if(edge%2==0):
        print(1)
        print("1 "*vertex,end=" ")
    else:
        if(o>0):
            print(2)
            for j in range(vertex):
                if(j==store3 or vertexlist[j]==0):
                    print("1",end=" ")
                else:
                    print("2",end=" ")
        else:
            print(3)
            for j in range(vertex):
                if(j==store1):
                    print("1",end=" ")
                elif(j==store2):
                    print("2",end=" ")
                else:
                    print("3",end=" ")
    print()
