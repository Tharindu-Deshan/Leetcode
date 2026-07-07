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

def binary_search_recursion(array,target):
    left = 0
    right= len(array)-1
    mid = (left+right)//2
    if(len(array)==0):
        return False
    elif(array[mid]==target):
        return True
    elif(array[mid]<=target):
        return binary_search_recursion(array[mid+1:],target)
    else:
        return binary_search_recursion(array[:mid],target)

    #need to look at this 
def binary_search_recursion_v2(array, target, left=0, right=None):
    if right is None:
        right = len(array) - 1
    if left > right:          # base case: range is empty
        return False
    mid = (left + right) // 2
    if array[mid] == target:
        return True
    elif array[mid] < target:
        return binary_search_recursion_v2(array, target, mid + 1, right)
    else:
        return binary_search_recursion_v2(array, target, left, mid - 1)


list_1=[7,8,9,10,100]
print(binary_search(list_1,10))
print(binary_search_recursion(list_1,108))