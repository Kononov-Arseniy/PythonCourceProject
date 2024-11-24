'''
https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/?envType=problem-list-v2&envId=sliding-window
'''

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)    
        max_sum = 0
        current_sum = 0
        window = set()
        left = 0
            
        for right in range(n):
            while nums[right] in window:
                window.remove(nums[left])
                current_sum -= nums[left]
                left += 1
            window.add(nums[right])
            current_sum += nums[right]
            if right - left + 1 == k:
                max_sum = max(max_sum, current_sum)
                window.remove(nums[left])
                current_sum -= nums[left]
                left += 1
        return max_sum