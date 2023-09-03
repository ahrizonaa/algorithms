#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#


# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len([word for word in re.split(r"\s+", s) if word][-1])


# @lc code=end
