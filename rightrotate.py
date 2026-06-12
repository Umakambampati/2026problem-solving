def rightrotation(arr1,k):
    k=k%len(arr1)
    for _ in range(k):
        num=arr1[-1]
        for i in range(len(arr1)-1,0,-1):
            arr1[i]=arr1[i-1]
        arr1[0]=num
    return arr1
print(rightrotation([1,2,3,4,5],2))

