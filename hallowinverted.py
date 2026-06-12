def hallowinverted(n):
    for i in range(n):
        for j in range(i+1):
            print(' ',end=' ')
        for j in range(i,n-1):
            if j==i or i==0:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        for j in range(i,n):
            if j==n-1 or i==0:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()
hallowinverted(5)