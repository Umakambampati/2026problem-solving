def duplicate(arr1):
    dict1={}
    for num in arr1:
        if num not in dict1:
            dict1[num]=1
        else:
            dict1[num]+=1
    list1=[]
    for key,value in dict1.items():
        if value>1:
            list1.append(key)
    return list1
print(duplicate([1,2,2,3,3,4,4,5]))
            
