#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#


# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        numerals = list(s)
        conv = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        for i, n in enumerate(numerals):
            val = conv[n]
            if i == 0:
                numerals[i] = val
            else:
                prev = val / numerals[i - 1]
                if prev == 5 or prev == 10:
                    numerals[i] = val - numerals[i - 1]
                    numerals[i - 1] = 0
                else:
                    numerals[i] = val
        return sum(numerals)


# @lc code=end
