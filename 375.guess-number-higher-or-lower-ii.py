#
# @lc app=leetcode id=375 lang=python3
#
# [375] Guess Number Higher or Lower II
#


# @lc code=start
class Solution:
    def getMoneyAmount(self, n: int) -> int:
        if n <= 3:
            return n - 1

        dp = [[0] * (n + 1) for i in range(n + 1)]

        for i in range(2, n + 1):
            for l in range(1, n - i + 2):
                minimax = float("inf")
                for j in range(l, l + i - 1):
                    ans = j + max(dp[l][j - 1], dp[j + 1][l + i - 1])
                    minimax = min(ans, minimax)
                dp[l][l + i - 1] = minimax

        return dp[1][n]


# @lc code=end
