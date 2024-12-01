'''
https://leetcode.com/problems/set-matrix-zeroes/submissions/1428772468/?envType=problem-list-v2&envId=hash-table
'''
from typing import List

class Solution:
    def setZeroes(self, matr: List[List[int]]) -> None:
        rows = len(matr)
        cols = len(matr[0])

        for i in range(rows):
            for j in range(cols):
                if matr[i][j] == 0:
                    matr[i][j] = [matr[i][j], 0]
                else:
                    matr[i][j] = [matr[i][j], 1]

        for i in range(rows):
            for j in range(cols):
                if matr[i][j][1] == 0:
                    for x in range(cols):
                        matr[i][x][0] = 0
                    for x in range(rows):
                        matr[x][j][0] = 0

        for i in range(rows):
            for j in range(cols):
                matr[i][j] = matr[i][j][0]