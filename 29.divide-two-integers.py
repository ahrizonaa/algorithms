#
# @lc app=leetcode id=29 lang=python3
#
# [29] Divide Two Integers
#


# @lc code=start
class Solution:
    def signer(self, n, dividend, divisor):
        if dividend < 0 and divisor < 0:
            return -n
        if dividend > 0 and divisor > 0:
            return n
        return -n

    def limiter(self, dividend):
        # print("limiter", dividend)
        if dividend < self.lower:
            return self.lower
        elif dividend > self.upper:
            return self.upper
        return dividend

    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0

        positive = True if dividend >> 31 == divisor >> 31 else False

        if abs(dividend) == abs(divisor):
            if positive:
                return 1
            return -1

        self.lower = -(2 << 30)
        self.upper = -self.lower - 1

        if positive:
            dividend = abs(dividend)
            divisor = abs(divisor)

        # print("here")
        if abs(divisor) == 1:
            # print(positive)
            if positive and dividend < 0:
                dividend = -dividend
                # print("44", dividend)
            return self.limiter(dividend)

        if dividend < self.lower:
            return self.lower
        if dividend > self.upper:
            return self.upper

        curr = abs(divisor)
        i = 1
        # print("while")
        while curr < abs(dividend):
            curr = curr << 1
            i += 1
            print(i, curr)

        i -= 2
        ans = (2 << i) - abs(divisor)
        return ans
        # return self.signer(ans, dividend, divisor)


# @lc code=end
print("ans", Solution().divide(2147483647, 2))

# 10
# 3
# 7
# -3
5
