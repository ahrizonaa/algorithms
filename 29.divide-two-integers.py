#
# @lc app=leetcode id=29 lang=python3
#
# [29] Divide Two Integers
#


# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -(2 << 30) and divisor == -1:
            return (2 << 30) - 1

        positive = True if dividend >> 31 == divisor >> 31 else False

        divisor = -divisor if divisor < 0 else divisor
        dividend = -dividend if dividend < 0 else dividend

        ans = 0
        while dividend >= divisor:
            i = 1
            curr = divisor
            while curr + curr <= dividend:
                curr = curr + curr
                i += i
            ans += i
            dividend = dividend - curr

        return ans if positive else -ans


# @lc code=end
