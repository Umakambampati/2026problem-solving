def fullpyramid(n):
    for i in range(n):
        for j in range(i,n):
            print(' ',end=' ')
        for j in range(i):
            print('*',end=' ')
        for j in range(i+1):
            print('*',end=" ")
        print()
fullpyramid(5)
def inverted(n):
    for i in range(1,n):
        for j in range(i+1):
            print(' ',end=" ")
        for j in range(i,n-1):
            print('*',end=" ")
        for j in range(i,n):
            print('*',end=' ')
        print()
inverted(5)