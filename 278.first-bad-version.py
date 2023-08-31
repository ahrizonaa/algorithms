#
# @lc app=leetcode id=278 lang=python3
#
# [278] First Bad Version
#

# @lc code=start
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:


class Solution:
    def firstBadVersion(self, n: int) -> int:
        curr = delta = n // 2

        while True:
            delta = 1 if delta <= 1 else delta // 2
            res = isBadVersion(curr)
            if curr <= 0:
                return 1
            if curr >= n:
                return n
            if res and not isBadVersion(curr - 1):
                return curr
            if res:
                curr -= delta
            else:
                curr += delta


# @lc code=end
