'''
https://leetcode.com/problems/compare-version-numbers/?envType=problem-list-v2&envId=string&status=SOLVED
'''

class Solution(object):
    def compareVersion(self, ver1, ver2):
        ver1 = ver1.split('.')
        ver2 = ver2.split('.')
        # print(ver1)
        # print(ver2)
        for i in range(0, len(ver1)):
            ver1[i] = str(int(ver1[i]))
        for i in range(0, len(ver2)):
            ver2[i] = str(int(ver2[i]))
        if len(ver1) > len(ver2):
            lenth = len(ver1)
            for i in range(len(ver2), len(ver1)):
                ver2.append('0')
        else:
            lenth = len(ver2)
            for i in range(len(ver1), len(ver2)):
                ver1.append('0')
        ans = 0
        for i in range(0, lenth):
            if int(ver1[i]) > int(ver2[i]):
                ans = 1
                break
            elif int(ver1[i]) < int(ver2[i]):
                ans = -1
                break
        return (ans)
        # print(ver1)
        # print(ver2)
