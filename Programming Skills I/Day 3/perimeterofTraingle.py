# Given an integer array nums, return the largest perimeter of a triangle with a non-zero area, formed from three of these lengths.
# If it is impossible to form any triangle of a non-zero area, return 0.

from typing import List

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        if (nums[0] + nums[1] > nums[2]) & (nums[0] + nums[2] > nums[1]) & (nums[1] + nums[2] > nums[0]):
            return sum(nums)
        else:
            return 0

sol = Solution()
sides = [2,1,2]
print(sol.largestPerimeter(sides))

sides = [1,2,1]
print(sol.largestPerimeter(sides))