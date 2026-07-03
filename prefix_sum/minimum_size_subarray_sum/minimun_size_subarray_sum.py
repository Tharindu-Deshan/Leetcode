def minSubArrayLen(target, nums):
      """
      :type target: int                                 
      :type nums: List[int]
      :rtype: int

      Input: target = 7, nums = [2,3,1,2,4,3]            prefix_sum = [2, 5, 6, 8, 12, 15]
      Output: 2
      Explanation: The subarray [4,3] has the minimal length under the problem constraint - greater than or equal to target.
      """
      min_length =0
      prefix_sum_arr=nums[:]

      for i in range(1,len(nums)):
            prefix_sum_arr[i]=prefix_sum_arr[i]+prefix_sum_arr[i-1]

      for i in range(len(nums)):
            for j in range(i,len(nums)):
                  if (i==j):
                        if((nums[i]>=target)):
                              return 1
                  else:
                        sum_bet_i_j=0
                        curr_length=j-i+1
                        if(i==0):
                              sum_bet_i_j=prefix_sum_arr[j]
                        else:
                              sum_bet_i_j=prefix_sum_arr[j]-prefix_sum_arr[i-1]

                        if((sum_bet_i_j>=target)):
                              if((min_length==0) or (min_length >curr_length)):
                                    min_length=curr_length
                 
      return min_length

                              
      

nums = [2,3,1,2,4,3]
x=minSubArrayLen(7,nums)
print(x)
      
                      
                  
            