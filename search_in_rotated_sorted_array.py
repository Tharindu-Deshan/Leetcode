def search(nums, target: int) -> int:
        mid = len(nums)//2
        if(nums[mid]==target):
                return True
        elif (nums[mid-1]<nums[mid]):
                if(nums[0]<=target and nums[mid]>=target):
                        search(nums[:mid+1],target)

                else:
                        return -1

        else:
                # right side is sorted
                if(nums[mid]<=target and nums[-1]>=target):
                        search(nums[mid:],target)
                else:
                        return -1


list1=[4,6,8,1,2,3]
print(search(list1,1))