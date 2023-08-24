#
# @lc app=leetcode id=235 lang=python3
#
# [235] Lowest Common Ancestor of a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans=None
        def dfs(node):
            if self.ans:
                return
            if (p.val<=node.val and q.val>=node.val) or (q.val<=node.val and p.val>=node.val) and not self.ans:
                self.ans=node
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
            
        dfs(root)
        return self.ans
# @lc code=end

