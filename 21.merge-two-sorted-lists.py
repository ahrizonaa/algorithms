#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not list1 and list2:
            return list2
        elif not list2 and list1:
            return list1

        head = None
        curr = None
        if list1 and list2:
            if list1.val <= list2.val:
                head = list1
                list1 = list1.next
            else:
                head = list2
                list2 = list2.next
            curr = head

        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        while list1:
            curr.next = list1
            curr = curr.next
            list1 = list1.next

        while list2:
            curr.next = list2
            curr = curr.next
            list2 = list2.next

        return head


# @lc code=end
