'''
https://leetcode.com/problems/simplify-path/?envType=problem-list-v2&envId=string&status=SOLVED
'''

class Solution(object):
    def simplifyPath(self, s):
        dop_arr = [""] * 3001
        #s = str(input())
        ans = "/"
        i = 1
        j = 0
        news = ""
        while i < len(s):
            if s[i] == '/' and news == "":
                i += 1
            elif s[i] == '/' and news == "..":
                if j != 0:
                    j -= 1
                    dop_arr[j] = ""
                    i += 1
                    news = ""
                else:
                    dop_arr[j] = ""
                    i += 1
                    news = ""
                #print(dop_arr)
            elif s[i] == '/' and news == ".":
                i += 1
                news = ""
            elif s[i] == '/':
                dop_arr[j] = news
                j += 1
                news = ""
                i += 1
                #print(dop_arr)
            else:
                news += s[i]
                i += 1
        if news != "":
            if news == "..":
                j -= 1
                dop_arr[j] = ""
            elif news != ".":
                dop_arr[j] = news
                j += 1
        for l in range(0,3000):
            if dop_arr[l] != "":
                ans += dop_arr[l] + '/'
        if ans != "/":
            ans = ans[:-1]
        return(ans)