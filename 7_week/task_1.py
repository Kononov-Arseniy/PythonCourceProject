'''
https://leetcode.com/problems/get-equal-substrings-within-budget/?envType=problem-list-v2&envId=sliding-window
'''

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        #s = "abcd"
        #t = "acde"
        #maxCost = 0
        asci = []
        #print(ord(s[1]) - ord(t[1]))
        for i in range(0,len(s)):
            asci.append(abs(ord(s[i]) - ord(t[i])))
        i_right = 0
        i_left = 0
        ans = 0
        cntCost = maxCost
        cntlen = 0
        while (i_right < len(s)):
            if cntCost - asci[i_right] >= 0:
                cntCost -= asci[i_right]
                cntlen += 1
                ans = max(ans,cntlen)
                i_right += 1
            elif i_right == i_left:
                i_left += 1
                i_right += 1
            else:
                ans = max(ans,cntlen)
                cntCost += asci[i_left]
                cntlen -= 1
                i_left += 1
        return ans