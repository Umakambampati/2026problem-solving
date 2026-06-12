def strongnumber(num):
    temp=num
    sum=0
    while temp>0:
        digit=temp%10
        fact=1
        for i in range(1,digit+1):
            fact*=i
        sum+=fact
        temp=temp//10
    return sum==num
print(strongnumber(145))

