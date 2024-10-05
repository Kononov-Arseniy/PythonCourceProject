'''
https://leetcode.com/problems/minimum-size-subarray-sum/?envType=problem-list-v2&envId=array
'''

class Solution(object):
    def minSubArrayLen(self, target, nums):
        # nums = [12,28,83,4,25,26,25,2,25,25,25,25,12]
        # target = int(input())
        ans = 0
        i1 = 0
        i2 = 1
        if nums[i1] >= target:
            ans = 1
        elif len(nums) > 1:
            summ = nums[i1] + nums[i2]
            res = 1000000
            while i1 != i2:
                if i2 == len(nums) - 1:
                    if summ < target:
                        break
                    elif summ >= target and i2 - i1 + 1 < res:
                        res = i2 - i1 + 1
                        summ -= nums[i1]
                        i1 += 1
                    elif summ >= target:
                        summ -= nums[i1]
                        i1 += 1
                    if i1 == i2 and nums[i1] >= target:
                        res = 1
                        break
                else:
                    if summ < target:
                        i2 += 1
                        summ += nums[i2]
                    elif summ >= target and i2 - i1 + 1 < res:
                        res = i2 - i1 + 1
                        summ -= nums[i1]
                        i1 += 1
                    elif summ >= target:
                        summ -= nums[i1]
                        i1 += 1
                    if i1 == i2 and nums[i1] >= target:
                        res = 1
                        break
            if res != 1000000:
                ans = res
        return (ans)