#You are given an array of unique integers salary where salary[i] is the salary of the ith employee.
#Return the average salary of employees excluding the minimum and maximum salary.

from typing import List

class Solution:
    def average(self, salary: List[int]) -> float:
        # Take a sum all of values in list, then subtract min and max salary
        # Get the average by dividing the result by len of list - 2 (min and max)
        return (sum(salary) - min(salary) - max(salary)) / (len(salary) - 2)

salary = [4000,3000,1000,2000]
#salary = [1000,2000,3000]
sol = Solution()
print(sol.average(salary))