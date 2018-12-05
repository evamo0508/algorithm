def greedy(product):
	if product==1 or product==2 or product==3 or product==5 or product==7:
		return 10+product
	digits=[]
	while product!=1:
		for i in range(9,1,-1):
			if product%i==0:
				product/=i
				digits.append(i)
	number=0
	for i in range(len(digits)):
		number+=digits[i]*(10**i)
	return number

if __name__=="__main__":
	caseNo=int(input())
	products=[]
	for i in range(caseNo):
		products.append(int(input()))
	for i in range(caseNo):
		print(greedy(products[i]))
