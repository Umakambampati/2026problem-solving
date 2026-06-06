def perfectnumber(num):
    total=0
    for i in range(1,num):
        if num%i==0:
            total+=i
    return total==num
print(perfectnumber(12))
