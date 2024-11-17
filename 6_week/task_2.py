'''
https://leetcode.com/problems/minimum-size-subarray-sum/submissions/1455486685/?envType=problem-list-v2&envId=sliding-window
'''

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        i_left = 0
        cnt_sum = 0
        min_length = float("inf")
        for i_right in range(n):
            cnt_sum += nums[i_right]
            while cnt_sum >= target:
                min_length = min(min_length, i_right - i_left + 1)
                cnt_sum -= nums[i_left]
                i_left += 1
        return min_length if min_length != float("inf") else 0