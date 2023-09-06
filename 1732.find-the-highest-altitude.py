#
# @lc app=leetcode id=1732 lang=python3
#
# [1732] Find the Highest Altitude
#


# @lc code=start
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans = curr = 0
        curr = 0

        for i in gain:
            curr += i
            ans = max(ans, curr)

        return ans


# @lc code=end
