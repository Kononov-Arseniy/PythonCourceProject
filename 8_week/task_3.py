'''
https://leetcode.com/problems/count-the-number-of-substrings-with-dominant-ones/?envType=problem-list-v2&envId=sliding-window
'''

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0
        zero_indices = []

        for i, char in enumerate(s):
            if char == '0':
                zero_indices.append(i)

            l = 0
            while l <= len(zero_indices):
                target_length = l * l + l
                if target_length > i + 1:
                    break
                left_index = zero_indices[-1 - l] if l < len(zero_indices) else -1
                right_index = zero_indices[-l] if l > 0 else i
                min_length = i - right_index + 1
                max_length = i - left_index
                
                if min_length >= target_length:
                    count += max_length - min_length + 1
                elif min_length <= target_length <= max_length:
                    count += max_length - target_length + 1

                l += 1

        return count