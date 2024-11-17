'''
https://leetcode.com/problems/longest-substring-without-repeating-characters/?envType=problem-list-v2&envId=sliding-window
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i_left = 0
        i_right = 0
        ans = 0
        s_cnt = ""
        cnt_ans = 0
        if len(s) != 0:
            while i_right != len(s):
                if s[i_right] not in s_cnt:
                    s_cnt += s[i_right]
                    cnt_ans += 1
                    ans = max(cnt_ans, ans)
                    i_right += 1
                else:
                    i_left += 1
                    ans = max(cnt_ans, ans)
                    cnt_ans -= 1
                    s_cnt = s_cnt[1:]
        return ans