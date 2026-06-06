def palindrome(num):
    reverse=0
    temp=num
        
    while temp>0:
        digit=temp%10
        reverse=reverse*10+digit
        temp=temp//10
    if reverse==num:
        return True
    return False
print(palindrome(21))

