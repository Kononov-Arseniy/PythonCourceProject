'''
https://leetcode.com/problems/find-the-power-of-k-size-subarrays-i/submissions/1467625197/?envType=problem-list-v2&envId=sliding-window
'''

class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums

        ans = []
        i_left = 0
        i_right = 1
        while i_right < len(nums):
            if nums[i_right] - nums[i_right-1] != 1:
                while i_left < i_right and i_left + k - 1 < len(nums):
                    ans.append(-1)
                    i_left += 1
                i_left = i_right
            elif i_right - i_left == k - 1:
                ans.append(nums[i_right])
                i_left += 1
            i_right += 1
        return ans