# arr1=[0,1,0,3,12]
# arr2=[0]*len(arr1)
# l2=[]
# for num in arr1:
#     if num!=0:
#         l2.append(num)
# for i in range(len(l2)):
#     arr2[i]=l2[i]
# print(arr2)

# approach2:
def movezeros(arr1):
    left=0
    for right in range(len(arr1)):
        if arr1[right]!=0:
            arr1[left],arr1[right]=arr1[right],arr1[left]
            left+=1
    return arr1
print(movezeros([0,1,3,0,12]))