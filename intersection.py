def intersection(arr1,arr2):
    unique=[]
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if arr1[i]==arr2[j]:
                if arr1[i] not in unique:
                    unique.append(arr1[i])
    return unique
print(intersection([1,2,2,1],[2,2]))