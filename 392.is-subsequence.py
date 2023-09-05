#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#


# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        i = j = 0

        while i < len(t) and j < len(s):
            if s[j] == t[i] and j < len(s):
                j += 1
            i += 1

        return j == len(s)


# @lc code=end
