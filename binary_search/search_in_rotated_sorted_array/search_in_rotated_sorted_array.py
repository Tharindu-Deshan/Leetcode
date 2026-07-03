def search(nums, target):
    left=0
    right=len(nums)-1
    while(left<=right):
        mid=(left+right)//2
        if(nums[mid]==target):
            return True
        if(nums[left]<=nums[mid]):
            if(nums[left]<=target and target<=nums[mid] ):
                right=mid-1
            else:
                left=mid+1
        else:
            if(nums[mid]<=target and target<=nums[right]):
                left=mid+1
            else:
                right = mid-1
    return False


list1=[4,6,8,9,10,11,12,1,2,3]
print(search(list1,3))
