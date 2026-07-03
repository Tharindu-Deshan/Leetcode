#here we use bottom up approach also known as tabulation.here we calculate small problems and apply them to next problems.
#we use those solution for next solutions

#0,1,1,2,3,5,8,13

def bottom_up(n):
    bottom_up_dict={0:0,1:1}
    if(n<=1):
        return n
    for i in range(2,n+1):
        bottom_up_dict[i]=bottom_up_dict[i-1]+bottom_up_dict[i-2]

    return bottom_up_dict[n]


def bottom_up_optimized(n):
    first_value=0
    next_value=1
    if(n<=1):
        return n
    for i in range(2,n+1):
        temp= first_value+next_value
        first_value=next_value
        next_value=temp

    return next_value


print(bottom_up(34))
print(bottom_up_optimized(34))