#
# @lc app=leetcode id=345 lang=python3
#
# [345] Reverse Vowels of a String
#


# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ["a", "e", "i", "o", "u"]
        chars = list(s)
        n = len(chars)
        left = 0
        right = n - 1

        while left < right:
            while left < right and chars[left].lower() not in vowels:
                left += 1
            while right > left and chars[right].lower() not in vowels:
                right -= 1

            tmp = chars[left]
            chars[left] = chars[right]
            chars[right] = tmp

            left += 1
            right -= 1

        return "".join(chars)


# @lc code=end
