def reversedigits(num):
    reverse=0
    if num<0:
        num=abs(num)
        while num>0:
            digit=num%10
            reverse=reverse*10+digit
            num=num//10
        return -(reverse)
    while num>0:
        digit=num%10
        reverse=reverse*10+digit
        num=num//10
    return reverse
print(reversedigits(-987))
