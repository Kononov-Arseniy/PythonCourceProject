'''
https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/?envType=problem-list-v2&envId=sliding-window
'''

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)
        cntKol = 0
        cnts = ""
        ans = 0
        alph = "aeiou"
        for i in range(0,k):
            if s[i] in alph:
                cntKol += 1
            cnts += s[i]
        i_right = k
        ans = max(ans,cntKol)
        while i_right < n:
            if (cnts[0] in alph):
                cntKol -= 1
            if s[i_right] in alph:
                cntKol += 1
            cnts = cnts[1:] + s[i_right]
            ans = max(cntKol,ans)
            i_right += 1
        return ans