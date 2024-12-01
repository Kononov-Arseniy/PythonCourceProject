'''
https://leetcode.com/problems/longest-consecutive-sequence/?envType=problem-list-v2&envId=hash-table
'''
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        ans = 0

        if nums:
            for num in num_set:
                if num - 1 not in num_set:
                    cur_n = num
                    cur_str = 1

                    while cur_n + 1 in num_set:
                        cur_n += 1
                        cur_str += 1

                    ans = max(ans, cur_str)

        return ans
