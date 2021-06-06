def lcs(X, Y):
    m = len(X)
    n = len(Y)

    C = [[0]*(n + 1) for i in range(m + 1)]
    subsequence = []

#zad 2
    for i in range(m):
        for j in range(n):
            if X[i]==Y[j]:
                C[i][j]=C[i-1][j-1]+1
            else:
                C[i][j]=max(C[i-1][j], C[i][j-1])
            print(C[i][j], end='')
        print(" ")

#zad 3
    m = len(X)-1
    n = len(Y)-1
    while m >= 0:
        while n>= 0 and m>=0:
            if X[m]==Y[n]:
                subsequence.insert(0, X[m])
                m-=1
                n-=1
            elif C[m-1][n]>=C[m][n-1]:
                m-=1
            elif C[m-1][n]<C[m][n-1]:
                n-=1
            else:
                n-=1
        m-=1
    return subsequence

x = "BDCABA"
y = "ABCBDAB"
print(lcs(x, y))

