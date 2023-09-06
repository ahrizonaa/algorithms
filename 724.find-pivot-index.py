#
# @lc app=leetcode id=724 lang=python3
#
# [724] Find Pivot Index
#


# @lc code=start
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        right = 0
        for i in range(len(nums) - 1, 0, -1):
            right += nums[i]

        left = 0
        for i in range(len(nums)):
            if left == right:
                return i
            left += nums[i]
            right -= 0 if i >= len(nums) - 1 else nums[i + 1]

        return -1


# @lc code=end
