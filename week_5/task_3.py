'''
https://leetcode.com/problems/powerful-integers/?envType=problem-list-v2&envId=hash-table
'''
from typing import List

class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        powerful = []
        x_pow = 1

        while x_pow <= bound:
            y_pow = 1
            while x_pow + y_pow <= bound:
                powerful.append(x_pow + y_pow)
                if y == 1:
                    break
                y_pow *= y

            if x == 1:
                break
            x_pow *= x

        return list(set(powerful))
