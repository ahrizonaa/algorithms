#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#


# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1

        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 10:
                digits[i] = 0
                if i - 1 >= 0:
                    digits[i - 1] += 1

        if not digits[0]:
            return [1] + digits
        return digits


# @lc code=end
