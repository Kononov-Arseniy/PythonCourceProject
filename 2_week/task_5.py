'''
https://leetcode.com/problems/complex-number-multiplication/?envType=problem-list-v2&envId=string
'''

class Solution(object):
    def complexNumberMultiply(self, num1, num2):
        degr = "0123456789"
        ans = ("")
        real = 1
        imaginary = 1
        fl1 = 0
        fl2 = 0
        str_deg = ""
        str_ima = ""
        deg = 1
        ima = 1
        for i in range(0, len(num1)):
            if i == 0 and num1[i] == '-':
                deg = -1
            elif num1[i] in degr and fl1 == 0:
                str_deg += num1[i]
                fl1 = 1
            elif num1[i] in degr and fl2 == 0 and fl1 == 1:
                str_deg += num1[i]
            elif num1[i] == '+' and num1[i + 1] == '-':
                ima = -1
                fl2 = 1
            elif num1[i] == '+':
                fl2 = 1
            elif num1[i] in degr and fl2 == 1 and fl1 == 1:
                str_ima += num1[i]
        deg = deg * int(str_deg)
        ima = ima * int(str_ima)
        fl3 = 0
        fl4 = 0
        str_deg = ""
        str_ima = ""
        for i in range(0, len(num2)):
            if i == 0 and num2[i] == '-':
                real = -1
            elif num2[i] in degr and fl3 == 0:
                str_deg += num2[i]
                fl3 = 1
            elif num2[i] in degr and fl4 == 0 and fl3 == 1:
                str_deg += num2[i]
            elif num2[i] == '+' and num2[i + 1] == '-':
                imaginary = -1
                fl4 = 1
            elif num2[i] == '+':
                fl4 = 1
            elif num2[i] in degr and fl4 == 1 and fl3 == 1:
                str_ima += num2[i]
        real = real * int(str_deg)
        imaginary = imaginary * int(str_ima)
        real_res = deg * real + -1 * ima * imaginary
        imaginary_res = deg * imaginary + real * ima
        ans = str(real_res) + '+' + str(imaginary_res) + 'i'
        # print(deg,ima)
        # print(real,imaginary)
        return (ans)