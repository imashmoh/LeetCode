# Given an integer number n, return the difference between the product of its digits and the sum of its digits.

from functools import reduce

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod = 1
        a = [int(x) for x in str(n)]
        for i in a:
            prod *= i
        return prod - sum(a)
        
        # Solution 2
        # this solution has security risk hence no to be used in prod. check out stackoverflow answer to know why
        # https://stackoverflow.com/questions/35804961/python-eval-is-it-still-dangerous-if-i-disable-builtins-and-attribute-access
        #return eval('*'.join(str(n))) - eval('+'.join(str(n)))

        # solution 3
        # a = [int(x) for x in str(n)]
        # return reduce((lambda x, y: x * y), a) - reduce((lambda x, y: x + y), a)

#n = 244
#n = 4421
n = 123456
sol = Solution()
print(sol.subtractProductAndSum(n))