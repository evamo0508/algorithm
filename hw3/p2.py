
GRAY, BLACK = 0, 1

def topological(graph):
    order, enter, state ,d= [], set(graph), {}, 0

    def dfs(node):
        state[node] = GRAY
        for k in graph.get(node, ()):
            sk = state.get(k, None)
            if sk == GRAY: raise ValueError("cycle")
            if sk == BLACK: continue
            enter.discard(k)
            dfs(k)
        order.append(node)
        state[node] = BLACK

    while enter: dfs(enter.pop())
    return order

def knapsack(c, w, max_weight):
    rows = len(w) + 1
    cols = max_weight + 1

    # adding dummy values as later on we consider these values as indexed from 1 for convinence
    v = [0] + w[:]
    w = [0] + w[:]

    # row : values , #col : weights
    dp_array = [[0 for i in range(cols)] for j in range(rows)]

    # 0th row and 0th column have value 0

    # values
    for i in range(1, rows):
        # weights
        for j in range(1, cols):
            # if this weight exceeds max_weight at that point
            if j - w[i] < 0:
                dp_array[i][j] = dp_array[i - 1][j]

            # max of -> last ele taken | this ele taken + max of previous values possible
            else:
                dp_array[i][j] = max(dp_array[i - 1][j], v[i] + dp_array[i - 1][j - w[i]])

    # return dp_array[rows][cols]  : will have the max value possible for given wieghts

    courseChosen = []
    i = rows - 1
    j = cols - 1

    # Get the items to be picked
    while i > 0 and j > 0:

        # ith element is added
        if dp_array[i][j] != dp_array[i - 1][j]:
            # add the value
            courseChosen.append(c[i-1])
            # decrease the weight possible (j)
            j = j - w[i]
            # go to previous row
            i = i - 1

        else:
            i = i - 1

    return courseChosen

if __name__=="__main__":
	getLine=input()
	getLineInt=[int(i) for i in getLine.split()]
	#n:number of courses;p:number of prerequisite pairs
	n=getLineInt[0]
	p=getLineInt[1]
	m=getLineInt[2]
    #semester[ID]=which semester is available--->vertex
	semester,magicPower=[0]*n,[0]*n
	for i in range(n):
		getLine=input()
		getLineInt=[int(j) for j in getLine.split()]
		semester[i]=getLineInt[1]
		magicPower[i]=getLineInt[2]
    #canStudy[preCourse]=[cousre1,cousre2,...]--->adj list
	canStudy={i:[] for i in range(n)}
	needToStudy={i:[] for i in range(n)}
	for i in range(p):
		getLine=input()
		getLineInt=[int(j) for j in getLine.split()]
		canStudy[getLineInt[1]].append(getLineInt[0])
		needToStudy[getLineInt[0]].append(getLineInt[1])
	needToStudyNo=[len(needToStudy[i]) for i in range(n)]
	try: order=topological(canStudy)
	except ValueError: 
		print(-1)
		exit()
	if len(order)==0:
		print(-1)
		exit()
	semesterNo=0
	coursePlan,canStudyNow,canStudyNow_new={},set(),set()
	#course with no requisite
	for i in range(n):
		if needToStudyNo[i]==0:
			canStudyNow.add(i)
	while order:
		semesterNo+=1
		coursePlan[semesterNo],courseLeft=[],[]
		while True:
			if len(order)==0: 
				KPweight=[]
				for i in coursePlan[semesterNo]:
					KPweight.append(magicPower[i])
				courseChosen=knapsack(coursePlan[semesterNo],KPweight,m)
				remain=set(coursePlan[semesterNo])-set(courseChosen)
				Remain=list(remain)
				courseLeft+=Remain
				for i in Remain:
					coursePlan[semesterNo].remove(i)
					canStudyNow.add(i)
					for j in canStudy[i]:
						if needToStudyNo[j]==0:
							canStudyNow_new.remove(j)
						needToStudyNo[j]+=1
				break
			course=order.pop()
			if course not in canStudyNow:
				courseLeft.append(course)
				continue
			if (semesterNo%2==1 and semester[course]!=1) or (semesterNo%2==0 and semester[course]!=0):
				coursePlan[semesterNo].append(course)
				canStudyNow.remove(course)
				for i in canStudy[course]:
					needToStudyNo[i]-=1
					if needToStudyNo[i]==0:
						canStudyNow_new.add(i)
			else:
				courseLeft.append(course)
		courseLeft.reverse()
		order+=courseLeft
		canStudyNow.update(canStudyNow_new)
		canStudyNow_new=set()
	print(semesterNo*0.5)
	for i in range(semesterNo):
		if len(coursePlan[i+1])==0:
			print(-1)
		else:
			print(*coursePlan[i+1],sep=' ')