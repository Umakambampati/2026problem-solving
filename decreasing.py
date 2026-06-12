def decreasing(n):
    for i in range(n):
        for j in range(i,n):
            print('*',end=' ')
        print()
decreasing(5)