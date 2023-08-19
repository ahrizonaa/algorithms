#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#


# @lc code=start
from math import floor


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        nums = []
        while True:
            nums.append(x % 10)
            if nums[-1] == x:
                break
            x = floor(x / 10)
        for i in range(floor(len(nums) / 2)):
            if nums[i] != nums[len(nums) - i - 1]:
                return False

        return True


# @lc code=end
