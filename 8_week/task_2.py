'''
https://leetcode.com/problems/longest-nice-subarray/?envType=problem-list-v2&envId=sliding-window
'''

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        ans = 0
        i_left = 0
        current_bitwise_or = 0
        for i_right in range(len(nums)):
            while (current_bitwise_or & nums[i_right]) != 0:
                current_bitwise_or ^= nums[i_left]
                i_left += 1
            current_bitwise_or |= nums[i_right]
            ans = max(ans, i_right - i_left + 1)
        return ans