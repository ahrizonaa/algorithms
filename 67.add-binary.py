#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

import itertools


# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        alen, blen = len(a), len(b)
        size = max(alen, blen)

        a = ([0] * (blen - alen) if alen < blen else []) + [int(n) for n in a]
        b = ([0] * (alen - blen) if blen < alen else []) + [int(n) for n in b]

        carry = 0
        for i in range(size - 1, -1, -1):
            s = a[i] + b[i] + carry

            if s == 2:
                carry = 1
                s = 0
            elif s == 3:
                carry = 1
                s = 1
            else:
                carry = 0
            a[i] = s

        return (str(carry) if carry else "") + "".join([str(n) for n in a])


# @lc code=end

print(Solution().addBinary("1101", "101"))
