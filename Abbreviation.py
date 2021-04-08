"""
This solution is for the Abbreviation problem as posted on Hackerrank
(https://www.hackerrank.com/challenges/abbr?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dynamic-programming)

Based on the logic of the Longest Common Subsequence explanation video here
(https://www.youtube.com/watch?v=ASoaQq66foQ)
"""

a='daBcd'
b='ABC'

T = [[False for j in range(len(b)+1)] for i in range(len(a)+1)]

# base case
# f('','')
T[0][0]=True

for i in range(1,len(a)+1):
    for j in range(len(b)+1):
        # base case
        # f('xy','') if a lower can drop
        # f('xyZa','') if upper encountered, then subsequent continue False
        if j==0:
            if a[i-1].islower():
                T[i][j] = T[i-1][j]

        ### if match ###
        # a is upper case
        # must match cause cannot drop
        elif a[i-1] == b[j-1]:
            T[i][j] = T[i-1][j-1]

        # a is lower case
        # has the option to drop OR match
        elif a[i-1].upper() == b[j-1]:
            T[i][j] = max(T[i - 1][j - 1],T[i - 1][j])

        else:
            ### if don't match ###

            # a is upper case
            # end state cause cannot drop
            if a[i-1].isupper():
                T[i][j] = False
            else:
                # a is lower case
                # drop it
                T[i][j] = T[i-1][j]

print('YES' if T[-1][-1] == True else 'NO')

