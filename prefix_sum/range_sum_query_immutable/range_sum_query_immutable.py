class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.prefix_sum = list(nums)
        for i in range(1,len(nums)):
            self.prefix_sum[i]=self.prefix_sum[i]+self.prefix_sum[i-1]
            print(self.prefix_sum[i])
        

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        print(self.prefix_sum)
        if(right<left):
            return 0
        elif(left==0):
            value= self.prefix_sum[right]
        else:
            value= self.prefix_sum[right]-self.prefix_sum[left-1]
        return value

        

        


# Your NumArray object will be instantiated and called as such:
nums=[-2, 0, 3, -5, 2, -1]

obj = NumArray(nums)
param_1 = obj.sumRange(2,5)
print(param_1)


# [-2, 0, 3, -5, 2, -1]
# [-2,-2, 1,-4, -2, -3]

# 2,5

# 0,5