# def buysell(arr1):
#     max_profit=0
#     for i in range(len(arr1)):
#         for j in range(i+1,len(arr1)):
#             if arr1[j]-arr1[i]>max_profit:
#                 max_profit=arr1[j]-arr1[i]
#     return max_profit
# print(buysell([7,6,4,3,1]))


def buysell(arr1):
    lowest_price=arr1[0]
    max_profit=0
    for i in range(1,len(arr1)):
        if arr1[i]<lowest_price:
            lowest_price=arr1[i]
        elif arr1[i]-lowest_price>max_profit:
            max_profit=arr1[i]-lowest_price
    return max_profit
print(buysell([7, 1, 5, 3, 6, 4]))
