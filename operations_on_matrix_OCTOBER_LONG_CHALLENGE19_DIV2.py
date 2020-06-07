#code by shubham kumar singh
for _ in range(int(input())):
    row,col,que=map(int,input().split())
    rowlist=[0]*row
    collist=[0]*col
    for __ in range(que):
        x,y=map(int,input().split())
        rowlist[x-1]+=1
        collist[y-1]+=1
    roweven=0
    rowodd=0
    coleven=0
    colodd=0
    for i in range(row):
        if(rowlist[i]%2==0):
            roweven+=1
        else:
            rowodd+=1
    for i in range(col):
        if(collist[i]%2==0):
            coleven+=1
        else:
            colodd+=1
    print(((roweven*colodd)+(rowodd*coleven)))
        
