import sys
########################################
# You can add supporting functions here





########################################
def match(men, women, mprefer, wprefer):
    ### TODO ###
    # Implement the Gale-Shapley algorithm.
    # You should return a dictionary of pairing result, use woman as key and man as
    # value.

    wives = {}
    n=len(men[0])
    p_lastw=[-1]*n
    while len(wives)!=n:
        for i in range(0,n): 
            for j in range(p_lastw[i]+1,n):
                r=mprefer[i][j]
                if r not in wives:
                    wives[r]=i
                else:
                    if women[r][wives[r]]>women[r][i]:
                        p_lastw[wives[r]]=r
                        wives[r]=i
    return wives


def is_stable(men, women, mprefer, wives):
    if wives is None:
        wives = wives
    for w, m in wives.items():
        i = men[m][w]
        preferred = mprefer[m][:i]
        for p in preferred:
            h = wives[p]
            if women[p][m] < women[p][h]:  
                return False
    return True

if __name__ == '__main__':
    '''
    A reminder of the definitions of variables

    men is a 2D-list which presents men's rankings for women. 
    men[m][w]=i means man 'm' ranks woman 'w' as i.
    Note that every list is zero-based and 0 means the highest preference.
    For example, if there are 10 pairs of men and women, 
    they are denoted as m0, m1, ..., m9 and w0, w1, ..., w9
    men[1][2] = 0 means m1 likes w2 the most among all women.
    Similarly, women[1][2] = 1 means, for w1, m2 is her second choice.
    
    mprefer is a 2D-list which presents men's preference.  
    mprefer[m][i]=w means, for man 'm', his i-th preferable woman is 'w'
    For examples, mprefer[1][0]=2 means m1's first choice is w2.
    '''
    case = str(sys.argv[1])
    men = []
    men_file = 'men_' + case + '.txt'
    women_file = 'women_' + case + '.txt'
    for line in open(men_file, 'r'):
        man = list(map(int, line.split()))
        men.append(man)

    women = []
    for line in open(women_file, 'r'):
        woman = list(map(int, line.split()))
        women.append(woman)

    wives = {}
    pairs = []
    
    mprefer = []
    wprefer = []
    pair_num = len(men[0])
    
    for i in range(pair_num):
        mp = []
        wp = []
        for j in range(pair_num):
            mp.append(men[i][:].index(j))
            wp.append(women[i][:].index(j))
        mprefer.append(mp)
        wprefer.append(wp)
    
    wives = match(men, women, mprefer, wprefer)
    if is_stable(men, women, mprefer, wives):
        print('The matching is stable.')
    else:
        print('The matching is failed.')







