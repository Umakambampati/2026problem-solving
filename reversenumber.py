def reversenumber(n):
    for i in range(n):
        for j in range(i,0,-1):
            print(j,end=' ')
        print()
reversenumber(6)
