'''
https://leetcode.com/problems/kth-largest-element-in-an-array/?envType=problem-list-v2&envId=array&status=SOLVED
'''

class Solution(object):
    def findKthLargest(self, arr, k):
        nums = [0] * 20001
        #k = int(input())
        ans = 0
        for i in range(0,len(arr)):
            nums[arr[i] + 10000] += 1
        #print(nums)
        for i in range(len(nums)-1,-1,-1):
            if nums[i] != 0:
                if nums[i] - k < 0:
                    k = k - nums[i]
                else:
                    ans = i - 10000
                    break
        return(ans)