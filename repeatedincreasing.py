def increasingtraingle(n):
    for i in range(1,n):
        for j in range(1,i+1):
            print(i,end=' ')
        print()
increasingtraingle(6)