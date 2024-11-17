'''
https://leetcode.com/problems/integer-to-roman/?envType=problem-list-v2&envId=hash-table&status=SOLVED
'''
class Solution:
    def intToRoman(self, num: int) -> str:
        ans = ""
        ans += (num // 1000) * "M"
        hundreds = (num // 100) % 10
        tens = (num // 10) % 10
        ones = num % 10

        if hundreds <= 3:
            ans += hundreds * "C"
        elif hundreds == 4:
            ans += "CD"
        elif hundreds <= 8:
            ans += "D" + (hundreds - 5) * "C"
        elif hundreds == 9:
            ans += "CM"

        if tens <= 3:
            ans += tens * "X"
        elif tens == 4:
            ans += "XL"
        elif tens <= 8:
            ans += "L" + (tens - 5) * "X"
        elif tens == 9:
            ans += "XC"

        if ones <= 3:
            ans += ones * "I"
        elif ones == 4:
            ans += "IV"
        elif ones <= 8:
            ans += "V" + (ones - 5) * "I"
        elif ones == 9:
            ans += "IX"

        return ans
