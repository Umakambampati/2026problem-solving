def alphapyramid(n):
    for i in range(n):
        for j in range(i,n):
            print(' ',end=' ')
        for j in range(i+1):
            print(chr(65+j),end=' ')
        for j in range(i-1,-1,-1):
            print(chr(65+j),end=' ')
        print()
alphapyramid(6)
