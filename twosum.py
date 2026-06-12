# def two_sum(arr1,target):
#     for i in range(len(arr1)):
#         for j in range(i+1,len(arr1)):
#             if arr1[i]+arr1[j]==target:
#                 return i,j
# print(two_sum([2, 7, 11, 15],9))

# approach2:
def twosum(arr1,target):
    dict1={}
    for i,num in enumerate(arr1):
        need=target-num
        if need in dict1:
            return [dict1[need],i]
        dict1[num]=i
print(twosum([2,7,11,15],9))

