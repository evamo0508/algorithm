
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

if __name__=="__main__":
	getLine=input()
	getLineInt=[int(i) for i in getLine.split()]
	#n:number of courses;p:number of prerequisite pairs
	n=getLineInt[0]
	p=getLineInt[1]
    #semester[ID]=which semester is available--->vertex
	semester=[0]*n
	for i in range(n):
		getLine=input()
		getLineInt=[int(j) for j in getLine.split()]
		semester[i]=getLineInt[1]
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
			if len(order)==0: break
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