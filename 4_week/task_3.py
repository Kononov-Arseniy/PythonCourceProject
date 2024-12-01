'''
https://leetcode.com/problems/sum-of-even-numbers-after-queries/?envType=problem-list-v2&envId=array
'''

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        summ = 0
        for i in range(0,len(nums)):
            if nums[i] % 2 == 0:
                summ += nums[i]
        for i in range(0,len(queries)):
            #current = nums[queries[i][1]]
            if nums[queries[i][1]] % 2 == 0:
                summ -= nums[queries[i][1]]
            nums[queries[i][1]] += queries[i][0]
            if nums[queries[i][1]] % 2 == 0:
                summ += nums[queries[i][1]]
            ans.append(summ)
        return(ans)
