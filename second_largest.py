def second_largest(arr1):
    largest=float("-inf")
    second_largest=float("-inf")
    for i in range(len(arr1)):
        if arr1[i]>largest:
            second_largest=largest
            largest=arr1[i]
        elif arr1[i]>second_largest and arr1[i]<largest:
            second_largest=arr1[i]
    return second_largest
print(second_largest([2,3,7,3,9]))
