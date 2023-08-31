#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#


# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        uniq = sorted(list(set(nums)))
        for i in range(len(uniq)):
            nums[i] = uniq[i]
        return len(uniq)


# @lc code=end
