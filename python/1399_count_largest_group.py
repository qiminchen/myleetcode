"""
Given an integer n. Each number from 1 to n is grouped according to the sum of its digits.
Return how many groups have the largest size.
Example 1:

Input: n = 13
Output: 4
Explanation: There are 9 groups in total, they are grouped according sum of its digits of numbers from 1 to 13:
[1,10], [2,11], [3,12], [4,13], [5], [6], [7], [8], [9]. There are 4 groups with largest size.
"""


class Solution:
    def countLargestGroup(self, n: int) -> int:
        res = {}
        for integer in range(1, n + 1):
            sums = sum([int(i) for i in str(integer)])
            if sums not in res:
                res[sums] = [integer]
            else:
                res[sums].append(integer)

        count = collections.Counter([len(v) for _, v in res.items()])
        max_key = max(count.keys())
        return dict(count)[max_key]
