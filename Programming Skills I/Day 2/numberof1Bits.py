# Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).
# Example 1:
# Input: n = 00000000000000000000000000001011
# Output: 3
# Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.

# how do we do this?

# 1. take count as 0
# 2. '&' allows to figure out which number we currently have:
#    0 & 0 = 0
#    1 & 0 = 0; 0 & 1 = 0
#    1 & 1 = 1
#    => So, at each step we can get whether 1 or 0 and then add it to count.
# 3. But we need to move one step to the right in bites term at each iteration
#    => >> is a way.

import collections


class Solution:
    def hammingWeight(self, n: int) -> int:
        # solution 1
        # count = 0
        # while n:
        #     count += (n & 1)
        #     n = n >> 1
        # return count
        # solution 2
        counter = collections.Counter(bin(n)[2:])
        return counter.get("1", 0)

n = 0b00000000000000000000000000001011
#n = 0b00000000000000000000000010000000
#n = 0b11111111111111111111111111111101
sol = Solution()
print(sol.hammingWeight(n))