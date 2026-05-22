def two_sum_index(list,target):
    dict={}
    for i,num in enumerate(list):
        diff = target-num
        if(diff in dict):
            return i,dict[diff]
        dict[num]=i
    return
    
def two_sum_vals(list,target):
    seen_set= set()
    for i in list:
        diff = target-i
        if(diff in seen_set):
            return i,diff
        seen_set.add(i)
    return 

x=[1,3,4,6,7,0,6,4,3,5,6]

print(two_sum_index(x,8))
print(two_sum_vals(x,8))