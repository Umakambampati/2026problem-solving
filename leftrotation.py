def leftrotation(arr,k):
    k=k%len(arr)
    for _ in range(k):
        num=arr[0]
        for i in range(len(arr)-1):
            arr[i]=arr[i+1]
        arr[-1]=num
    return arr
print(leftrotation([1,2,3,4,5],2))