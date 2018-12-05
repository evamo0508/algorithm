import time
import sys

########################################
# You can add supporting functions here
def merge(a,b,c):
    x=[]
    while len(a)!=0 and len(b)!=0 and len(c)!=0:
        if a[0]<=b[0] and a[0]<=c[0]:
            x.append(a[0])
            a.remove(a[0])
        elif b[0]<=a[0] and b[0]<=c[0]:
            x.append(b[0])
            b.remove(b[0])
        else:
            x.append(c[0])
            c.remove(c[0])
    while len(a)!=0 and len(b)!=0 and len(c)==0:
        if a[0]<b[0]:
            x.append(a[0])
            a.remove(a[0])
        else:
            x.append(b[0])
            b.remove(b[0])
    while len(a)!=0 and len(b)==0 and len(c)!=0:
        if a[0]<c[0]:
            x.append(a[0])
            a.remove(a[0])
        else:
            x.append(c[0])
            c.remove(c[0])
    while len(a)==0 and len(b)!=0 and len(c)!=0:
        if b[0]<c[0]:
            x.append(b[0])
            b.remove(b[0])
        else:
            x.append(c[0])
            c.remove(c[0])
    if len(a)!=0:
        x+=a
    elif len(b)!=0:
        x+=b
    else:
        x+=c
    return x
########################################

def mergesort(x, count):
    ### TODO ###
    # Implement the merge sort algorithm.
    # x is a list with N elements.
    # You must return a sorted list and a counter of splitting number. 
    if len(x)==0 or len(x)==1:
        return x,count
    else:
        #middle is the number of item in the second list
        middle=int(len(x)/3)
        count+=1
        if len(x)%3==1:
            a,count=mergesort(x[:middle+1],count)
            b,count=mergesort(x[middle+1:middle*2+1],count)
            c,count=mergesort(x[middle*2+1:],count)
        elif len(x)%3==2:
            a,count=mergesort(x[:middle+1],count)
            b,count=mergesort(x[middle+1:middle*2+2],count)
            c,count=mergesort(x[middle*2+2:],count)
        else:
            a,count=mergesort(x[:middle],count)
            b,count=mergesort(x[middle:middle*2],count)
            c,count=mergesort(x[middle*2:],count)
        x=merge(a,b,c)
    return x, count

if __name__ == '__main__':
    case = sys.argv[1]
    test_name = 'test_'+str(case)+'.txt'
    out_name = 'out_'+str(case)+'.txt'
    file_in = open(test_name, 'r')
    file_out = open(out_name, 'w')
    start_time = time.time()
    l = file_in.readline().split()
    l = list(map(int, l))
    count = 0 
    result, count = mergesort(l, count)
    for i in result:
        file_out.write(str(i)+' ')
    file_out.write('\n')
    file_out.write(str(count))
    print('Timer: ', time.time()-start_time)
