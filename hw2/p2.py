def transposeMatrix(m):
    t = []
    for c in range(len(m[0])):
        tRow = []
        for r in range(len(m)):
            tRow.append(m[r][c])
        t.append(tRow)
    return t

def getMatrixMinor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

def getMatrixDeternminant(m):
    #base case for 2x2 matrix
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]

    determinant = 0
    for c in range(len(m)):
        determinant += ((-1)**c)*m[0][c]*getMatrixDeternminant(getMatrixMinor(m,0,c))
    return determinant

def getMatrixInverse(m):
    determinant = getMatrixDeternminant(m)
    #special case for 2x2 matrix:
    if len(m) == 2:
        return [[m[1][1]/determinant, -1*m[0][1]/determinant],
                [-1*m[1][0]/determinant, m[0][0]/determinant]]

    #find matrix of cofactors
    cofactors = []
    for r in range(len(m)):
        cofactorRow = []
        for c in range(len(m)):
            minor = getMatrixMinor(m,r,c)
            cofactorRow.append(((-1)**(r+c)) * getMatrixDeternminant(minor))
        cofactors.append(cofactorRow)
    cofactors = transposeMatrix(cofactors)
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c]/determinant
    return cofactors

def getMatrixMultiply(X,Y):
	results=[[0 for y in range(len(Y[0]))] for x in range(len(X))]
	for i in range(len(X)):
		for j in range(len(Y[0])):
			for k in range(len(X[0])):
				results[i][j] += X[i][k] * Y[k][j]
	return results

def error(i,j,m,yValues):
	n=j-i+1 #contain n points
	if n<=m+1:
		return 0
	M=[]
	for x in range(i+1,j+2):
		M.append([])
		for y in range(m+1):
			M[x-i-1].append(x**y)
	Mt=transposeMatrix(M)
	Y=[[yValues[x]] for x in range(i,j+1)]
	A=getMatrixMultiply(getMatrixInverse(getMatrixMultiply(Mt,M)),getMatrixMultiply(Mt,Y))
	errors=[0 for x in range(n)]
	for x in range(i,j+1):
		for y in range(m+1):
			errors[x-i]+=A[y][0]*((x+1)**y)
		errors[x-i]=(errors[x-i]-yValues[x])**2
	return sum(errors)

def constructTable(n,m,C,yValues):
	cost=[[0 for y in range(n)] for x in range(n)]
	for i in range(n):
		cost[i][i]=0
	for l in range(1,n):
		for i in range(n-l):
			j=i+l
			cost[i][j]=error(i,j,m,yValues)
			for k in range(i+1,j):
				q=cost[i][k]+cost[k+1][j]+C
				if q<cost[i][j]:
					cost[i][j]=q
	return cost
	    
if __name__=="__main__":
	firstLine=input()
	firstList=firstLine.split()
	n=int(firstList[0])
	m=int(firstList[1])
	C=int(firstList[2])
	secondLine=input()
	yValues=[float(i) for i in secondLine.split()]
	cost=constructTable(n,m,C,yValues)
	print(round(cost[0][n-1]))
