def sum_to_N(num):
    if (num==0):
        return num
    else:
        return num+sum_to_N(num-1)

print(sum_to_N(10))