'''
https://leetcode.com/problems/multiply-strings/?envType=problem-list-v2&envId=string
'''

class Solution(object):
    def multiply(self, num1, num2):
        ans = 0
        for i in range(0,len(num1)):
            for j in range(0,len(num2)):
                ans += int(num1[i]) * 10**(len(num1)-i-1) * int(num2[j]) * 10**(len(num2)-j-1)
        return str(ans)