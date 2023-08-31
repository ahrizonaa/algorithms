#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#


# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        filtered = [x for x in nums if x != val]

        for i in range(len(filtered)):
            nums[i] = filtered[i]

        return len(filtered)


# @lc code=end
