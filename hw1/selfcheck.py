import match
import sys

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

for case in range(1,4):
    men = []
    men_file = 'men_' + str(case) + '.txt'
    women_file = 'women_' + str(case) + '.txt'
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

    wives = match.match(men, women, mprefer, wprefer)

    if is_stable(men, women, mprefer, wives):
        print('Pass test case %d.' %case)
    else:
        print('Test case %d fail.' %case)

