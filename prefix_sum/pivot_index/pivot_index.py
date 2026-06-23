def pivotIndex( nums):
        """
        :type nums: List[int]
        :rtype: int
        Input: nums = [1,7,3,6,5,6]
        Output: 3

        """
        for i in range(len(nums)):
            left_sum=sum(nums[:i])
            right_sum=sum(nums[i+1:])
            if(left_sum==right_sum):
                  return i
            else:
                  left_sum=0
                  right_sum=0
        return -1

def pivotIndexOptimized(nums):
    for i in range(1,len(nums)):
        nums[i]=nums[i]+nums[i-1]

    for i in range(len(nums)):
        if(i==0):
            left_sum=0
            right_sum=nums[-1]-nums[i]
        else:
            left_sum=nums[i-1]
            right_sum=nums[-1]-nums[i]               
            
        if(left_sum==right_sum):
            return i 
    return -1       


nums = [1,7,3,6,5,6]
nums = [2, -1, 1]
print(pivotIndexOptimized(nums))

