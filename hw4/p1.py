if __name__=="__main__":
    getLine=input()
    getLineInput=[int(i) for i in getLine.split()]
    #cities, roads
    C=getLineInput[0]
    R=getLineInput[1]
    roads=[0]*C
    for i in range(C):
        roads[i]=[0]*C
    for i in range(R):
        getLine=input()
        getLineInput=[int(i) for i in getLine.split()]
        roads[getLineInput[0]-1][getLineInput[1]-1]=1
        roads[getLineInput[1]-1][getLineInput[0]-1]=1
    size=[]
    seq=[]
    count=0
    for i in range(C):
        size.append(sum(roads[i]))
    while not R==0:
        count+=1
        edge=max(size)
        R-=edge
        node=size.index(edge)
        seq.append(node+1)
        size[node]=0
        for i in range(C):
            if roads[node][i]==1:
                roads[node][i]=0
                roads[i][node]=0
                size[i]-=1
    print(count)
    print(seq)
