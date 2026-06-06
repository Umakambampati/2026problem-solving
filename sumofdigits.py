def sumofdigits(num):
    num=abs(num)
    sum=0
    if num==0:
        return 0
    while num!=0:
        digit=num%10
        sum+=digit
        num=num//10
    return sum
print(sumofdigits(-897))