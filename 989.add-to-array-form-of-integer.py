#
# @lc app=leetcode id=989 lang=python3
#
# [989] Add to Array-Form of Integer
#


# @lc code=start
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        sys.set_int_max_str_digits(10001)
        return [int(d) for d in list(str(int("".join([str(d) for d in num])) + k))]


# @lc code=end
