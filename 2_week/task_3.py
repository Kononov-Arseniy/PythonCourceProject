'''
https://leetcode.com/problems/reverse-words-in-a-string/?envType=problem-list-v2&envId=string&status=SOLVED
'''

class Solution(object):
    def reverseWords(self, s):
        #s = str(input())
        s = s.split()
        ans = ""
        for i in range(len(s)-1,-1,-1):
            ans += s[i] + ' '
        ans = ans[:-1]
        return(ans)