def fullpyramid(n):
    for i in range(5):
        for j in range(i,n):
            print(' ',end=' ')
        for j in range(i):
            print('*',end=' ')
        for j in range(i+1):
            print('*',end=" ")
        print()
fullpyramid(5)