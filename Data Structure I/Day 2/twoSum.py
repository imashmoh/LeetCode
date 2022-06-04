# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]

from typing import List
from unittest import result
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Solution 1 - Brute Force 
        # for i in range(0, len(nums)):
        #     for j in range(1, len(nums)):
        #         if i == j : pass
        #         elif target == nums[i] + nums[j]:
        #             return [i, j]
        
        # Solution 2 :  using Hint 2
        # So, if we fix one of the numbers, say x, we have to scan the entire array to find the next number y
        # which is value - x, where value is the input parameter. 
        # Can we change our array somehow so that this search becomes faster?
        pair = dict() 
        for i in range(0, len(nums)):
            x = nums[i] # i1 x = 2, i2 x = 7
            y = target - x # i1 y = 7, i2 y = 2  
            if x in pair: # i1 pair is empty, i2 x = 7 is present in pair
                return [i, pair[x]] # return current index and pair index
                pass
            else: 
                pair[y] = i # i1 pair = { y : i } = {7 : 0}     

        # solution 3
        # a = [int(x) for x in str(n)]
        # return reduce((lambda x, y: x * y), a) - reduce((lambda x, y: x + y), a)


sol = Solution()
nums = [2,7,11,15]
target = 9
print(sol.twoSum(nums, target))

nums = [3,2,4]
target = 6
print(sol.twoSum(nums, target))

nums = [3,3]
target = 6
print(sol.twoSum(nums, target))

nums = [2,5,5,11]
target = 10
print(sol.twoSum(nums, target))