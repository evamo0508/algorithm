Implement Gale-Shapley algorithm

In this problem, four variables are given in match.py, they are 'men', 'women', 'mprefer' and 'wprefer'

'men' is a 2D-list which presents men's rankings for women. 
men[m][w]=i means man 'm' ranks woman 'w' as i.
Note that every list is zero-based and 0 means the highest preference.
For example, if there are 10 pairs of men and women, 
they are denoted as m0, m1, ..., m9 and w0, w1, ..., w9
men[1][2]=0 means m1 likes w2 the most among all women.
Similarly, women[1][2] = 1 means, for w1, m2 is her second choice.

'mprefer' is a 2D-list which presents men's preference.  
mprefer[m][i]=w means, for man 'm', his i-th preferable woman is 'w'
For examples, mprefer[1][0]=2 means m1's first choice is w2.

The goal is to complete the function 'match' in match.py.
You should return a stable matching result as a dictionary.
The dictionary takes women as keys and men as values.
For example, {1:0, 2:1, 0:2} means (m0, w1), (m1, w2), (m2, w0) is a stable matching.


You CAN:
1. Modify the function 'match' in match.py. You have to keep the existing arguments, since they are for grading. The grading procedure is similar to running selfcheck.py. Make sure your implementation would not make selfcheck fail to execute.
2. Add supporting functions to match.py. 
3. Use selfcheck.py to test the correctness of your code. Note that the given testing cases are a part of testing cases for grading. Passing every test case in selfcheck does not mean getting full credits.
4. Execute match.py to test on specific test case. To test on test case 3: 
>>> python match.py 3

You CAN NOT:
1. Import any library.
2. Modify any existing code except the function "match" in match.py. 
