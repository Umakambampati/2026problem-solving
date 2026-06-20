def numberpyramid(n):
    for i in range(n):
        for j in range(i,n):
            print(' ',end=' ')
        for j in range(1,i+1):
            print(j,end=' ')
        for j in range(i-1,0,-1):
            print(j,end=' ')
        print()
numberpyramid(6)
    
