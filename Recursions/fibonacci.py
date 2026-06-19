def fib(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return fib(n-1)+fib(n-2)
    
print(fib(10))


def dp_fib(n,memo):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    elif(n in memo):
        return memo[n]
    else:
        x=dp_fib(n-1,memo)+dp_fib(n-2,memo)
        if (n not in memo):
            memo[n]=x
        return dp_fib(n-1,memo)+dp_fib(n-2,memo)

def dp_fib_main(n):
    memo={}
    return dp_fib(n,memo)

print(dp_fib_main(50))