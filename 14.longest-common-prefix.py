#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#


# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs):
        i = 0
        while i < min(list(map(lambda e: len(e), strs))):
            c = strs[0][i]
            for s in strs[1:]:
                if c != s[i]:
                    return strs[0][:i]
            i += 1
        return strs[0][:i]


# @lc code=end
