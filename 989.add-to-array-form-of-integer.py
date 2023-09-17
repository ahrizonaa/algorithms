#
# @lc app=leetcode id=989 lang=python3
#
# [989] Add to Array-Form of Integer
#


# @lc code=start
from typing import List


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        carry = n = 0

        j = 1
        k = [int(d) for d in str(k)]
        for i in range(len(num) - 1, -1, -1):
            if j <= len(k):
                n = num[i] + k[-j] + carry
            else:
                n = num[i] + carry
            if n > 9:
                carry = 1
                n = n % 10
            else:
                carry = 0
            num[i] = n
            j += 1
        m = j
        while j <= len(k):
            if carry:
                n = k[-j] + 1
                if n > 9:
                    carry = 1
                    n = n % 10
                else:
                    carry = 0
                k[-j] = n
            j += 1
            if j > len(k):
                return (
                    [1] + [int(d) for d in k[: -m + 1]] + num
                    if carry
                    else [int(d) for d in k[: -m + 1]] + num
                )
        return num if not carry else [1] + num


# @lc code=end
print(Solution().addToArrayForm([2, 7, 4], 181))
