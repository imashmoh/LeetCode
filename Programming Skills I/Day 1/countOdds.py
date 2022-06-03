# Given two non-negative integers low and high.
# Return the count of odd numbers between low and high (inclusive).

from typing import List

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        diff = high - low
        if(diff % 2 != 0):
            # if diff between high and low is odd, 
            # then odd number count in the range is (diff + 1) divided by 2
            return int((diff + 1)/ 2)
        elif(low % 2 != 0 and high % 2 != 0):
            # if diff between high and low is even,
            # and both high and low are odd,
            # then odd number count in the range is (diff divided by 2) + 1
            return int((diff / 2) + 1)
        else:
            # if diff between high and low is even,
            # and both high and low are not odd,
            # then odd number count in the range is (diff divided by 2)
            return int(diff/2)

low = int(input())
high = int(input())
sol = Solution()
print(sol.countOdds(low,high))