def prime(num):
    is_prime=True
    if num==1 or num<=/0:
        return False
    for i in range(2,num):
        if num%i==0:
            is_prime=False
            break
    return is_prime
print(prime(8))