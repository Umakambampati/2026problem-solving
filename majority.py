def majority(arr2):
    n=len(arr2)//2
    dict1={}
    for num in arr2:
        if num not in dict1:
            dict1[num]=1
        else:
            dict1[num]+=1
    for key,value in dict1.items():
        if value>n:
            return key
print(majority([3, 3, 4, 2, 3, 3, 3]))