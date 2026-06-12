def primerange(start,stop):
    list1=[]
    for i in range(start,stop+1):
        if i<=1:
            continue
        is_prime=True
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                is_prime=False
                break
        if is_prime:
            list1.append(i)
    return list1
print(primerange(1,10))
            