'''
https://leetcode.com/problems/jump-game/?envType=problem-list-v2&envId=array
'''

class Solution(object):
    def canJump(self, arr):
        finish = len(arr) - 1
        for i in range(len(arr) - 2, -1, -1):
            if arr[i] + i >= finish:
                finish = i
        if finish == 0:
            ans = True
        else:
            ans = False
        return(ans)