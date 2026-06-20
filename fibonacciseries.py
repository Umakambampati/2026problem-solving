def fibonacciseries(n):
    a=0
    b=1
    if n==1:
        return 0
    if n==2:
        return 1
    for i in range(n):
        print(a,end=" ")
        a,b=b,a+b
fibonacciseries(7)
