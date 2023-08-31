#
# @lc app=leetcode id=374 lang=python3
#
# [374] Guess Number Higher or Lower
#

# @lc code=start
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:


class Solution:
    def guessNumber(self, n: int) -> int:
        curr = delta = n // 2

        while True:
            delta = 1 if delta <= 1 else delta // 2
            res = guess(curr)
            if curr <= 0:
                return 1
            if curr >= n:
                return n
            if res == 0:
                return curr
            if res == -1:
                curr -= delta
            else:
                curr += delta


# @lc code=end
