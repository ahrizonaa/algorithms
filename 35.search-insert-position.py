#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#


# @lc code=start
class Solution:
    def searchInsert(self, nums, target: int) -> int:
        self.n = len(nums)
        curr = delta = self.n // 2

        if target > nums[-1]:
            return len(nums)
        if target <= nums[0]:
            return 0

        while True:
            delta = 1 if delta <= 1 else delta // 2
            if curr <= 0:
                return 0 if nums[0] >= target else 1
            if curr >= self.n - 1:
                return self.n if nums[-1] < target else self.n - 1
            if nums[curr] == target:
                return curr
            if nums[curr - 1] == target:
                return curr - 1
            if nums[curr + 1] == target:
                return curr + 1
            if target > nums[curr] and target < nums[curr + 1]:
                return curr + 1
            if target < nums[curr] and target > nums[curr - 1]:
                return curr
            if nums[curr] > target:
                curr -= delta
            else:
                curr += delta


# @lc code=end

ret = Solution().searchInsert([1, 2, 4, 6, 8, 9, 10], 10)
print("ans", ret)
