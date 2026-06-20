def lcm(num1,num2):
    multiple=max(num1,num2)
    while True:
        if multiple%num1==0 and multiple%num2==0:
            return multiple
        multiple+=1
print(lcm(6,8))
        
