#
# @lc app=leetcode id=1768 lang=python3
#
# [1768] Merge Strings Alternately
#


# @lc code=start
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n, m = len(word1), len(word2)
        k = min(m, n)
        ans = [None] * (k * 2)

        for i in range(k):
            ans[2 * i] = word1[i]
            ans[2 * i + 1] = word2[i]

        return "".join(ans + list((word1[k:] if n > k else word2[k:])))


# @lc code=end
