#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#


# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = [s[0]]
        s = s[1:]
        end = {")", "}", "]"}
        pairs = {"(": ")", "{": "}", "[": "]"}
        for c in s:
            if c in end:
                if not stack:
                    return False
                while stack:
                    if stack[-1] in pairs and pairs[stack[-1]] == c:
                        stack.pop()
                        break
                    else:
                        return False
            else:
                stack.append(c)
        return len(stack) == 0


# @lc code=end
