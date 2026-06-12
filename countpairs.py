def countpairs(arr1,target):
    count=0
    for i in range(len(arr1)):
        for j in range(i+1,len(arr1)):
            if arr1[i]+arr1[j]==target:
                count+=1
    return count
print(countpairs([1,5,7,1],6))