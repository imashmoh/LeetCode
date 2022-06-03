from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Solution 1
        # nums.sort()
        # for i in range(len(nums) - 1):
        #     if(nums[i] == nums[i+1]):
        #         return True
        # return False

        # Solution 2    
        # return(len(nums) != len(set(nums)))

        # Solution 3
        # First Create an empty set, then sort the nums 
        # next loop each element and check if its present in the distinct set 
        # if element present then return true else add the element in the set
        # distinctNumSet = set()
        # nums.sort()
        # for i in nums:
        #     if i in distinctNumSet:
        #         return True
        #     else:
        #         distinctNumSet.add(i)
        # #if there are no duplicate values then this statment will execute
        # return False       

        # Solution 4
        # First Create an empty dictionary, then sort the nums 
        # next loop each element and check if its present in the dictionary 
        # if element present then return true else add the element in the set
        distinctNum = {}
        nums.sort()
        for i in nums:
            if i in distinctNum.keys():
                return True
            else:
                distinctNum[i] = 1
        #if there are no duplicate values then this statment will execute
        return False 

nums = [1,2,3,4,5,6]
sol = Solution()
print(sol.containsDuplicate(nums))    
#print(containsDuplicate(containsDuplicate, nums))