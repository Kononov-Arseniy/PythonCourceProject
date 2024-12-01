'''
https://leetcode.com/problems/sort-an-array/?envType=problem-list-v2&envId=array
'''

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        dp = [0] * 1000000
        for i in range(0,len(nums)):
            dp[500000 + nums[i]] += 1
        ans = []
        for i in range(0,len(dp)):
            for j in range(0,dp[i]):
                ans.append(i-500000)
        return(ans)
