'''
https://leetcode.com/problems/most-profit-assigning-work/?envType=problem-list-v2&envId=array
'''

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        ans = 0
        dp = []
        for i in range(0,len(difficulty)):
            newarr = [difficulty[i], profit[i]]
            dp.append(newarr)
        dp = sorted(dp)
        worker = sorted(worker)
        worker.sort()
        ans = 0
        dollars = 0
        i = 0
        for w in worker:
            while i < len(dp) and dp[i][0] <= w:
                dollars = max(dollars, dp[i][1])
                i += 1
            ans += dollars
        return(ans)
