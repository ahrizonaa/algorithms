#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#


# @lc code=start
class Solution:
    def binarysearch(self, nums, target, left, right):
        while left <= right:
            if left == right:
                return left if nums[left] == target else -1
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        return -1

    def binarysearch_left(self, nums, target, left, right):
        if left == right:
            if nums[left] == target:
                return left
            return left + 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                if mid == 0:
                    return 0
                if mid - 1 >= 0 and nums[mid - 1] != target:
                    return mid
                elif mid - 1 == 0 and nums[0] == target:
                    return 0
                right = mid - 1

            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

    def binarysearch_right(self, nums, target, left, right):
        if left == right:
            if nums[right] == target:
                return right
            return right - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                if mid + 1 <= self.n - 1 and nums[mid + 1] != target:
                    return mid
                elif mid + 1 == self.n - 1 and nums[-1] == target:
                    return self.n - 1
                left = mid + 1

            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

    def searchRange(self, nums, target):
        if not nums:
            return [-1, -1]
        self.n = len(nums)
        if self.n == 1:
            return [0, 0] if nums[0] == target else [-1, -1]

        found = self.binarysearch(nums, target, 0, self.n - 1)

        if found < 0 or found > self.n:
            return [-1, -1]

        start = end = -1

        if found - 1 >= 0 and nums[found - 1] == target:
            start = self.binarysearch_left(nums, target, 0, found - 1)
        else:
            start = found
        if found + 1 <= self.n - 1 and nums[found + 1] == target:
            end = self.binarysearch_right(nums, target, found + 1, self.n - 1)
        else:
            end = found
        return [start, end]


# @lc code=end
