'''
https://leetcode.com/problems/letter-combinations-of-a-phone-number/?envType=problem-list-v2&envId=string
'''


class Solution(object):
    def letterCombinations(self, s):
        list_leters = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        # s = str(input())
        ans = list()
        i = 0
        res_str = ""
        if len(s) != 0:
            for j in range(0, len(list_leters[int(s[i])])):
                if (len(s) > 1):
                    res_str += list_leters[int(s[i])][j]
                    for k in range(0, len(list_leters[int(s[i + 1])])):
                        if len(s) > 2:
                            res_str += list_leters[int(s[i + 1])][k]
                            for l in range(0, len(list_leters[int(s[i + 2])])):
                                if len(s) > 3:
                                    res_str += list_leters[int(s[i + 2])][l]
                                    for m in range(0, len(list_leters[int(s[i + 3])])):
                                        res_str += list_leters[int(s[i + 3])][m]
                                        ans.append(res_str)
                                        res_str = res_str[0:3]
                                    res_str = res_str[0:2]
                                else:
                                    res_str += list_leters[int(s[i + 2])][l]
                                    ans.append(res_str)
                                    res_str = res_str[0:2]
                            res_str = res_str[0:1]
                        else:
                            res_str += list_leters[int(s[i + 1])][k]
                            ans.append(res_str)
                            res_str = res_str[0:1]
                    res_str = res_str[0:0]
                else:
                    res_str += list_leters[int(s[i])][j]
                    ans.append(res_str)
                    res_str = res_str[0:0]
        return ans