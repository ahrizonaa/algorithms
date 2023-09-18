#
# @lc app=leetcode id=151 lang=python3
#
# [151] Reverse Words in a String
#


# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed([w for w in re.split("\s+", s) if w]))


# @lc code=end
