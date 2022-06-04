# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, 
# and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. 
# To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, 
# and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
# 
# Example 1:
# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

# I am not able to solve this, I will need to revisit this. 
# Following solution is taken from https://leetcode.com/problems/merge-sorted-array/discuss/1561318/Python-or-Explained

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # if the second array is empty, there's nothing to do
        if nums2:
            # pointer for each one of the arrays
            i = j = 0
            # while we don't reach the end of any of the arrays
            while i < m and j < n:
                # if the currect element of nums1 is bigger than the current element of nums2
                if nums1[i] > nums2[j]:
                    # insert the current element of nums2 into nums1 at the current
                    # position of nums1 that we are inspecting
                    nums1.insert(i, nums2[j])
                    # move the nums2 pointer
                    j+=1
                    # the insertion will push all elements beyond the position i to the back
                    # meaning that now the final valid element of of nums1 is at position m+1
                    m+=1
                # and we always move the nums1 pointer because either the current value of nums1 
                # is in the correct position or it was moved one poistion further in the array 
                # to accomodate one value from nums2
                i+=1
            # finally, if we didn't reach the end of nums2
            if j < n:
                # replace all the zeros at the end of nums1 with the rest of the values of nums2 
                # that are not in nums1
                nums1[m:] = nums2[j:]
            else:
                # otherwise, we inserted all `n` elements of nums2 into nums1 and,
                # in this case, we need to delete the last `n` elements of nums1 
                # (they are the zeros that we pushed back to acomodate the nums2 values)
                del nums1[-n:]

sol = Solution()
nums1 = [1,2,3,0,0,0] 
m = 3 
nums2 = [2,5,6] 
n = 3
sol.merge(nums1, m, nums2, n)
print(nums1)

nums1 = [1]
m = 1
nums2 = []
n = 0
sol.merge(nums1, m, nums2, n)
print(nums1)

nums1 = [0]
m = 0
nums2 = [1]
n = 1
sol.merge(nums1, m, nums2, n)
print(nums1)