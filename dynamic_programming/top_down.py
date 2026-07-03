#this is also known as memoization. this means we keep each problems solution and when each subproblem called another time we dont recalculate, 
#we just put that number

#the problem  is theres a recursion depth limit for example python limit is 1000.in this approach if we go to calculate fib(2000) it will hit the maximum depth

def top_down_fib(n,memo):
    if(n<=1):
        return n
    elif(n in memo):
        return memo[n]
    else:
        x= top_down_fib(n-1,memo)+top_down_fib(n-2,memo)
        memo[n]=x
        return x

def fib(n):
    memo={}
    return top_down_fib(n,memo)

print(fib(199))