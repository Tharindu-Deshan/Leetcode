def binarySearch(arr, targetVal):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == targetVal:
            return True
        
        if arr[mid] < targetVal:
            left = mid + 1
        else:
            right = mid - 1
    return False

def search(nums, target):

        def is_sorted(partial_list):
                if(partial_list[0]<=partial_list[-1]):
                        return  True
                else:
                        return False

        mid = len(nums)//2
        left_half=nums[0:mid]
        right_half=nums[mid+1:]

        if(nums[mid]==target):
                return True       
        elif(is_sorted(left_half)) and (nums[mid]<=target):
                return binarySearch(left_half,target)
        else:
             return  search(right_half,target)

list1=[4,6,8,9,10,11,12,1,2,3]
print(search(list1,23))