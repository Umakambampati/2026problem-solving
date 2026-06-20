def leaders(arr1):
    unique=[]
    for i in range(len(arr1)):
        is_greater=True
        for j in range(i+1,len(arr1)):
            if arr1[i]<arr1[j]:
                is_greater=False
                break
        if is_greater:
            unique.append(arr1[i])
    return unique
print(leaders([16, 17, 4, 3, 5, 2]))