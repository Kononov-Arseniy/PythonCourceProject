"""
https://leetcode.com/problems/string-to-integer-atoi/submissions/1397898288/?source=submission-noac
"""


class Solution(object):
    def myAtoi(self, s1):
        # s1 = str(input())
        i = 0
        s = ""
        fl_deg = 0
        for i in range(0, len(s1)):
            if s1[i] != " ":
                s += s1[i]
                fl_deg = 1
            elif s1[i] == " " and fl_deg == 1:
                s += s1[i]
                # print(s)
        ans = "0"
        fl = 0
        fl_minus = 0
        fl_plus = 0
        deg = "0123456789-"
        for i in range(0, len(s)):
            if i == 0:
                if s[i] == "+":
                    fl_plus = 1
                    ans = "0"
                elif not (s[i] in deg):
                    ans = "0"
                    break
                elif s[i] == "-":
                    fl_minus = 1
                    ans = "0"
                elif s[i] != "0":
                    ans = s[i]
                    fl = 1
            else:
                if fl_minus == 1 and i == 1:
                    ans = "-"
                if not (s[i] in deg) and fl == 0:
                    ans = "0"
                    break
                if not (s[i] in deg):
                    break
                elif s[i] == "-" and fl == 0:
                    ans = "0"
                    break
                elif s[i] == "-":
                    break
                elif s[i] != "0" and fl == 0:
                    ans += s[i]
                    fl = 1
                elif s[i] != "0" and fl == 1:
                    ans += s[i]
                elif s[i] == "0" and fl == 1:
                    ans += s[i]
        if s1 == "":
            ans = "0"
        news = ""
        if fl_plus == 1 and len(ans) > 1:
            for i in range(1, len(ans)):
                news += ans[i]
            ans = news
        if int(ans) < (-2) ** 31:
            ans = str((-2) ** 31)
        if int(ans) > 2**31 - 1:
            ans = str(2**31 - 1)
        return int(ans)
