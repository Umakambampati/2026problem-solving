def productofdigits(num):
    num=abs(num)
    product=1
    if num==0:
        return 0
    while num!=0:
        digit=num%10
        product*=digit
        num=num//10
    return product
print(productofdigits(0))
