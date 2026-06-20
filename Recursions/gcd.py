def GCD(x,y):
    if(y==0):
        return x
    else:
        return GCD(y,x%y)
print(GCD(0,10))