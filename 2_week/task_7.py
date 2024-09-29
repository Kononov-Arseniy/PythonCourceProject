#не дорешано 142/290

s = str(input())
k = 0
if s != "" and s[0] != '0' and not("00" in s):
    if len(s) != 1:
        k = 1
        l = len(s)
        s += '@'
        for i in range(1,l):
            if s[i] == '0' and int(s[i-1]) > 2:
                k = 0
                break
            elif s[i] == '0':
                k = k
            elif ((int(s[i-1]) == 2 and int(s[i]) < 7) or int(s[i-1]) == 1) and s[i+1] != '0':
                k += 1

    else:
        k = 1
print(k)
