def search(nums, target):


        def is_sorted(partial_list):
                if(partial_list[0]<=partial_list[-1]):
                        return  True
                else:
                        return False


        mid = len(nums)//2

        if(nums[mid]==target):
                return True
        
        elif nums[mid]<=target:
                #target in right side
                pass
        else:
                #left side sorted
                
                pass

list1=[4,6,8,1,2,3]
print(search(list1,1))