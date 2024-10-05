'''
https://leetcode.com/problems/container-with-most-water/?envType=problem-list-v2&envId=array
'''

class Solution(object):
    def maxArea(self, heights):
        #heights = [1,8,6,2,5,4,8,3,7]
        i1 = 0
        i2 = len(heights) - 1
        ans = min(heights[i1],heights[i2]) * (len(heights) - 1)
        while i1 != i2:
            if heights[i1] < heights[i2]:
                i1 += 1
            else:
                i2 -= 1
            if ans < min(heights[i1],heights[i2]) * (i2 - i1):
                ans = min(heights[i1],heights[i2]) * (i2 - i1)
        return(ans)