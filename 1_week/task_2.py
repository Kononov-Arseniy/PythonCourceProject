'''
https://leetcode.com/problems/longest-substring-without-repeating-characters/description/?envType=problem-list-v2&envId=string
'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
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
                #print(0)
            elif not(s[i] in news):
                news += s[i]
                i += 1
                cnt += 1
                #print(1)
            else:
                if cnt > ans:
                    ans = cnt
                fl_count = 0
                news = ""
                i = i_start + 1
                cnt = 0
                #print(2)
        if cnt > ans:
            ans = cnt
        return ans