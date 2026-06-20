def armstrong(num):
    result=0
    temp=num
    length=len(str(num))
    while temp>0:
        digit=temp%10
        result+=digit**length
        temp=temp//10
    return result==num
print(armstrong(153))