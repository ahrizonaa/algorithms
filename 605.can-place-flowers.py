#
# @lc app=leetcode id=605 lang=python3
#
# [605] Can Place Flowers
#


# @lc code=start
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        left = curr = 0
        size = len(flowerbed)
        while left < size and flowerbed[left] != 1:
            left += 1

        if left >= size:
            left += 1
            return (left // 2 if left % 2 != 0 else left / 2) >= n

        curr += left // 2 if left % 2 != 0 else left / 2

        right = left + 1

        while right < size:
            while right < size and flowerbed[right] != 1:
                right += 1
            dist = right - left - 1 if right < size else right - left
            curr += dist // 2 if dist % 2 != 0 else dist / 2 - 1
            left = right
            right += 1

        return curr >= n


# @lc code=end
