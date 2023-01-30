n=int(input("Enter range : "))
a=0
b=1
k=0
print(0)
print(1)
def fib(n,a,b,k):
    c=a+b
    a=b
    b=c
    k+=1
    if(k==n-2):
        return 0
    else:
        print(c)
        fib(n,a,b,k)
fib(n,a,b,k)