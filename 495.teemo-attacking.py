#
# @lc app=leetcode id=495 lang=python3
#
# [495] Teemo Attacking
#


# @lc code=start
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        curr = 0
        n = len(timeSeries)
        for i, t in enumerate(timeSeries):
            if i + 1 < n:
                if t + duration - 1 >= timeSeries[i + 1]:
                    curr += timeSeries[i + 1] - t
                else:
                    curr += duration
            else:
                curr += duration

        return curr


# @lc code=end
