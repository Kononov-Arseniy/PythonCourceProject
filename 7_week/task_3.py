'''
https://leetcode.com/problems/maximum-sum-of-almost-unique-subarray/?envType=problem-list-v2&envId=sliding-window
'''

class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        max_sum = 0
        window_start = 0 
        element_count = {}
        for window_end in range(len(nums)):
            right_element = nums[window_end]
            element_count[right_element] = element_count.get(right_element, 0) + 1
            if window_end >= k - 1:
                if len(element_count) >= m:
                    current_sum = sum(nums[window_start:window_end + 1])
                    max_sum = max(max_sum, current_sum)
                left_element = nums[window_start]
                element_count[left_element] -= 1
                if element_count[left_element] == 0:
                    del element_count[left_element]
                window_start += 1   
        return max_sum