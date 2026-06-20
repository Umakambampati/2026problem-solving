def positivesnegatives(arr1):
    positives=[]
    negatives=[]
    for i in range(len(arr1)):
        if arr1[i]>=0:
            positives.append(arr1[i])
        elif arr1[i]<0:
            negatives.append(arr1[i])
    return [positives+negatives]
print(positivesnegatives([-1, 2, -3, 4, 5, -6]))
