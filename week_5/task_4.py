'''
https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/1428812128/?envType=problem-list-v2&envId=hash-table
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        i = 0
        i_start = 0
        news = ""
        cnt = 0
        fl_count = 0

        while i < len(s):
            if fl_count == 0:
                news += s[i]
                i_start = i
                fl_count = 1
                cnt = 1
                i += 1
            elif s[i] not in news:
                news += s[i]
                i += 1
                cnt += 1
            else:
                if cnt > ans:
                    ans = cnt
                fl_count = 0
                news = ""
                i = i_start + 1
                cnt = 0

        if cnt > ans:
            ans = cnt

        return ans
