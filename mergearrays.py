def mergearray(arr,arr2):
    list3=arr+arr2
    for i in range(len(list3)):
        for j in range(len(list3)-1):
            if list3[j]>list3[j+1]:
                list3[j],list3[j+1]=list3[j+1],list3[j]
    return list3
print(mergearray([1,3,5],[2,4,6]))