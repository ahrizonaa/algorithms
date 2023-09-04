#
# @lc app=leetcode id=1071 lang=python3
#
# [1071] Greatest Common Divisor of Strings
#


# @lc code=start
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        [A, B] = [str1, str2] if len(str1) < len(str2) else [str2, str1]

        for i in range(len(A), -1, -1):
            substr = A[:i]
            regx = "((" + substr + ")+)"
            occurrences = re.findall(regx, B)
            if len(occurrences) > 0 and len(occurrences[0][0]) == len(B):
                smaller = re.findall(regx, A)
                if len(smaller) > 0 and len(smaller[0][0]) == len(A):
                    return substr
        return ""


# @lc code=end
