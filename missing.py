def missingnumber(arr1):
    xor=0
    for i in range(1,max(arr1)+1):
        xor^=i
    xor2=0
    for num in arr1:
        xor2^=num
    return xor^xor2
print(missingnumber([1,2,4,5,6]))