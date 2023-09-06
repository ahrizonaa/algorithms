#
# @lc app=leetcode id=725 lang=python3
#
# [725] Split Linked List in Parts
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(
        self, head: Optional[ListNode], k: int
    ) -> List[Optional[ListNode]]:
        ans, n, curr = [None] * k, 0, head
        while curr:
            curr = curr.next
            n += 1

        prequence = n % k

        curr = head
        i = 0
        while i < prequence and curr:
            tmp = curr
            j = k + 1
            while tmp and j > 1:
                tmp = tmp.next
                j -= 1
            ans[i] = curr
            if tmp:
                curr = tmp.next
                tmp.next = None
            i += 1

        while curr and i < k:
            tmp = curr
            j = k
            while tmp and j > 1:
                tmp = tmp.next
                j -= 1
            ans[i] = curr
            if tmp:
                curr = tmp.next
                tmp.next = None
            i += 1

        return ans


# @lc code=end
