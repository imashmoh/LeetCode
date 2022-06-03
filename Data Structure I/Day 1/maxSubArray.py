# Given an integer array nums, find the contiguous subarray (containing at least one number) 
# which has the largest sum and return its sum.
# A subarray is a contiguous part of an array.
# Example 1:
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:        
        accumulatedSum = maxSum = nums[0]
        if(len(nums) == 1): 
            #if array has only one element no need to further calculation
            return maxSum
        else:
            for i in range(1, len(nums)):
                accumulatedSum = max(nums[i], accumulatedSum + nums[i])
                maxSum = max(maxSum, accumulatedSum)
        return maxSum

#nums = [-2,1,-3,4,-1,2,1,-5,4]
nums = [1,2,3,4,5,6]
#nums = list(map(int, input().rstrip((",")).split()))
sol = Solution()
print(sol.maxSubArray(nums))