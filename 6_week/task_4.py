'''
https://leetcode.com/problems/permutation-in-string/?envType=problem-list-v2&envId=sliding-window
'''

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ans = False
        if len(s1) <= len(s2):
            right = len(s1) - 1
            cnt_s = s2[:right + 1]
            alph = "abcdefghijklmnopqrstuvwxyz"
            while right != len(s2) - 1:
                if all(s1.count(char) == cnt_s.count(char) for char in alph):
                    return True
                right += 1
                cnt_s = cnt_s[1:] + s2[right]
            if all(s1.count(char) == cnt_s.count(char) for char in alph):
                ans = True
        return ans