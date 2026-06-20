def countdigits(num):
    num=abs(num)
    if num==0:
        return 1
    else:
        count=0
        while num>0:
            count+=1
            num=num//10
        return count
print(countdigits(-78965))

