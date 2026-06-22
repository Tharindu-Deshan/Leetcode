def binary_search(array,target):
    left=0
    right=len(array)-1
    while(left<=right):
        mid=(left+right)//2 
        if(array[mid]==target):
            return True
        elif(target<=array[mid]):
            right=mid-1
        else:
            left=mid+1
    return False

list_1=[7,8,9,10]
print(binary_search(list_1,100))